#pragma once

#ifndef GAME_H
#define GAME_H

#include <Adafruit_ST7789.h>
#include "Grid.h"
#include "Ships.h"

#define SCREEN_WIDTH  135
#define SCREEN_HEIGHT 240
#define CELL_WIDTH    10
#define GRID_GAP      20
#define X_OFFSET      (( SCREEN_WIDTH - (CELL_WIDTH * 10) ) / 2)
#define Y_OFFSET      ((SCREEN_HEIGHT - ((CELL_WIDTH * 10 * 2))) / 2) - (GRID_GAP / 2)
#define PLAYER_Y_OFFSET Y_OFFSET + (CELL_WIDTH * 10) + GRID_GAP

class PlacementConfiguration{
    public:
        PlacementConfiguration(int8_t x, int8_t y, uint8_t rot_val){
            location = Coordinates{x, y};
            rotation = rot_val % 4;
        }
        Coordinates location;
        uint8_t rotation;
};

class GameConfiguration{
    public:
        GameConfiguration(){
            carrier_conf = new PlacementConfiguration(4, 5, 0);
            battleship_conf = new PlacementConfiguration(0, 0, 0);
            submarine_conf = new PlacementConfiguration(2, 0, 0);
            destroyer_conf = new PlacementConfiguration(4, 0, 0);
            patrolboat_conf = new PlacementConfiguration(6, 0, 1);
        }
        PlacementConfiguration* carrier_conf;
        PlacementConfiguration* battleship_conf;
        PlacementConfiguration* submarine_conf;
        PlacementConfiguration* destroyer_conf;
        PlacementConfiguration* patrolboat_conf;

};

class Game{

    public:
        Game(Adafruit_ST7789* tft, GameConfiguration* game_conf);
        void draw();
        void selectCell(Coordinates coords);
        void drawShip(Coordinates coords, uint8_t rotation);
        Carrier* carrier;
        Battleship* battleship;
        Destroyer* destroyer;
        Submarine* submarine;
        PatrolBoat* patrolboat;

    private:
        Grid* opponent_grid;
        Grid* player_grid;
        Adafruit_ST7789* display;
        
        
        
        


};


#endif