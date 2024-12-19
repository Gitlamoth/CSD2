//
// Created by braml on 18/12/2024.
//
#pragma once
#include <iostream>
#include "square.h"
#include "melody.h"

class Synth{
public:
    //constructors
    Synth();
    ~Synth();
protected:
    //methods
    void play();
    // set frequency for all oscillators
    virtual void setOscFreqs(float frequency) = 0;
    float mtof(float midiPitch);
    void updatePitch(Melody& melody, Square& square);

    virtual float getSamples();
    float samples;
    float sampleRate;
    virtual void tick();
    void updateFrameIndex();

    int frameIndex = 0;
    double noteDelayFactor = 0.11;
    float sample;
    float amplitude;
};


