# You are given a maze in the form of a matrix of size n * m. Each cell is either clear or blocked denoted by 1 and 0 respectively.
# A rat sits at the top-left cell and there exists a block of cheese at the bottom-right cell. Both these cells are guaranteed to be clear.
# You need to find if the rat can get the cheese if it can move only in one of the two directions - down and right. It can’t move to blocked cells.


# Backtracking algorithm, check if we can get to the cheese from the 
# cell on the right or from the cell at the bottom
# if yes, then return True, else return False
class Solution:
    def __init_(self):
        print('Start a solution')

    def canGetCheeseFrom(self, maze, x, y):
        n = len(maze)
        m = len(maze[0])

        if x == n - 1 and y == m - 1:
            return True
        
        if x+1 < n and maze[x+1][y] == 1:
            if self.canGetCheeseFrom(maze, x+1, y):
                return True
        
        if y+1 < m and maze[x][y+1] == 1:
            if self.canGetCheeseFrom(maze, x, y+1):
                return True

        return False 

    def canGetCheese(self, maze):
        return self.canGetCheeseFrom(maze, 0, 0)
    
if __name__ == '__main__':
    maze = [[1, 1, 0, 0], [1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 0, 1]]
    solution = Solution()
    print(solution.canGetCheese(maze))
