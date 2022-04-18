#include "Board.h"

Board::Board(Adafruit_ST7789* tft, FleetConfiguration* conf){
    display = tft;
    opponent_grid = new Grid(X_OFFSET, Y_OFFSET, display, CELL_WIDTH);
    player_grid = new Grid(X_OFFSET, PLAYER_Y_OFFSET, display, CELL_WIDTH);

    fleet = new Fleet(conf, player_grid);
}

void Board::draw(){
    opponent_grid->draw();
    player_grid->draw();

    fleet->carrier->blit();
    fleet->battleship->blit();
    fleet->destroyer->blit();
    fleet->submarine->blit();
    fleet->patrolboat->blit();
}