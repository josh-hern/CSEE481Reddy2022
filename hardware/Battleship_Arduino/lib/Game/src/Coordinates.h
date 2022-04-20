#pragma once

#ifndef COORDINATES_H
#define COORDINATES_H

#include <Adafruit_ST7789.h> //this is a sin.  it's only required for int8_t


class Coordinates{
    public:
        int8_t x;
        int8_t y;
        bool isInBounds();
        Coordinates operator+(Coordinates other);
        Coordinates operator-(Coordinates other);
        bool operator==(Coordinates other);

};

#endif