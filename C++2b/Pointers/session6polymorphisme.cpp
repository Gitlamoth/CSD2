// somethingpointer = &nice_thing

// nice_thing.show()

// (*somethingpointer).show()

// somethingpointer->show();

// Something* somethingpointer = new Something

class Oscillator
{
public:
    virtual getSample();
};

class Sine : public Oscillator
{
public:
    getSample();
};

class Square : public Oscillator
{
public:
    getSample();
};

Oscillator* oscillatorBank[3];

oscillatorBank[0] = new Sine;
oscillatorBank[1] = new Square;
oscillatorBank[2] = new Sine;