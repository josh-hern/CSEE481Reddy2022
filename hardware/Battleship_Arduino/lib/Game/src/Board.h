#pragma once

#include <Ships.h>
#include <Adafruit_ST7789.h>
#include <Grid.h>
#include "AttackHistory.h"

#ifndef BOARD_H
#define BOARD_H

#define SCREEN_WIDTH  135
#define SCREEN_HEIGHT 240
#define CELL_WIDTH    10
#define GRID_GAP      20
#define X_OFFSET      (( SCREEN_WIDTH - (CELL_WIDTH * 10) ) / 2)
#define Y_OFFSET      ((SCREEN_HEIGHT - ((CELL_WIDTH * 10 * 2))) / 2) - (GRID_GAP / 2)
#define PLAYER_Y_OFFSET Y_OFFSET + (CELL_WIDTH * 10) + GRID_GAP

class Board{

    public:
        Board(Adafruit_ST7789* tft, FleetConfiguration* fleet_conf);
        void draw();
        Fleet* player_fleet;
        Fleet* opponent_fleet;
        Grid* opponent_grid;
        Grid* player_grid;
        AttackHistory* attack_history;

    private:
        Adafruit_ST7789* display;

};


#endif

