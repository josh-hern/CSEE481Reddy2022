#pragma once

#include <Board.h>
#include <Input.h>

#ifndef GAMESTATES_H
#define GAMESTATES_H

class GameState{

    public:
        virtual void draw() = 0;
        virtual void attachInterrupts(UserInputs* inputs) = 0;

};

#endif

