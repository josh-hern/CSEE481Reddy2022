#pragma once

#ifndef INPUT_H
#define INPUT_H

#include <Arduino.h>
#include <FreeRTOS.h>

#define UP 35
#define DOWN 36
#define LEFT 39
#define RIGHT 34
#define A 25
#define B 26



class Button{
    public:
        Button(uint8_t pinNumber, void (isr)());
        void stateChangeISR();
        void setHandler(void (*fn)());
    
    private:
        uint16_t lastInterruptTime;
        bool lastState;
        uint8_t pin;
        SemaphoreHandle_t isrSemaphore;
        uint16_t count;
        void (*handler)();
};



class UserInputs{
    public:
        UserInputs();
        Button* up;
        Button* down;
        Button* left;
        Button* right;
        Button* a;
        Button* b;
};

void upISR();
void downISR();
void leftISR();
void rightISR();
void aISR();
void bISR();


#endif