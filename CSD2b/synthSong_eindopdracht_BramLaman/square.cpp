//
// Created by braml on 18/12/2024.
//

#include "square.h"


Square::Square(float frequency, float samplerate) : Oscillator()
{
    std::cout << "Square - constructor\n";
    this->frequency = frequency;
    this->samplerate = samplerate;
}



Square::~Square() {
    std::cout << "Square - destructor\n";
}

void Square::calculate() {
    if(phase < 0.5f){
        sample = -1 * amplitude;
    }
    else {
        sample = amplitude;
    }
}