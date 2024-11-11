#include<iostream>

using namespace std;

int main(){
    int capacity = 10;
    int items = 4;
    int price[items + 1] = {0, 3, 7, 2, 9};
    int wt[items + 1] = {0, 2, 2, 4, 5};
    int dp[items + 1][capacity + 1];
    
    for(int i = 0; i <= items; i++){
        for(int j = 0; j <= capacity; j++){
            if(i == 0 || j == 0){
                //There's nothing to add to Knapsack
                dp[i][j] = 0;
            }
            else if(wt[i] <= j){
                //Choose previously maximum or value of current item + value of remaining weight
                dp[i][j] = max(dp[i - 1][j], price[i] + dp[i - 1][j - wt[i]]);
            }
            else{
                //Add previously added item to knapsack
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
	

    cout << "Maximum Profit Earned: " << dp[items][capacity] << "\n";
    return 0;
}

/*
0/1 Knapsack :
Time Complexity: O(N*W). 
where ‘N’ is the number of weight element and ‘W’ is capacity. As for every weight element we traverse through all weight capacities 1<=w<=W.
Auxiliary Space: O(N*W). 
The use of 2-D array of size ‘N*W’.
*/


//code for dynamically accepting user input

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
    int capacity, items;

    // Accepting knapsack capacity and number of items
    cout << "Enter the knapsack capacity: ";
    cin >> capacity;

    cout << "Enter the number of items: ";
    cin >> items;

    vector<int> price(items + 1), wt(items + 1);

    // Accepting the price and weight of each item
    cout << "Enter the prices of the items:\n";
    for(int i = 1; i <= items; i++){
        cout << "Price of item " << i << ": ";
        cin >> price[i];
    }

    cout << "Enter the weights of the items:\n";
    for(int i = 1; i <= items; i++){
        cout << "Weight of item " << i << ": ";
        cin >> wt[i];
    }

    vector<vector<int>> dp(items + 1, vector<int>(capacity + 1, 0));

    // Dynamic programming to calculate the maximum profit
    for(int i = 1; i <= items; i++){
        for(int j = 1; j <= capacity; j++){
            if(wt[i] <= j){
                dp[i][j] = max(dp[i - 1][j], price[i] + dp[i - 1][j - wt[i]]);
            }
            else{
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    cout << "Maximum Profit Earned: " << dp[items][capacity] << "\n";
    return 0;
}
