#include <iostream>

// 3 type access specifiers:
// public, protected, private

class Oscillator
{
private:
  float freq;

public:
  Oscillator();
  Oscillator(float freq);
  ~Oscillator();

  void setFreq(float freq);
  float getFreq();

};
