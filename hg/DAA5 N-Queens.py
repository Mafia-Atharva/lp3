def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")


def is_safe(board, row, col, n):
    # Check this column on upper side
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check upper diagonal on right side
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # Base case: If all queens are placed
    if row >= n:
        return True
    
    # Try placing a queen in each column in the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen

            # Recur to place the rest of the queens
            if solve_n_queens(board, row + 1, n):
                return True
            
            # If placing queen in board[row][col] doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False


# Main function to initialize the board and get user input
def main():
    # Get board size from the user
    n = int(input("Enter the size of the board (n x n): "))

    # Initialize an empty n x n board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Get the position for the first queen
    row = int(input("Enter the row index for the first queen (0-based): "))
    col = int(input("Enter the column index for the first queen (0-based): "))

    # Check if the position is valid
    if 0 <= row < n and 0 <= col < n:
        # Place the first queen on the board
        board[row][col] = 1
        print("Board after placing the first queen:")
        print_board(board)
        
        # Solve the rest of the board starting from the next row
        if solve_n_queens(board, row + 1, n):
            print("Solution found:")
            print_board(board)
        else:
            print("No solution exists.")
    else:
        print("Invalid position for the first queen.")

# Run the main function
main()


"""
Key Functions and Logic
print_board function:

Prints the board's current state, showing queens (Q) and empty cells (.).
Takes board as input, which is an N x N grid where 1 represents a queen, and 0 represents an empty cell.
is_safe function:

Checks if placing a queen at position (row, col) is safe, meaning it won’t be attacked by any other queen.
Safety Checks:
Column Check: Ensures no queen exists in the current column above the row.
Left Diagonal Check: Ensures no queen exists on the left diagonal from (row, col) going up-left.
Right Diagonal Check: Ensures no queen exists on the right diagonal from (row, col) going up-right.
If all checks pass, it returns True, indicating it’s safe to place a queen at (row, col).
solve_n_queens function:

Recursively tries to place queens on the board, row by row.
Base Case: If all queens are successfully placed (row >= n), it returns True.
Recursive Case:
For each column in the current row, it checks if placing a queen is safe.
If safe, places the queen (board[row][col] = 1) and recursively attempts to place the next queen.
If successful, it returns True.
If not, it backtracks by removing the queen (board[row][col] = 0) and tries the next column.
Returns False if no solution is found for the current configuration.
main function:

Initializes the chessboard and prompts the user to enter:
The board size n (for an n x n board).
The starting position (row, col) of the first queen.
Places the first queen at the user-specified position, checks if it's valid, and displays the initial board.
Calls solve_n_queens starting from the next row to solve the rest of the board.
If a solution is found, it displays the final board; otherwise, it indicates that no solution exists.
"""