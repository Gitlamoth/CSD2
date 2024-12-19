#pragma once

#include "synth.h"

#define NUM_SINES 5

class additivSineSynth : public Synth {
  public:
    additivSineSynth(float sampleRate);
    ~additivSineSynth();

    void setOscFreqs(float frequency) override;
    void tick() override;
    float getSamples() override;

  protected:
    //std::vector<Saw> saws;
};

