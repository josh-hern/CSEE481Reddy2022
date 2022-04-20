#pragma once

#ifndef ATTACKHISTORY_H
#define ATTACKHISTORY_H

#include "Coordinates.h"

class Cell{
    public:
        Cell();
        Cell(uint8_t x, uint8_t y);
        void markHit();
        bool isHit();
        Coordinates coords;
    private:
        bool hit;
};

class AttackGrid{
    public:
        AttackGrid();
        Cell* getCell(Coordinates to_get);

    private:
        Cell grid[10][10];
};

class AttackHistory{

    public:
        AttackHistory();
        AttackGrid player_grid;
        AttackGrid opponent_grid;

};

#endif