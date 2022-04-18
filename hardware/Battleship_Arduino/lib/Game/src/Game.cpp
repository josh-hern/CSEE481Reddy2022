#include "Game.h"
#include "Board.h"

Game::Game(Adafruit_ST7789* tft, GameConfiguration* game_conf){
    board = new Board(tft, game_conf->fleet_configuration);
}

void Game::draw(){ 
    Serial.println("Game calling draw");
    board->draw();
}

void Game::selectCell(Coordinates coords){
    board->opponent_grid->selectCell(coords.x, coords.y);
}

void Game::drawShip(Coordinates coords, uint8_t rotation){
    board->fleet->carrier->setRotation(rotation);
    board->fleet->carrier->setPosition(coords);    
    board->fleet->carrier->blit();
}