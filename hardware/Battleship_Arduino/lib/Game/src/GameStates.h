#pragma once

#ifndef GAMESTATES_H
#define GAMESTATES_H

class GameState{

    public:
        virtual void draw() = 0;

};


class PlaceShips: GameState{

    public:
        PlaceShips();
        void draw();

};

#endif

