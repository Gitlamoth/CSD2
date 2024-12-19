//
// Created by braml on 18/12/2024.
//

#include "oscillator.h"
#include <iostream>

Oscillator::Oscillator()
{
    std::cout << "Oscillator - constructor" << std::endl;
}

Oscillator::~Oscillator(){
    std::cout << "Oscillator - destructor" << std::endl;
}


void Oscillator::setSamplerate(float samplerate) {
    this->samplerate =samplerate;
}

float Oscillator::getSamples() {
    return sample;
}

void Oscillator::tick(){
    phase += frequency / samplerate;
    if(phase > 1.0f) {
        phase -= 1.0f;
    }
    calculate();
}

//getters and setters
void Oscillator::setFrequency(float frequency)
{
    // TODO add check to see if parameter is valid
    this->frequency = frequency;
}

float Oscillator::getFrequency()
{
    return frequency;
}