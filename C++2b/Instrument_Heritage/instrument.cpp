#include "instrument.h"
#include <iostream>

// executionairies file, where executions are displayed
// the :: seem to be as a guidance for cross reffering 

//          ::      Refference
instrument::instrument(float theString, float body) {
    this -> theString = theString;
    this -> body = body;
    
}
instrument::~instrument(){

}

float instrument :: radiation() {
    hertz = theString * body;
    std::cout << "Radiating: " << hertz << " Hz" << std::endl;
    return hertz;
}

  