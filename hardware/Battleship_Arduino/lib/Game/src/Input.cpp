#include "Input.h"

Button::Button(uint8_t pinNumber, void (*isr)()){
    lastState = HIGH;
    lastInterruptTime = 0;
    pin = pinNumber;
    handler = NULL;
    isrSemaphore = xSemaphoreCreateMutex();
    count = 0;
    uint8_t mode = INPUT;
    if(pinNumber == A || pinNumber == B){
        mode = INPUT_PULLUP;
    }
    pinMode(pinNumber, mode);
    attachInterrupt(pinNumber, isr, FALLING);
}

// Called when a button is pressed; will call the assigned handler callback
// if the appropriate amount of time has passed
void Button::stateChangeISR(){
    auto gotSemaphore = xSemaphoreTake(isrSemaphore, 0);
    if(gotSemaphore == pdFALSE){
        Serial.println("Failed to get semaphore");
        return;
    }
    lastState = digitalRead(pin);
    if((xTaskGetTickCount() - lastInterruptTime) > 250){
        if(lastState == LOW && handler != NULL) {
            count++;
            //Serial.printf("Failling edge detected: %d\n", count);
            handler();
        }
        lastInterruptTime = xTaskGetTickCount();
    }
    xSemaphoreGive(isrSemaphore);
}

void Button::setHandler(void (*fn)()){
    handler = fn;
}

UserInputs* inputs;

UserInputs::UserInputs(){
    up = new Button(UP, upISR);
    down = new Button(DOWN, downISR);
    left = new Button(LEFT, leftISR);
    right = new Button(RIGHT, rightISR);
    a = new Button(A, aISR);
    b = new Button(B, bISR);
}

/*
This is all very, very dumb.  Basically, you can't give
attachInterrupt a reference to a member function.  Or,
you probably can, but I'm not good enough at c++ to know how.
So, what we do instead is give it a reference to once of these
that is a non-member function, but has a reference to global
inputs.  So, then we can get the Button object reference
and call the stateChangeISR that we wanted to call in the first
place.  That debounces the input, and then calls whatever
handler has been assigned.  Stupid.
\
*/

void upISR(){
    inputs->up->stateChangeISR();
}

void downISR(){
    inputs->down->stateChangeISR();
}

void leftISR(){
    inputs->left->stateChangeISR();
}

void rightISR(){
    inputs->right->stateChangeISR();
}

void aISR(){
    inputs->a->stateChangeISR();
}

void bISR(){
    inputs->b->stateChangeISR();
}


