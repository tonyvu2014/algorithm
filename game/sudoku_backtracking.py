N = 9

class SudokuBoard:
    def __init__(self, grid):
        self.grid = grid

    def set_cell(self, i, j, value):
        self.grid[i][j] = value

    def reset_cell(self, i, j):
        self.grid[i][j] = 0

    def is_cell_value_valid(self, i, j, value):
        # Check values in this row are unique
        for col in range(9):
            if self.grid[i][col] == value:
                return False

        # Check values in this column are unique
        for row in range(9):
            if self.grid[row][j] == value:
                return False

        # Check values in the 3x3 square are unique
        startRow = row - row % 3
        startCol = col - col % 3
        for row in range(3):
            for col in range(3):
                if self.grid[row + startRow][col + startCol] == value:
                    return False

        return True

    def solve(self, i, j):
        if (i == N-1 and j == N):
            return True

        if j == N:
            i += 1
            j = 0
       
        if self.grid[i][j] > 0:
            return self.solve(i, j+1)

        for value in range(1, N+1, 1):
            if self.is_cell_value_valid(i, j, value):
                self.grid[i][j] = value
                if self.solve(i, j+1):
                    return True
            self.grid[i][j] = 0

        return False

    def display(self):
        for i in range(N):
            for j in range(N):
                print(self.grid[i][j], end = " ")
            print()
	

if __name__ == '__main__':
    grid = [
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0]
    ]
    sudokuBoard = SudokuBoard(grid)
    if sudokuBoard.solve(0, 0):
        sudokuBoard.display()
    else:
        print('No solution')
        sudokuBoard.display()

                      
				


		

		
                       
		
                                                            





 
                        
