#include "oscillator.h"



//overkoepelende variabellen, maakt een module/element aanwezig in elk van de losse files


Oscillator::Oscillator() : Oscillator(220, 0)
{
    std::cout <<"Inside Oscillator constructor ()\n ";
}

Oscillator::~Oscillator()
{}