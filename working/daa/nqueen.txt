def is_safe(board, x, y, n):
    # Check column
    for row in range(x):
        if board[row][y] == 1:
            return False

    # Check upper-left diagonal
    row, col = x, y
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # Check upper-right diagonal
    row, col = x, y
    while row >= 0 and col < n:
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print("Q " if board[i][j] == 1 else "_ ", end="")
        print()
    print("\n")

def n_queen(board, x, n):
    if x == n:
        print_board(board, n)
        return

    for col in range(n):
        if is_safe(board, x, col, n):
            board[x][col] = 1
            n_queen(board, x + 1, n)
            board[x][col] = 0  # Backtrack

def main():
    # Input size of board
    n = int(input("Enter the size of the board (n): "))
    
    # Initialize board
    board = [[0] * n for _ in range(n)]
    
    # Ask for the position of the first queen
    first_queen_row = int(input("Enter the row for the first queen (0-based indexing): "))
    first_queen_col = int(input("Enter the column for the first queen (0-based indexing): "))

    # Validate input position
    if not (0 <= first_queen_row < n and 0 <= first_queen_col < n):
        print(f"Invalid position! The row and column must be between 0 and {n-1}.")
        return

    # Place the first queen
    board[first_queen_row][first_queen_col] = 1

    print("--------All possible solutions--------")
    # Call nQueen function starting from the next row
    n_queen(board, first_queen_row + 1, n)

main()


#OUTPUT:

#Enter the size of the board (n): 4
#Enter the row for the first queen (0-based indexing): 0
#Enter the column for the first queen (0-based indexing): 1
#--------All possible solutions--------
#_ Q _ _ 
#_ _ _ Q 
#Q _ _ _ 
#_ _ Q _ 

