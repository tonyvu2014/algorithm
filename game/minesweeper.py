class MineSweeper:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.board = [[0 for j in range(column)] for i in range(row)]
        self.board_state = [['_' for j in range(column)] for i in range(row)]
        self.hidden_count = row*column
        self.mine_count = 0

    def set_mine_locations(self, mine_locations):
        for x, y in mine_locations:
            for i in range(-1, 2):
                if i+x < 0 or i+x >= self.row:
                    continue
                for j in range(-1, 2):
                    if j+y < 0 or j+y >= self.column:
                        continue
                    self.board[x+i][y+j] += 1
            self.board[x][y] = 9
            self.mine_count += 1
    
    def reset(self):
        self.board_state = [['_' for j in range(self.column)] for i in range(self.row)]
        self.hidden_count = self.row*self..column

    def reveal_cell(self, x, y):
        if self.board[x][y] == 9: # detect a mine
            self.board_state = [[self.board[i][j] for j in range(self.column)] for i in range(self.row)]
            self.hidden_count = 0
            return False
        
        if self.board_state[x][y] == '_':
            self.board_state[x][y] = self.board[x][y]
            self.hidden_count -= 1
        
        return True

    def is_completed(self):
        return self.hidden_count <= self.mine_count
    
    def print_state(self):
        for i in range(self.row):
            print(' '.join([str(self.board_state[i][j]) for j in range(self.column)]))

    def print_board(self):
        for i in range(self.row):
            print(' '.join([str(self.board[i][j]) for j in range(self.column)]))
        
def play(mine_sweeper):
    while True:
        cell = input('Type your selected cell in this format x y or -1 to exit: ')
        location = cell.split()
        if len(location) < 2:
            if location[0] == '-1':
                print('You quit the game.')
                break
            else:
                print('Invalid input')
                continue
        try:
            x = int(location[0]) - 1
            y = int(location[1]) - 1
            if x < 0 or x > mine_sweeper.row-1:
                print('Invalid input')
                continue
            if y < 0 or y > mine_sweeper.column-1:
                print('Invalid input')
                continue
            print('You played: (' + location[0] + ', ' + location[1] + ')' )
            status = mine_sweeper.reveal_cell(x, y)
            if not status:
                print('You lost')
                break
            elif mine_sweeper.is_completed():
                print('You won')
                break
            mine_sweeper.print_state()
        except ValueError:
            print('Invalid input')

if __name__ == '__main__':
    game = MineSweeper(4, 4)
    game.set_mine_locations([(1, 1), (2, 3), (3, 0)])
    game.print_board()
    game.print_state()
    play(game)





