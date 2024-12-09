//
// Created by braml on 02/12/2024.
//

#ifndef INSTRUMENT_H
#define INSTRUMENT_H

#endif //INSTRUMENT_H

class instrument {
public:
    // Default constructor
    instrument();

    // Method to play a specific sound
    void play(int index);

private:
    // Fixed-size array of strings
    const char* sound[4] = {"kadeng!", "katoef...", "SHALENGG!", "poef.."};
};


