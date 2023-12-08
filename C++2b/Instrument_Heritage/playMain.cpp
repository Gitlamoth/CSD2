
#include "bass.h"
#include "violin.h"
#include <iostream>

//main function calling for Radiate to get back values from instrument.cpp via instrument.h
// 

int main() {
    
   violin hearViolin(3.0,4.0);
   bass hearBass(5.0,6.0);
    // hearViolin.radiation();
    // hearBass.radiation();
    float hertzOviolin = hearViolin.radiation();
    std::cout<<"Hertz:"<< hertzOviolin << std::endl;

    return 0;
}
