#include "Grid.h"
#include <Adafruit_ST7789.h>

Grid::Grid(uint8_t x, uint8_t y, Adafruit_ST7789* tft, uint8_t scale){
    x_position = x;
    y_position = y;
    display = tft;
    cell_scale = scale;
    selectedCell = NULL;
    for(uint8_t y=0; y<10; y++){
        for(uint8_t x=0; x<10; x++){
            grid[x][y] = new TemporalCell(x, y);
        }
    }
}

void Grid::draw(){
    for(uint8_t y=0; y<10; y++){
        for(uint8_t x=0; x<10; x++){
            TemporalCell* cell = grid[x][y];
            if(cell->hasChanged()){
                drawCell(cell);
                cell->setValue(cell->current_value);
            }
        }
    } 
}

void Grid::selectCell(Coordinates coords){
    if(selectedCell != NULL){
        TemporalCell* prev_selected = selectedCell;
        prev_selected->deselect();
        drawCell(prev_selected);
    }
    if(coords.x > 9 || coords.y > 9 || coords.x < 0 || coords.y < 0) return;
    selectedCell = grid[coords.x][coords.y];
    selectedCell->select();
    drawCell(selectedCell);
}

TemporalCell* Grid::getCell(int8_t x, int8_t y){
    if(x < 0 || y < 0) return NULL;
    if(x > 9 || y > 9) return NULL;

    return grid[x][y];
}

void Grid::drawCell(TemporalCell* cell){
    if(cell == NULL) return; // return if there is no cell
    if(cell->location.x > 9 || cell->location.y >9) return; // return if out of bounds (prob not necessary)

    // get the cell's offset from 0 based on scale, and add grid offset
    uint8_t x_value = (cell->location.x*cell_scale) + x_position;
    uint8_t y_value = (cell->location.y*cell_scale) + y_position;

    // drawing the cell if it's selected
    if(cell->isSelected()){
        uint16_t color = cell->current_value;
        if(color == 0) color = COLOR_LIGHT_BLUE;
        display->fillRect(x_value, y_value, cell_scale, cell_scale, COLOR_SELECTED);
        display->fillRect(
            x_value+2, y_value+2, cell_scale - 4, cell_scale - 4, color
        );
 
    } 
    // drawing the cell if it's not selected
    else {
        uint16_t color = cell->current_value;
        if(color == 0) color = COLOR_LIGHT_BLUE;      
        display->drawRect(x_value, y_value, cell_scale, cell_scale, 0xFFFF);
        display->fillRect(
            x_value+1, y_value+1, cell_scale - 2, cell_scale - 2, color
        );
    }
    
}
    