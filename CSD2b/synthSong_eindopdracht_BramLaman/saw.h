//
// Created by braml on 19/12/2024.
//
#pragma once
#include "oscillator.h"

class Saw : public Oscillator
{
public:
    //Constructor and destructor
    Saw(float frequency, float samplerate = 44100);
    ~Saw();

    void calculate();
};


