'''This program will be able to solve easy sudoku puzzles.'''

rows, cols = 9, 9
sudoku = [[0 for i in range(rows)] for y in range(cols)]


def print_board(mat):
    '''
    This function will print the matrix 'mat' in the shape of a 
    sudoku board.
    '''
    for i in range(9):
        for j in range(9):
            if(j in [2, 5, 8]):
                print(mat[i][j], end="|")
            else:
                print(mat[i][j], end=" ")
        if(i in [2, 5]):
            print()
            print("- - - - - - - - -")
        else:
            print()
    
print_board(sudoku)

def create_puzzle(mat):
    pass