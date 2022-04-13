#pragma once

#ifndef GRID_H
#define GRID_H

#include <Arduino.h>
#include <Adafruit_ST7789.h>

class Ship;

#define BACKGROUND_BLUE     0x4c78
#define SELECTED_CELL_COLOR 0xF800

class Coordinates{
    public:
        int8_t x;
        int8_t y;

        Coordinates operator+(Coordinates other){
            return Coordinates{
                (int8_t)(x + other.x),
                (int8_t)(y + other.y)
             };
        }

        Coordinates operator-(Coordinates other){
            return Coordinates{
                (int8_t)(x - other.x),
                (int8_t)(y - other.y)
             };
        }
};

class TemporalCell{
    public:

        uint8_t current_value;
        uint8_t previous_value;
        Coordinates location;
        Ship* occupyingShip;
        bool selected;

        TemporalCell(int8_t x, int8_t y){
            location = {x, y};
            current_value = 0;
            previous_value = 0xFF;
            selected = false;
            occupyingShip = NULL;
        }

        void setValue(uint8_t value){
            previous_value = current_value;
            current_value = value;
        }

        void setShip(Ship* to_set){
            occupyingShip = to_set;
        }

        void select(){
            selected = true;
        }

        void deselect(){
            selected = false;
        }

        bool isSelected(){
            return selected;
        }

        bool isEmpty(){
            return occupyingShip == NULL;
        }

        bool hasChanged(){
            return previous_value != current_value;
        }

        bool operator == (const TemporalCell& other){
            return other.current_value == this->current_value &&
            other.previous_value == this->previous_value;
        }

};

class Grid{

    public:
        Grid(uint8_t x, uint8_t y, Adafruit_ST7789* tft, uint8_t scale);
        void draw();
        void selectCell(uint8_t x, uint8_t y);
        TemporalCell* getCell(int8_t x, int8_t y);
        void drawCell(TemporalCell* value);

    
    private:
        uint8_t x_position;
        uint8_t y_position;
        uint8_t cell_scale;
        TemporalCell* selectedCell;
        TemporalCell* grid[10][10];
        Adafruit_ST7789* display;
        uint16_t colors[3] = {0xFFFF, 0xF800, 0x07e0}; 
};

#endif