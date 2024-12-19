//
// Created by braml on 19/12/2024.
//
#include "saw.h"
#include "math.h"


Saw::Saw(float frequency, float samplerate) : Oscillator()
{
    std::cout << "Saw - constructor\n";
    this->frequency = frequency;
    this->samplerate = samplerate;
}



Saw::~Saw() {
    std::cout << "Saw - destructor\n";
}

void Saw::calculate()
{
    sample =  (2.0f * phase -1.0f) * amplitude;
}