#include "instrument.h"
#include <iostream>

// executionairies file, where executions are displayed
// the :: seem to be as a guidance for cross reffering 

Instrument::Instrument(float string, float body) {
    String = string;
    Body = body;
    Hertz = 0; // Initialize Hertz to 0
}

    void Instrument :: radiation() {
        Hertz = String * Body;
        std::cout << "Radiating: " << Hertz << " Hz" << std::endl;
    }

    void Instrument :: hz() {
        std::cout << "Current Hertz: " << Hertz << " Hz" << std::endl;
    }