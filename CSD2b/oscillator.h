class Oscillator
{
public:
    Oscillator();
    Oscillator(float freq, float amp);
    ~Oscillator();

    void setFreq(float freq);
    float getFreq();

protected:
    Oscillator()
    float freq;
    float amp;
};