#include "oscillator.h"

Oscillator::Oscillator() : Oscillator(220) // default frequency
{
  std::cout << "Inside Oscillator constructor ()\n";
}


Oscillator::Oscillator(float frequency) 
    : freq(frequency)
{
  std::cout << "Inside Oscillator constructor (frequency)\n";
}



Oscillator::~Oscillator()
{
  std::cout << "Inside Oscillator destructor\n";
}

void Oscillator::setFreq(float freq)
    
{
  if(freq > 20 && freq < 20000)
  {
    this -> freq = freq;
  }
  else
  {
    std::cout << "The frequency value is incorrect"
    << " please present a value in the interval [20, 20000]\n";
  }
}


float Oscillator::getFreq()
{
  return freq;
}