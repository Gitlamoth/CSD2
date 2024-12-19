//
// Created by braml on 18/12/2024.
//
#pragma once
#include "oscillator.h"

class Square : public Oscillator
{
public:
    //Constructor and destructor
    Square();
    Square(double frequency, double samplerate);
    ~Square();

    void calculate();


};


