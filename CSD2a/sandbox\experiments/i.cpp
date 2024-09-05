#include <iostream>
#include <numeric> // For std::gcd and std::lcm

namespace Calculator {

    // Calculate GCD and LCM between two numbers
    int calculateGCD(int a, int b) {
        return std::gcd(a, b);
    }

    int calculateLCM(int a, int b) {
        return std::lcm(a, b);
    }
}

int main() {
    int firstNumber, secondNumber;

    std::cout << "Enter the first positive integer: ";
    std::cin >> firstNumber;

    if (firstNumber <= 0) {
        std::cerr << "Please enter a positive integer." << std::endl;
        return 1;
    }

    std::cout << "Enter the second positive integer: ";
    std::cin >> secondNumber;

    if (secondNumber <= 0) {
        std::cerr << "Please enter a positive integer." << std::endl;
        return 1;
    }

    // Calculate GCD and LCM between the two numbers
    int gcdResult = Calculator::calculateGCD(firstNumber, secondNumber);
    int lcmResult = Calculator::calculateLCM(firstNumber, secondNumber);

    std::cout << "GCD of " << firstNumber << " and " << secondNumber << ": " << gcdResult << std::endl;
    std::cout << "LCM of " << firstNumber << " and " << secondNumber << ": " << lcmResult << std::endl;

    return 0;
}
