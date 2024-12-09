#include <iostream>
#include "instrument.h"


// Constructor definition
instrument::instrument() {
    std::cout << "Instrument - constructor\n" << std::endl;
};


// Method to play a specific sound
void instrument::play(int index) {
    if (index >= 0 && index < 4) {
        std::cout << "Sound: " << sound[index] << std::endl;
    } else {
        std::cout << "Invalid sound index!" << std::endl;
    }
};


