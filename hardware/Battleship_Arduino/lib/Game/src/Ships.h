
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
        Carrier(Grid* grid): Ship((uint8_t)5, grid){}
};

class Battleship: public Ship{
    public:
        Battleship(Grid* grid): Ship((uint8_t)4, grid){}
};

class Destroyer: public Ship{
    public:
        Destroyer(Grid* grid): Ship((uint8_t)3, grid){}
};

class Submarine: public Ship{
    public:
        Submarine(Grid* grid): Ship((uint8_t)3, grid){}
};

class PatrolBoat: public Ship{
    public:
        PatrolBoat(Grid* grid): Ship((uint8_t)2, grid){}
};



#endif