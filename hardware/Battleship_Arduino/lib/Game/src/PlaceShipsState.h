#pragma once

#ifndef PLACESHIPSSTATE_H
#define PLACESHIPSSTATE_H

#include "GameState.h"
#include "Grid.h"
#include "Ships.h"
#include "Coordinates.h"

class PlaceShipsState: public GameState{

    public:
        PlaceShipsState(Board* game_board);
        void draw();
        void activate(UserInputs* inputs);
        void rotateShip();
        void pickUpShip();
        void moveUp();
        void moveDown();
        void moveLeft();
        void moveRight();
    private:
        void attachInterrupts(UserInputs* inputs);
        Board* board;
        Coordinates cursor_position;
        uint8_t rotation;

};


#endif