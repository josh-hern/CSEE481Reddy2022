#pragma once

#ifndef PLACESHIPSSTATE_H
#define PLACESHIPSSTATE_H

#include "GameState.h"
#include "Grid.h"

class PlaceShipsState: public GameState{

    public:
        PlaceShipsState(Board* game_board);
        void draw();
        void attachInterrupts(UserInputs* inputs);
        void rotateShip();
        void pickUpShip();
        void moveUp();
        void moveDown();
        void moveLeft();
        void moveRight();
    private:
        Board* board;
        Coordinates cursor_position;
        uint8_t rotation;

};


#endif