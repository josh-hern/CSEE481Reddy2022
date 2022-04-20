#include "AttackHistory.h"

Cell::Cell(){
    coords = {0, 0};
    hit = false;
}

Cell::Cell(uint8_t x, uint8_t y){
    coords = {(int8_t)x, (int8_t)y};
    hit = false;
}

void Cell::markHit(){
    hit = true;
}

bool Cell::isHit(){
    return hit;
}

AttackGrid::AttackGrid(){
    for(uint8_t y=0; y<10; y++){
        for(uint8_t x=0; x<10; x++){
            grid[x][y] = Cell(x, y);
        }
    }
}

Cell* AttackGrid::getCell(Coordinates to_get){
    if(!to_get.isInBounds()) return NULL;
    return &grid[to_get.x][to_get.y];
}

AttackHistory::AttackHistory(){
    player_grid = AttackGrid();
    opponent_grid = AttackGrid();
}