
#pragma once

#ifndef SHIPS_H
#define SHIPS_H

#include <Adafruit_ST7789.h>
#include "Grid.h"

typedef Coordinates Vector; // define Vector as a Coordinates

class Ship{
    public:
        Ship(uint8_t ship_length, Grid* grid_canvas);
        void setRotation(uint8_t rotation_value);
        void setPosition(Coordinates coords);
        void placeOnGrid(Coordinates coords);
        bool fitsAt(int8_t x, int8_t y);
        void blit();
        void unblit();
        char* ship_type;
    
    private:
        Grid* grid;
        uint8_t length;
        uint8_t rotation;
        Coordinates position;
        TemporalCell** ship_cells; //pointer to array with len = length
        Vector ROTATIONS[4];
        void initialize_rotations();
        void getShipCellCoordinates(int8_t x, int8_t y, Coordinates dest[]);
        void getShipCells(int8_t x, int8_t y, TemporalCell* dest[]);
};

class Carrier: public Ship{
    public:
        Carrier(Grid* grid): Ship((uint8_t)5, grid){
            ship_type = (char *) "Carrier";
        }
        
};

class Battleship: public Ship{
    public:
        Battleship(Grid* grid): Ship((uint8_t)4, grid){
            ship_type = (char *) "Battleship";
        }
};

class Destroyer: public Ship{
    public:
        Destroyer(Grid* grid): Ship((uint8_t)3, grid){
            ship_type = (char *) "Destroyer";
        }
};

class Submarine: public Ship{
    public:
        Submarine(Grid* grid): Ship((uint8_t)3, grid){
            ship_type = (char *) "Submarine";
        }
};

class PatrolBoat: public Ship{
    public:
        PatrolBoat(Grid* grid): Ship((uint8_t)2, grid){
            ship_type = (char *) "PatrolBoat";
        }
};

class ShipConfiguration{
    public:
        ShipConfiguration(int8_t x, int8_t y, uint8_t rot_val){
            location = Coordinates{x, y};
            rotation = rot_val % 4;
        }
        Coordinates location;
        uint8_t rotation;
};

class FleetConfiguration{
    public:
        FleetConfiguration(){
            carrier_conf = new ShipConfiguration(4, 5, 0);
            battleship_conf = new ShipConfiguration(0, 0, 0);
            submarine_conf = new ShipConfiguration(2, 0, 0);
            destroyer_conf = new ShipConfiguration(4, 0, 0);
            patrolboat_conf = new ShipConfiguration(6, 0, 1);
        }
        ShipConfiguration* carrier_conf;
        ShipConfiguration* battleship_conf;
        ShipConfiguration* submarine_conf;
        ShipConfiguration* destroyer_conf;
        ShipConfiguration* patrolboat_conf;
};

class Fleet{
    public:
        Fleet(FleetConfiguration* conf, Grid* grid);
        Carrier* carrier;
        Battleship* battleship;
        Destroyer* destroyer;
        Submarine* submarine;
        PatrolBoat* patrolboat;
};



#endif