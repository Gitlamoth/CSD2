#ifndef _INSTRUMENT_H_
#define _INSTRUMENT_H_

#include <iostream>

//So called Header file for resembling available variables

class instrument {
public:
//            CONSTRUCTOR
    instrument(float theString, float body);
    ~instrument();
    float radiation();

protected:

    float theString;
    float body;
    float hertz;


};

#endif

