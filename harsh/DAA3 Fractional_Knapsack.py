class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0
    for item in items:
        if capacity <= 0:  # If the knapsack is full, break
            break
        
        if item.weight <= capacity:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take the fractional part of the item
            total_value += item.value * (capacity / item.weight)
            capacity = 0  # Knapsack is now full

    return total_value

def main():
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        value = float(input(f"Enter the value of item {i + 1}: "))
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))
    max_value = fractional_knapsack(capacity, items)
    
    print(f"The maximum value in the knapsack is: {max_value:.2f}")

if __name__ == "__main__":
    main()

# Enter the number of items: 4
# Enter value and weight of item 1: 60 10
# Enter value and weight of item 2: 100 20
# Enter value and weight of item 3: 120 30
# Enter value and weight of item 4: 90 25
# Enter the maximum capacity of the knapsack: 50


"""
Problem Overview
In the Fractional Knapsack Problem:

Each item has a value and a weight.
You have a knapsack with a certain weight capacity.
You can take fractions of items to maximize the total value in the knapsack without exceeding its capacity.
Explanation of the Code
The code consists of three main components:

Item Class

The Item class represents an item with a value and a weight.
It also calculates the value-to-weight ratio (self.ratio), which is crucial for deciding which items to prioritize.
python
Copy code
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio
fractional_knapsack Function

This function performs the main logic of the Fractional Knapsack Problem.
Parameters:
capacity: The maximum weight the knapsack can hold.
items: A list of Item objects.
Steps in the function:

Step 1: Sort the items list by the value-to-weight ratio in descending order, so the items with the highest value-to-weight ratios come first.
Step 2: Initialize total_value to keep track of the total value accumulated in the knapsack.
Step 3: Iterate over the sorted items:
If capacity is less than or equal to zero, the knapsack is full, so break the loop.
If the item's weight is less than or equal to the remaining capacity, add its full value to total_value and reduce the capacity by the item’s weight.
If the item's weight exceeds the remaining capacity, take only a fraction of the item to fill the knapsack to capacity and break the loop.
Return total_value, which is the maximum value achievable for the given capacity.
python
Copy code
def fractional_knapsack(capacity, items):
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0
    for item in items:
        if capacity <= 0:  # Knapsack is full
            break
        
        if item.weight <= capacity:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.value * (capacity / item.weight)
            capacity = 0  # Knapsack is now full

    return total_value
main Function

This function takes input from the user to create items and the knapsack capacity, then calls fractional_knapsack to compute the maximum value achievable.
Steps in main:

Step 1: Get the number of items (n) and initialize an empty list items.
Step 2: For each item, prompt the user to enter its value and weight, then create an Item object and append it to items.
Step 3: Prompt the user to enter the capacity of the knapsack.
Step 4: Call fractional_knapsack with capacity and items, store the returned max_value.
Step 5: Print max_value, formatted to two decimal places.
python
Copy code
def main():
    n = int(input("Enter the number of items: "))
    items = []

    for i in range(n):
        value = float(input(f"Enter the value of item {i + 1}: "))
        weight = float(input(f"Enter the weight of item {i + 1}: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))
    max_value = fractional_knapsack(capacity, items)
    
    print(f"The maximum value in the knapsack is: {max_value:.2f}")
Execution Control

The code uses the if __name__ == "__main__": block to run the main() function, which allows this script to be imported as a module without executing the main logic.

python
Copy code
if __name__ == "__main__":
    main()

"""
