//
// Created by braml on 18/12/2024.
//

#pragma once

#include "math.h"
#include <iostream>
class Oscillator
{
public:
    Oscillator();
    ~Oscillator();
    //Constructor and destructor
    void setSamplerate(float samplerate);
    //return the current sample
    float getSamples();
    // go to next sample
    void tick();
    virtual void calculate() = 0;
    //getters and setters
    void setFrequency(float frequency);
    float getFrequency();

protected:
    const float pi = acos (-1.0f);  //atan(1) * 4; <-- vak van Pieter.
    float frequency;
    float amplitude = 1.0f;
    float phase {0.0};
    // sample contains the current sample
    float sample = 0.0;
    float samplerate = 44100.0f;
};

