#pragma once

#ifndef GAME_H
#define GAME_H

#include <Adafruit_ST7789.h>
#include "Grid.h"
#include "Ships.h"
#include "Board.h"



class GameConfiguration{
    public:
        GameConfiguration(){
            fleet_configuration = new FleetConfiguration();
        }
        FleetConfiguration* fleet_configuration;

};

class Game{

    public:
        Game(Adafruit_ST7789* tft, GameConfiguration* game_conf);
        void draw();
        void selectCell(Coordinates coords);
        void drawShip(Coordinates coords, uint8_t rotation);
        Board* board;
};


#endif