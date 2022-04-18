#include "Game.h"
#include "Board.h"
#include "GameState.h"
#include "PlaceShipsState.h"

extern PlaceShipsState* placeShipsState;

Game::Game(Adafruit_ST7789* tft, GameConfiguration* game_conf, UserInputs* user_inputs){
    inputs = user_inputs;
    board = new Board(tft, game_conf->fleet_configuration);
    placeShipsState = new PlaceShipsState(board);
    placeShipsState->attachInterrupts(inputs);
    state = placeShipsState;
}

void Game::draw(){ 
    //Serial.println("Game calling draw");
    state->draw();
}

