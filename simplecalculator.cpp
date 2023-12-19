#include <iostream>

// Function to add two numbers
double add(double a, double b) {
    return a + b;
}

// Function to subtract two numbers
double subtract(double a, double b) {
    return a - b;
}

// Function to multiply two numbers
double multiply(double a, double b) {
    return a * b;
}

// Function to divide two numbers
double divide(double a, double b) {
    if (b != 0) {
        return a / b;
    } else {
        std::cout << "Error! Division by zero is not allowed.\n";
        return 0;
    }
}

int main() {
    char operation;
    double num1, num2;

    do {
        // Display menu
        std::cout << "Choose an operation (+, -, *, /, q to quit): ";
        std::cin >> operation;

        // Check if the user wants to quit
        if (operation == 'q' || operation == 'Q') {
            break;
        }

        // Get input from the user
        std::cout << "Enter two numbers: ";
        std::cin >> num1 >> num2;

        // Perform the calculation based on the chosen operation
        switch (operation) {
            case '+':
                std::cout << "Result: " << add(num1, num2) << "\n";
                break;
            case '-':
                std::cout << "Result: " << subtract(num1, num2) << "\n";
                break;
            case '*':
                std::cout << "Result: " << multiply(num1, num2) << "\n";
                break;
            case '/':
                std::cout << "Result: " << divide(num1, num2) << "\n";
                break;
            default:
                std::cout << "Invalid operation. Try again.\n";
        }

    } while (true);

    std::cout << "Calculator closed.\n";

    return 0;
}
