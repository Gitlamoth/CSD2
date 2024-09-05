#include "oscillator.h"

int main()
{
  std::cout << "\nin main\n";
  Oscillator osc;

  std::cout << "Frequency of the Oscillator object osc is: "
    << osc.getFreq() << "\n";

  osc.setFreq(440);
  std::cout << "Frequency of the Oscillator object osc is: "
    << osc.getFreq() << "\n";

  // end program
  return 0;
}
