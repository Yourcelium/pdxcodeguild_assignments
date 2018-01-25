class TicTac:
    def __init__(self):
        self.board = [
                    [None, None, None], #self.board[y][x]
                    [None, None, None], #self.board[1]
                    [None, None, None], #self.board[2]
                    ]

    def place_token(self, x, y, token):
        row = int(y)
        columb = int(x)
        if self.board[row][columb] = None:
            self.board[row][columb] = token
        else:
            print('That space is taken try again')
            newx = input('Type X dimension: ')
            newy = input('Type Y dimension: ')
            self.place_token(newx, newy, token)

    def calc_winner(self):
        for i in self.board:
            if i[0] not None and i[0] == i[1] and i[0] == i[3]:
                print(f'{i[0]} is the wins')


