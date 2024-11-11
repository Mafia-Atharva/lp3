def knapsack(weights, values, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def main():
    n = int(input("Enter the number of items: "))
    weights = []
    values = []

    for i in range(n):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        values.append(value)
        weights.append(weight)

    capacity = int(input("Enter the capacity of the knapsack: "))
    max_value = knapsack(weights, values, capacity)

    print(f"The maximum value in the knapsack is: {max_value}")

if __name__ == "__main__":
    main()

# 0/1 Knapsack:
# Time Complexity: O(N * W), where 'N' is the number of items and 'W' is the knapsack capacity. 
# For each item, we traverse through all weight capacities 1 <= w <= W. This results in a time complexity of O(N * W).
# 
# Auxiliary Space: O(N * W). 
# The space complexity is due to the use of a 2D array `dp` of size N * W, where N is the number of items and W is the knapsack capacity.

# Example:
# Enter the capacity of the knapsack: 10
# Enter the number of items: 4
# Enter value and weight for item 1: 3 2
# Enter value and weight for item 2: 7 2
# Enter value and weight for item 3: 2 4
# Enter value and weight for item 4: 9 5
# Maximum Profit Earned: 12


"""
Code Explanation
Function knapsack:

Inputs:

weights: List of weights of each item.
values: List of values of each item.
capacity: Maximum weight capacity of the knapsack.
Output:

Returns the maximum value that can be achieved without exceeding the knapsack's capacity.
Steps:

Initialize DP Table (dp):

dp[i][w] will store the maximum value attainable with the first i items and a knapsack capacity w.
This table has (n+1) x (capacity+1) dimensions, initialized to 0.
Fill the DP Table:

For each item i (from 1 to n):
For each weight capacity w (from 1 to capacity):
If weights[i-1] (current item’s weight) is less than or equal to w, the item can be included. Choose the maximum between:
Excluding the item (value dp[i-1][w]).
Including the item (value values[i-1] + dp[i-1][w - weights[i-1]]).
Otherwise, if the item can't be included (weight exceeds w), copy the maximum value without including it: dp[i][w] = dp[i-1][w].
Return the result in dp[n][capacity] - maximum value achievable with all items and full capacity.

Function main:

Takes input for the number of items, each item’s value and weight, and the knapsack capacity.
Calls the knapsack function to compute the maximum value.
Outputs the result.
Walkthrough Example
Consider the following inputs:

Items: 3
Values: [60, 100, 120]
Weights: [10, 20, 30]
Capacity: 50
Execution Steps
Initialize dp table of size 4 x 51 (for 3 items plus one row for 0 items and a capacity up to 50).

Filling the DP table:

For each item i and capacity w, compute the maximum value:
Item 1 (weight 10, value 60):
For capacities from 10 to 50, include item 1 (since weight 10 ≤ w), so dp[1][w] = 60.
Item 2 (weight 20, value 100):
For capacities from 20 to 50, decide to include item 2. For example, at w=30, include item 2, giving dp[2][30] = 160.
Item 3 (weight 30, value 120):
For capacities from 30 to 50, include item 3. For example, at w=50, include items 2 and 3, giving dp[3][50] = 220.
Result:

dp[3][50] returns 220, which is the maximum value achievable.
"""