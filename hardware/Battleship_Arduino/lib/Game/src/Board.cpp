#include "Board.h"

Board::Board(Adafruit_ST7789* tft, FleetConfiguration* conf){
    display = tft;
    opponent_grid = new Grid(X_OFFSET, Y_OFFSET, display, CELL_WIDTH);
    player_grid = new Grid(X_OFFSET, PLAYER_Y_OFFSET, display, CELL_WIDTH);

    player_fleet = new Fleet(conf, player_grid);
    opponent_fleet = new Fleet(conf, opponent_grid);
    attack_history = new AttackHistory();
}

void Board::draw(){
    opponent_grid->draw();
    player_grid->draw();

    opponent_fleet->blit();
    player_fleet->blit();
    // player_fleet->carrier->blit();
    // player_fleet->battleship->blit();
    // player_fleet->destroyer->blit();
    // player_fleet->submarine->blit();
    // player_fleet->patrolboat->blit();
}