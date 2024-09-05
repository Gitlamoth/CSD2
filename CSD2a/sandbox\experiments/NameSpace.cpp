#include <iostream>

//GPT LESSONING

// Define a namespace named "MyNamespace"
namespace MyNamespace {
    int x;
    void ingredients(int x) {
        std::cout << "Value of x: " << x << std::endl;
    }
};

int main() {
    MyNamespace::x = 5;

    // Accessing the variable and function within the namespace
    MyNamespace::ingeredients(MyNamespace::x);
    std::cout << "Value of x outside the namespace: " << MyNamespace::x << std::endl;

    return 0;
};
