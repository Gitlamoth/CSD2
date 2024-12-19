//
// Edited from examples by Ciska on 18/12/2024.
//
#pragma once
#include "audiocomponent.h"
#include "synth.h"
//  Daan Schrier


#define SAMPLE_RATE 44100.0f

struct CustomCallback : AudioCallback {
    explicit CustomCallback (double Fs);

    ~CustomCallback() override;

    void prepare (int sampleRate = SAMPLE_RATE) override;
    void process (AudioBuffer buffer) override;
    double mtof(float mPitch);
    void updatePitch(Melody& melody, Square& square);

private:
    //synth synth{SAMPLE_RATE};
};


