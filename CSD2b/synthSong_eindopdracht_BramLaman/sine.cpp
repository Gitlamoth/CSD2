#include "sine.h"


Sine::Sine(float frequency, float samplerate) : Oscillator()
{
  std::cout << "Sine - constructor\n";
  this->frequency = frequency;
  this->samplerate = samplerate;
}

Sine::~Sine() {
  std::cout << "Sine - destructor\n";
}

void Sine::calculate() {
  // NOTE 1. - frequency / SAMPLERATE can be implemented in a more efficient way
  sample = sin(pi * 2 * phase) * amplitude;
}