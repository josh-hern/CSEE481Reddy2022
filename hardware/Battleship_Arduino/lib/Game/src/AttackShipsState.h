#pragma once

#ifndef ATTACKSHIPSSTATE_H
#define ATTACKSHIPSSTATE_H

#include "GameState.h"
#include "Grid.h"
#include "Ships.h"
#include "Coordinates.h"

class AttackShipsState: public GameState{

    public:
        AttackShipsState(Board* game_board);
        void draw();
        void activate(UserInputs* inputs);
        void attack();
        void moveUp();
        void moveDown();
        void moveLeft();
        void moveRight();
        
    private:
        void attachInterrupts(UserInputs* inputs);
        Board* board;
        Coordinates cursor_position;

};

#endif