#include "Game.h"

Game::Game(Adafruit_ST7789* tft, GameConfiguration* game_conf){
    display = tft;
    opponent_grid = new Grid(X_OFFSET, Y_OFFSET, display, CELL_WIDTH);
    player_grid = new Grid(X_OFFSET, PLAYER_Y_OFFSET, display, CELL_WIDTH);

    carrier = new Carrier(player_grid);
    battleship = new Battleship(player_grid);
    destroyer = new Destroyer(player_grid);
    submarine = new Submarine(player_grid);
    patrolboat = new PatrolBoat(player_grid);

    // CURSED WARNING: setRotation MUST be called before setPosition

    carrier->setRotation(game_conf->carrier_conf->rotation);
    battleship->setRotation(game_conf->battleship_conf->rotation);
    destroyer->setRotation(game_conf->destroyer_conf->rotation);
    submarine->setRotation(game_conf->submarine_conf->rotation);
    patrolboat->setRotation(game_conf->patrolboat_conf->rotation);

    carrier->setPosition(game_conf->carrier_conf->location);
    
    battleship->placeOnGrid(game_conf->battleship_conf->location);
    destroyer->placeOnGrid(game_conf->destroyer_conf->location);
    submarine->placeOnGrid(game_conf->submarine_conf->location);
    patrolboat->placeOnGrid(game_conf->patrolboat_conf->location);

}

void Game::draw(){
    opponent_grid->draw();
    player_grid->draw();

    carrier->blit();
    battleship->blit();
    destroyer->blit();
    submarine->blit();
    patrolboat->blit();

}

void Game::selectCell(Coordinates coords){
    opponent_grid->selectCell(coords.x, coords.y);
}

void Game::drawShip(Coordinates coords, uint8_t rotation){
    carrier->setRotation(rotation);
    carrier->setPosition(coords);    
    carrier->blit();
}