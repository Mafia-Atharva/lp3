#include <iostream>
using namespace std;

// Global variable to count recursive steps
int recursive_step_count = 0;

// Recursive Fibonacci function with step count
int fibonacci_recursive(int n) {
    recursive_step_count++; // Increment step count for each function call
    
    // Base cases
    if (n == 0) return 0;
    if (n == 1) return 1;
    
    // Recursive calls
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

// Iterative Fibonacci function with step count
int fibonacci_iterative(int n, int &iterative_step_count) {
    int a = 0, b = 1, c;

    // Direct return for first two values
    if (n == 0) {
        iterative_step_count++; // Increment for the initial step
        return 0;
    }
    if (n == 1) {
        iterative_step_count++; // Increment for the initial step
        return 1;
    }

    // Iteratively calculate Fibonacci number and count steps
    for (int i = 2; i <= n; i++) {
        iterative_step_count++; // Increment for each loop iteration
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n;

    cout << "Enter the Fibonacci term to calculate: ";
    cin >> n;

    // Calculate Fibonacci using recursion
    recursive_step_count = 0; // Reset recursive step count
    int fibonacci_value_recursive = fibonacci_recursive(n);

    // Calculate Fibonacci using iteration
    int iterative_step_count = 0; // Initialize iterative step count
    int fibonacci_value_iterative = fibonacci_iterative(n, iterative_step_count);

    // Output results
    cout << "Fibonacci Value (Recursive): " << fibonacci_value_recursive << endl;
    cout << "Fibonacci Value (Iterative): " << fibonacci_value_iterative << endl;
    cout << "Steps required using Recursion: " << recursive_step_count << endl;
    cout << "Steps required using Iteration: " << iterative_step_count << endl;

    return 0;
}
