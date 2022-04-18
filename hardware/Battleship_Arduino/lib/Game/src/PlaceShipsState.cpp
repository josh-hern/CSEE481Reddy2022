#include "PlaceShipsState.h"
#include <Arduino.h>

PlaceShipsState* placeShipsState;


void rotateShipStatic(){
    placeShipsState->rotateShip();
}

void pickUpShipStatic(){
    placeShipsState->pickUpShip();
}

void moveUpStatic(){
    placeShipsState->moveUp();
}

void moveDownStatic(){
    placeShipsState->moveDown();
}

void moveLeftStatic(){
    placeShipsState->moveLeft();
}

void moveRightStatic(){
    placeShipsState->moveRight();
}

PlaceShipsState::PlaceShipsState(Board* game_board){
    board = game_board;
    cursor_position = {4, 4};
    rotation = 0;
}

void PlaceShipsState::draw(){
    board->draw();
}

void PlaceShipsState::attachInterrupts(UserInputs* inputs){
    inputs->a->setHandler(rotateShipStatic);
    inputs->b->setHandler(pickUpShipStatic);
    inputs->up->setHandler(moveUpStatic);
    inputs->down->setHandler(moveDownStatic);
    inputs->left->setHandler(moveLeftStatic);
    inputs->right->setHandler(moveRightStatic);
}

void PlaceShipsState::rotateShip(){
    rotation = (rotation + 1) % 4;
    board->fleet->carrier->setRotation(rotation);
}

void PlaceShipsState::pickUpShip(){

}

void PlaceShipsState::moveUp(){
    if(cursor_position.y > 0){
        cursor_position.y--;
        board->fleet->carrier->setPosition(cursor_position);
    }
}

void PlaceShipsState::moveDown(){
    if(cursor_position.y < 9){
        cursor_position.y++;
        board->fleet->carrier->setPosition(cursor_position);
    }
}

void PlaceShipsState::moveLeft(){
    if(cursor_position.x > 0){
        cursor_position.x--;
        board->fleet->carrier->setPosition(cursor_position);
    }
}

void PlaceShipsState::moveRight(){
    if(cursor_position.x < 9){
        cursor_position.x++;
        board->fleet->carrier->setPosition(cursor_position);
    }
}