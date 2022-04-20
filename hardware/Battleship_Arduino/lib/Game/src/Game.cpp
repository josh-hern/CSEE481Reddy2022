#include "Game.h"
#include "Board.h"
#include "GameState.h"

extern PlaceShipsState* placeShipsState;
extern AttackShipsState* attackShipsState;

Game::Game(Adafruit_ST7789* tft, GameConfiguration* game_conf, UserInputs* user_inputs){
    inputs = user_inputs;
    board = new Board(tft, game_conf->fleet_configuration);

    placeShipsState = new PlaceShipsState(board);
    attackShipsState = new AttackShipsState(board);
    Serial.println("About to activate state");
    //placeShipsState->activate(inputs);
    attackShipsState->activate(inputs);
    //state = placeShipsState;
    state = attackShipsState;
}

void Game::draw(){ 
    state->draw();
}

