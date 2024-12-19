//
// Created by braml on 18/12/2024.
//

#include "synth.h"

Synth::Synth(float sampleRate) : sampleRate(sampleRate) {
    std::cout << "Synth - Constructor\n";
}

Synth::~Synth(){
	std::cout<<"Synth - destructor"<<std::endl;
}

float Synth::mtof(float midiPitch){
    return 440.0 * pow (2.0, (midiPitch - 69.0f) / 12.0f);
}

// void Synth::updatePitch(Melody &melody, Square &square) {
//     float note = melody.getNote();
//     double freq = mtof (note);
//     std::cout << "next note: " << note << ", has frequency " << freq
//               << std::endl;
//     square.setFrequency (freq);
// }

void Synth::updateFrameIndex() {
    if (frameIndex >= noteDelayFactor * sampleRate) {
        frameIndex = 0;
        updatePitch();
    } else {
        frameIndex++;
    }
}
