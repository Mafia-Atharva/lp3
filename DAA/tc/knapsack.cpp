#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Item class to store value and weight of each item
class Item {
public:
    int value, weight;

    // Constructor to initialize value and weight of an item
    Item(int value, int weight) {
        this->value = value;
        this->weight = weight;
    }

    // Value-to-weight ratio for comparison
    double valueToWeightRatio() const {
        return (double)value / weight;
    }
};

// Comparator function to sort items by value-to-weight ratio in descending order
bool compare(Item item1, Item item2) {
    return item1.valueToWeightRatio() > item2.valueToWeightRatio();
}

int main() {
    int n;

    // Input number of items
    cout << "Enter the number of items: ";
    cin >> n;

    vector<Item> items;

    // Input value and weight of each item
    for (int i = 0; i < n; i++) {
        int value, weight;
        cout << "Enter value and weight of item " << (i + 1) << ": ";
        cin >> value >> weight;
        items.push_back(Item(value, weight));
    }

    // Input the total weight capacity of the knapsack
    int capacity;
    cout << "Enter the maximum capacity of the knapsack: ";
    cin >> capacity;

    // Sort items by their value-to-weight ratio in descending order
    sort(items.begin(), items.end(), compare);

    double maxValue = 0.0; // Initialize total maximum value that can be obtained

    // Loop through each item
    for (auto& item : items) {
        if (capacity >= item.weight) {
            // If the knapsack can carry the entire item weight
            maxValue += item.value; // Add the full item value
            capacity -= item.weight; // Decrease knapsack capacity by item's weight
        } else {
            // If the knapsack cannot carry the entire item weight, take fraction
            double valuePerWeight = item.valueToWeightRatio(); // Value-to-weight ratio
            maxValue += valuePerWeight * capacity; // Add fraction of the item's value
            capacity = 0; // Knapsack is full
            break; // No more items can be added
        }
    }

    // Output the maximum value obtained
    cout << "Maximum value that can be obtained in the knapsack: " << maxValue << endl;

    return 0;
}
