#include <iostream>
#include "instrument.h"
#include <string>

//main function calling for Radiate to get back values from instrument.cpp via instrument.h
// 

int main() {
    
    Instrument Radiate(40, 80);

    
    Radiate.radiation();

    
    Radiate.hz();

    return 0;
}
