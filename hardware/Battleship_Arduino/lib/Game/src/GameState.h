#pragma once

#include <Board.h>
#include <Input.h>
#include "Ships.h"

#ifndef GAMESTATES_H
#define GAMESTATES_H

class GameState{

    public:
        virtual void draw() = 0;
        virtual void activate(UserInputs* inputs) = 0;
        ShipColorPalette* player_color_palette;
        ShipColorPalette* opponent_color_palette;
    
    private:
        virtual void attachInterrupts(UserInputs* inputs) = 0;

};

#endif

