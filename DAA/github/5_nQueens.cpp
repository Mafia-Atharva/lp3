#include<bits/stdc++.h>
using namespace std;

bool isSafe(int **arr, int x, int y, int n){
    for(int row=0;row<x;row++){
        if(arr[row][y]==1){
            return false;
        }
    }

    int row =x;
    int col =y;
    while(row>=0 && col>=0){
        if(arr[row][col]==1){
            return false;
        }
        row--;
        col--;
    }

    row =x;
    col =y;
    while(row>=0 && col<n){
        if(arr[row][col]==1){
            return false;
        }
        row--;
        col++;
    }

    return true;
}

void printBoard(int **arr, int n){
	for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
			if(arr[i][j] == 1) cout << "[Q]";
			else cout << "[]";
		}
        cout << endl;
	}
	cout << endl;
	cout << endl;
}


void nQueen(int** arr, int x, int n){
    if(x == n){
        printBoard(arr, n);
		return;
    }

    for(int col=0;col<n;col++){
        if(isSafe(arr,x,col,n)){
            arr[x][col]=1;
            nQueen(arr,x+1,n);
            arr[x][col]=0;
        }
    }
}


int main(){
    int n;
    cin >> n;
    
    int **arr = new int*[n];    
    for(int i=0;i<n;i++){
        arr[i] = new int[n];
        for(int j=0;j<n;j++){
            arr[i][j]=0;
        }
    }
	
	nQueen(arr, 0, n);
	
	cout << "--------All possible solutions--------";
	
    return 0;
}

/*
Time Complexity: O(N!)
Auxiliary Space: O(N^2)
*/


//chatgpt code for dynamic input

#include<bits/stdc++.h>
using namespace std;

bool isSafe(int **arr, int x, int y, int n){
    // Check column
    for(int row = 0; row < x; row++){
        if(arr[row][y] == 1){
            return false;
        }
    }

    // Check upper-left diagonal
    int row = x, col = y;
    while(row >= 0 && col >= 0){
        if(arr[row][col] == 1){
            return false;
        }
        row--;
        col--;
    }

    // Check upper-right diagonal
    row = x, col = y;
    while(row >= 0 && col < n){
        if(arr[row][col] == 1){
            return false;
        }
        row--;
        col++;
    }

    return true;
}

void printBoard(int **arr, int n){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(arr[i][j] == 1) cout << "Q ";
            else cout << "_ ";
        }
        cout << endl;
    }
    cout << endl;
    cout << endl;
}

void nQueen(int **arr, int x, int n){
    if(x == n){
        printBoard(arr, n);
        return;
    }

    for(int col = 0; col < n; col++){
        if(isSafe(arr, x, col, n)){
            arr[x][col] = 1;
            nQueen(arr, x + 1, n);
            arr[x][col] = 0;
        }
    }
}

int main(){
    int n;
    cout << "Enter the size of the board (n): ";
    cin >> n;
    
    int **arr = new int*[n];    
    for(int i = 0; i < n; i++){
        arr[i] = new int[n];
        for(int j = 0; j < n; j++){
            arr[i][j] = 0;
        }
    }

    // Ask the user to input the position for the first queen
    int firstQueenRow, firstQueenCol;
    cout << "Enter the row and column for the first queen (0-based indexing): ";
    cin >> firstQueenRow >> firstQueenCol;

    // Check if the input is within bounds
    if(firstQueenRow < 0 || firstQueenRow >= n || firstQueenCol < 0 || firstQueenCol >= n){
        cout << "Invalid position! The row and column must be between 0 and " << n-1 << "." << endl;
        return 1;
    }

    // Place the first queen
    arr[firstQueenRow][firstQueenCol] = 1;

    // Call nQueen function starting from row 1 (since the first queen is placed)
    nQueen(arr, 1, n);
    
    cout << "--------All possible solutions--------";
    
    return 0;
}
