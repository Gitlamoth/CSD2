#include "additivSineSynth.h"

additivSineSynth::additivSineSynth(float sampleRate): Synth(sampleRate)
{
    std::cout << "additivSineSynth - constructor\n";

    std::array<float, NUM_SINES> detuneValues = {-8.0f, -4.0f, 0.0f, 4.0f, 8.0f};

    sines.reserve(NUM_SINES); // prevent sines from being constructed twice by reserving space
    for (float detune : detuneValues) {
        sines.emplace_back(detune, sampleRate);
    }
}

additivSineSynth::~additivSineSynth() {
    std::cout << "additivSineSynth - destructor\n";
}


void additivSineSynth::setOscFreqs(float frequency) {
    for (int i = 0; i < NUM_SINES; i++) {
        sines[i].setFrequency(frequency);
    }
}

void additivSineSynth::tickAll() {
    for (int i = 0; i < NUM_SINES; i++) {
        sines[i].tick();
    }
    updateFrameIndex();
}

float additivSineSynth::getSamples() {
    float samples = 0;
    for (int i = 0; i < NUM_SINES; i++) {
        samples += sines[i].getSample();
    }
    _samples = samples/NUM_SINES;
}