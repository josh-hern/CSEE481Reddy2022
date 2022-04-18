#pragma once

#ifndef GAME_H
#define GAME_H

#include <Adafruit_ST7789.h>
#include "Grid.h"
#include "Ships.h"
#include "Board.h"
#include "GameState.h"
#include "Input.h"



class GameConfiguration{
    public:
        GameConfiguration(){
            fleet_configuration = new FleetConfiguration();
        }
        FleetConfiguration* fleet_configuration;

};

class Game{

    public:
        Game(Adafruit_ST7789* tft, GameConfiguration* game_conf, UserInputs* user_inputs);
        void draw();
        GameState* state;
        Board* board;
        UserInputs* inputs;
};


#endif