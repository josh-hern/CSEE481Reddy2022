#include "Ships.h"
#include <Arduino.h>

Ship::Ship(uint8_t ship_length, Grid* grid_canvas){
    initialize_rotations();
    grid = grid_canvas;
    length = ship_length;
    rotation = 0;
    position = Coordinates {0,0};
    ship_cells = (TemporalCell**) malloc(sizeof(TemporalCell*) * ship_length);
    hit_index = new bool[length];    
    for(int i=0; i<length; i++){
        ship_cells[i] = NULL;
        hit_index[i] = false;
    }
    color_palette = new ShipColorPalette();

}

void Ship::initialize_rotations(){
    ROTATIONS[0] = Vector{0, 1};
    ROTATIONS[1] = Vector{1, 0};
    ROTATIONS[2] = Vector{0, -1};
    ROTATIONS[3] = Vector{-1, 0};
}

void Ship::setRotation(uint8_t rotation_value){
    rotation = rotation_value % 4;
}

void Ship::setPosition(Coordinates coords){
    position.x = coords.x;
    position.y = coords.y;
    for(uint8_t i=0; i<length; i++){
        TemporalCell* cell = ship_cells[i];
        if(cell != NULL){
            //only set to null if we're the owner
            if(cell->occupyingShip == this) cell->occupyingShip = NULL;
            cell->setValue((uint16_t) 0);
        }
    }
    getShipCells(position.x, position.y, ship_cells);
}

void Ship::placeOnGrid(Coordinates coords){
    Serial.println("Attempting to place on grid");
    Serial.printf("x: %d, y: %d\n", coords.x, coords.y);
    if(!fitsAt(coords.x, coords.y)) return;
    Serial.println("Placing on grid");
    setPosition(coords);
    //TemporalCell* cells[length];
    //getShipCells(coords.x, coords.y, cells);

    for(uint8_t i=0; i<length; i++){
        TemporalCell* cell = ship_cells[i];
        Serial.printf("Index: %d, x: %d, y: %d\n", i, cell->location.x, cell->location.y);
    }
    
    for(uint8_t i=0; i<length; i++){
        TemporalCell* cell = ship_cells[i];
        Serial.printf("Index: %d, x: %d, y: %d\n", i, cell->location.x, cell->location.y);
        if(cell == NULL){
            Serial.println("ERROR: cell was NULL and should not have been");
            return;
        }
        if(cell->occupyingShip != NULL){
            Serial.println("ERROR: cell has a ship already and should not");
            Serial.printf("Index: %d, x: %d, y: %d\n", i, cell->location.x, cell->location.y);
            Serial.printf("Pointer: %X\n", ((unsigned int)cell->occupyingShip));
            return;
        }
        cell->occupyingShip = this;
    }

    TemporalCell* cell = grid->getCell(4, 2);
    Serial.printf("x: %d, y: %d, occupied: %X", cell->location.x, cell->location.y, cell->occupyingShip);


}

/*
Ships will be considered to fit if all of their cells
fit on the board and are not already occupied.
Additionally, any of their adjacent cells may not be
occupied by another ship.

A ship might be thought of as a matrix:

oooooo      ooo
oxxxxo      oxo
oooooo      oxo
            oxo
            oxo
            ooo

Where O's are adjacent spaces and X's are the ship itself.
O's may be off of the board, but X's may not be.

This function will get an array of the coordinates and check
that they are all within the gameboard.  If they are not,
it returns false. It will also check if those spaces are
already occupied.

Then, it will get an array of the adjacent cells that are
on the board.  Then, it will check if they are occupied.
If they are, it will return false.

If the above conditions are met, it will return true.


Rotations will not truly be handled. if the rotation is 0
or 2, the x value for the ship pieces will always be the same.
If 0, the y value will be incremented from 0.  If 2, it will be
decremented from 0.  This will be done using coordinates acting
as a vector.
*/
bool Ship::fitsAt(int8_t x, int8_t y){

    Coordinates ship_coords[length];
    getShipCellCoordinates(x, y, ship_coords);

    for (uint8_t i=0; i<length; i++){
        Coordinates c = ship_coords[i];
        // TODO: check that coordinates are not NULL
        TemporalCell* cell = grid->getCell(c.x, c.y);
        if(cell == NULL){
            Serial.printf("Does not fit because cell is null for %s\n", ship_type);
            return false;
        }
        if(cell->occupyingShip != NULL && cell->occupyingShip != this){
            Serial.printf("Does not fit because occupied by %s:\n"
                "\tx: %d\n\ty: %d\n", cell->occupyingShip->ship_type,
                cell->location.x, cell->location.y);
            return false;
        }

    }

    uint8_t num_adjacent_cells = (length * 2) + 6; // 6 because can't be diagonal
    Coordinates adjacent_cells[num_adjacent_cells]; // length on either side + ends
    
    Vector current_rotation = ROTATIONS[rotation];
    Vector v = ROTATIONS[(rotation + 1) % 4]; // get 90 rotation of rotation

    // subtract the rotation vector from the first ship cell
    // coordinates to get the space before the ship.
    int8_t x_position = ship_coords[0].x - current_rotation.x;
    int8_t y_position = ship_coords[0].y - current_rotation.y;

    adjacent_cells[0] = Coordinates{x_position, y_position};
    adjacent_cells[1] = adjacent_cells[0] + v; // these get the adjacent diagonal cells
    adjacent_cells[2] = adjacent_cells[0] - v;
    
    //add the rotation vector to get space after ship, and then adjacent cells
    x_position = ship_coords[length - 1].x + current_rotation.x;
    y_position = ship_coords[length - 1].y + current_rotation.y;
    adjacent_cells[3] = Coordinates{x_position, y_position};
    adjacent_cells[4] = adjacent_cells[3] + v; // these get the adjacent diagonal cells
    adjacent_cells[5] = adjacent_cells[3] - v;

    // indices add 6 to skip over the "end caps"
    // indices are i * 2 so that there are two spaces to place coords
    // add 1 for the second one so it goes in the second slot.
    // i'm sorry
    for(uint8_t i=0; i<length; i++){
        Coordinates c = ship_coords[i];
        adjacent_cells[6 + (2 * i)] = c + (Coordinates)v;
        adjacent_cells[6 + (2 * i) + 1] = c - (Coordinates)v;
    }

    for(uint8_t i=0; i<num_adjacent_cells; i++){
        Coordinates c = adjacent_cells[i];
        TemporalCell* cell = grid->getCell(c.x, c.y);

        if(cell != NULL && cell->occupyingShip != NULL && cell->occupyingShip != this) return false; // if occupied and not by this
    }

    return true;
}

bool Ship::indexHit(uint8_t index){
    if(index >= length){ //return if out of bounds
        return false;
    }
    return hit_index[index];
}

bool Ship::coordinatesHit(Coordinates coords){
    int8_t index = getShipIndexFromCoords(coords);
    if(index < 0 || index > length) return false;
    return indexHit(index);
}

bool Ship::isSunk(){
    for(uint8_t i=0; i<length; i++){
        if(!indexHit(i)) return false;
    }
    return true;
}

// get the index of the ship that the passed coordinates are located on.
// if the coordinates are not on the ship, return -1.
int8_t Ship::getShipIndexFromCoords(Coordinates coords){
    Coordinates ship_coords[length];
    getShipCellCoordinates(position.x, position.y, ship_coords);
    for(uint8_t i=0; i<length; i++){
        if(ship_coords[i] == coords){
            return i; // this is the index we're looking for!
        }
    }

    return -1; // coordinates weren't on the ship
}

void Ship::attackCoordinates(Coordinates coords){
    int8_t index = getShipIndexFromCoords(coords);
    if(index < 0){
        Serial.println("Error! Coordinates were not on the attacked ship but should have been");
        return;
    } else if(index >= length){
        Serial.println("Error! index returned was greater than ship allows");
        return;
    }
    // Serial.printf("Address of this %s: %X\n", ship_type, this);
    // Serial.printf("Address of hit_index: %X\n", hit_index);
    // Serial.printf("Marking index %d hit on %s\n", index, ship_type);
    hit_index[index] = true;
    // Serial.printf("Reading back marked value: %d\n", hit_index[index]);
}

void Ship::getShipCellCoordinates(int8_t x, int8_t y, Coordinates dest[]){
    Vector current_rotation = ROTATIONS[rotation];
    for(uint8_t i=0; i<length; i++){
        int8_t x_position = (current_rotation.x * i) + x;
        int8_t y_position = (current_rotation.y * i) + y;
        dest[i] = Coordinates{x_position, y_position};
    }
}

void Ship::getShipCells(int8_t x, int8_t y, TemporalCell* dest[]){
    Coordinates coords[length];
    getShipCellCoordinates(x, y, coords);

    for(uint8_t i=0; i<length; i++){
        dest[i] = grid->getCell(coords[i].x, coords[i].y);
    }
}

void Ship::blit(){
    unblit();
    Coordinates ship_coordinates[length];
    getShipCellCoordinates(position.x, position.y, ship_coordinates);
    bool fits = fitsAt(position.x, position.y);
    bool placing = (color_palette->ship_hit == 0);
    bool sunk = isSunk();
    // Serial.printf("Address of this %s: %X\n", ship_type, this);
    // Serial.printf("Address of hit_index for ship %s: %X\n", ship_type, hit_index);
    for(int i=0; i<length; i++){
        // TODO: simplify this
        Coordinates c = ship_coordinates[i];
        TemporalCell* cell = grid->getCell(c.x, c.y);
        ship_cells[i] = cell;

        uint16_t value = (fits)? color_palette->ship_fits : color_palette->ship_doesnt_fit;
        if(!placing){
            // Serial.printf("%s reports %d for being hit at %d\n", ship_type, indexHit(i), i);
            if(sunk) value = color_palette->ship_sunk;
            else if(indexHit(i)){ 
                // Serial.printf("Blitting index %d as %X on %s\n", i, color_palette->ship_hit, ship_type);
                value = color_palette->ship_hit;
            }
            else value = color_palette->ship_base;
        }
        if(value == 0) value = COLOR_LIGHT_BLUE;

        if(cell != NULL){
            cell->setValue(value);
            grid->drawCell(cell);
        }
    }
}



void Ship::unblit(){
    
    for(int i=0; i<length; i++){
        TemporalCell* cell = ship_cells[i];
        if(cell != NULL){
            cell->setValue((uint16_t) 0);
        } else{
            Serial.printf("Error: cell value was NULL for ship %s\n", ship_type);
        }
    }
}

void Ship::setColorPalette(ShipColorPalette* palette){
    Serial.printf("Setting palette for %s\n", ship_type);
    color_palette->ship_fits         = palette->ship_fits;
    color_palette->ship_doesnt_fit   = palette->ship_doesnt_fit;
    color_palette->ship_base         = palette->ship_base;
    color_palette->ship_hit          = palette->ship_hit;
    color_palette->ship_sunk         = palette->ship_sunk;

}


Fleet::Fleet(FleetConfiguration* conf, Grid* grid){
    Serial.println("Creating fleet");
    carrier = new Carrier(grid);
    battleship = new Battleship(grid);
    destroyer = new Destroyer(grid);
    submarine = new Submarine(grid);
    patrolboat = new PatrolBoat(grid);

    Serial.println("Fleet created");

    // CURSED WARNING: setRotation MUST be called before setPosition

    carrier->setRotation(conf->carrier_conf->rotation);
    battleship->setRotation(conf->battleship_conf->rotation);
    destroyer->setRotation(conf->destroyer_conf->rotation);
    submarine->setRotation(conf->submarine_conf->rotation);
    patrolboat->setRotation(conf->patrolboat_conf->rotation);

    carrier->setPosition(conf->carrier_conf->location);
    
    battleship->placeOnGrid(conf->battleship_conf->location);
    destroyer->placeOnGrid(conf->destroyer_conf->location);
    submarine->placeOnGrid(conf->submarine_conf->location);
    patrolboat->placeOnGrid(conf->patrolboat_conf->location);

    Serial.println("Fleet placed");
}

void Fleet::blit(){
    carrier->blit();
    battleship->blit();
    destroyer->blit();
    submarine->blit();
    patrolboat->blit();
}

void Fleet::setColorPalette(ShipColorPalette* palette){
    carrier->setColorPalette(palette);
    battleship->setColorPalette(palette);
    destroyer->setColorPalette(palette);
    submarine->setColorPalette(palette);
    patrolboat->setColorPalette(palette);

}