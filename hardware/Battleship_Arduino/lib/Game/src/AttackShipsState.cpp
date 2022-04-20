#include "AttackShipsState.h"

AttackShipsState* attackShipsState; // global pointer for callbacks

void attackStaticAttack(){
    attackShipsState->attack();
}

void moveUpStaticAttack(){
    attackShipsState->moveUp();
}

void moveDownStaticAttack(){
    attackShipsState->moveDown();
}

void moveLeftStaticAttack(){
    attackShipsState->moveLeft();
}

void moveRightStaticAttack(){
    attackShipsState->moveRight();
}

AttackShipsState::AttackShipsState(Board* game_board){
    board = game_board;
    cursor_position = {4, 4};
    player_color_palette = new ShipColorPalette();
    player_color_palette->ship_base = COLOR_GRAY;
    player_color_palette->ship_hit = COLOR_SELECTED;
    player_color_palette->ship_sunk = COLOR_DARK_RED;
}

void AttackShipsState::draw(){
    board->draw();
}

void AttackShipsState::activate(UserInputs* inputs){
    Serial.println("Attaching interrupts");
    attachInterrupts(inputs);
    Serial.println("Setting color palette");
    board->player_fleet->setColorPalette(player_color_palette);
    Serial.println("Color palette set");
    board->opponent_grid->selectCell(cursor_position);
}


void AttackShipsState::attachInterrupts(UserInputs* inputs){
    inputs->a->setHandler(attackStaticAttack);
    inputs->b->setHandler(NULL);
    inputs->up->setHandler(moveUpStaticAttack);
    inputs->down->setHandler(moveDownStaticAttack);
    inputs->left->setHandler(moveLeftStaticAttack);
    inputs->right->setHandler(moveRightStaticAttack);
}

void AttackShipsState::attack(){
    // TODO: what do we do if the space has already been attacked??
    Cell* selected_cell = board->attack_history->opponent_grid.getCell(
        cursor_position
    );
    TemporalCell* grid_cell = board->opponent_grid->getCell(cursor_position.x, cursor_position.y);
    if(selected_cell->isHit()) return; // already been attacked
    if(grid_cell->occupyingShip != NULL){

        grid_cell->occupyingShip->attackCoordinates(cursor_position);
        selected_cell->markHit();
        // TODO: should send to the server
        return;
    }
    // else, there is no ship there.
    grid_cell->setValue(COLOR_DARK_BLUE);
    selected_cell->markHit();

}
void AttackShipsState::moveUp(){
    if(cursor_position.y > 0){
        cursor_position.y--;
        board->opponent_grid->selectCell(cursor_position);
    }
}
void AttackShipsState::moveDown(){
    if(cursor_position.y < 9){
        cursor_position.y++;
        board->opponent_grid->selectCell(cursor_position);
    }
}
void AttackShipsState::moveLeft(){
    if(cursor_position.x > 0){
        cursor_position.x--;
        board->opponent_grid->selectCell(cursor_position);
    }
}
void AttackShipsState::moveRight(){
    if(cursor_position.x < 9){
        cursor_position.x++;
        board->opponent_grid->selectCell(cursor_position);
    }
}

