#include "Coordinates.h"

bool Coordinates::isInBounds(){
    return x >= 0 && y >= 0 && x < 10 && y < 10;
}

Coordinates Coordinates::operator+(Coordinates other){
    return Coordinates{
        (int8_t)(x + other.x),
        (int8_t)(y + other.y)
        };
}

Coordinates Coordinates::operator-(Coordinates other){
    return Coordinates{
        (int8_t)(x - other.x),
        (int8_t)(y - other.y)
        };
}

bool Coordinates::operator==(Coordinates other){
    return other.x == x && other.y == y;
}