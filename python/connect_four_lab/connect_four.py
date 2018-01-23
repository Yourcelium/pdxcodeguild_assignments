

class TicTac:
    def __init__(self):
        self.board = {1: [],
                      2: [],
                      3: [],
                      4: [],
                      5: [],
                      6: [],
                      7: []}

    def __str__(self):
        return '''
        1:{}
        2:{}
        3:{}
        4:{}
        5:{}
        6:{}
        7:{}
        
        '''.format(self.board[1], self.board[2], self.board[3], self.board[4], self.board[5], self.board[6],
                   self.board[7],)

    def __repr__(self):
        return self.__str__()

    def place_tile(self, column, player):
        self.board[column].append(player)

    def read_board(self, text):
        game = open(text, 'r')
        all_moves = game.read().splitlines()
        red_moves = all_moves[::2]
        yellow_moves = all_moves[1::2]
        print(all_moves)
        print('Red Moves: {}'.format(red_moves))
        print('Yellow Moves : {}'.format(yellow_moves))
        for i in red_moves:
            self.board[i].append('R')
        for i in yellow_moves:
            self.board[i].append('Y')

    # def get_winner(self):
    #     #horizontal
    #     for i in range(7):
    #         if self.board[i] == self.board[i+1] and self.board[i] == self.board[i+2] and self.board[i] == self.board[i+3]:
    #             print('Winner')
    #
    #     #vertical
    #     for i in range(7):
    #         if self.board[i][1] == self.board[i][2] and self.board[i][1] == self.board[i][3] and self.board[i][1] == self.board[i][4]:
    #             print('Winner')
    #         elif self.board[i][2] == self.board[i][3] and self.board[i][2] == self.board[i][4] and self.board[i][2] == self.board[i][5]:
    #             print('Winner')
    #         elif self.board[i][3] == self.board[i][4] and self.board[i][3] == self.board[i][5] and self.board[i][3] == self.board[i][6]:
    #             print('Winner')
    #         elif self.board[i][4] == self.board[i][5] and self.board[i][4] == self.board[i][6] and self.board[i][4] == self.board[i][7]:
    #             print('Winner')

    def game(self):
        while True:
            red_move = int(input('Red Player: Which Column would you like to place a tile: '))
            if len(self.board[red_move]) > 7:
                print('That Column is full please try another')
                red_move = int(input('Red Player: Which Column would you like to place a tile: '))
            self.place_tile(red_move, 'R')
            print('''
        1:{}
        2:{}
        3:{}
        4:{}
        5:{}
        6:{}
        7:{}
        
        '''.format(self.board[1], self.board[2], self.board[3], self.board[4], self.board[5],
                   self.board[6], self.board[7],))
            yellow_move = int(input('Yellow Player: Which Column would you like to place a tile: '))
            if len(self.board[red_move]) > 7:
                print('That Column is full please try another')
                yellow_move = int(input('Yellow Player: Which Column would you like to place a tile: '))
            self.place_tile(yellow_move, 'Y')
            print('''
        1:{}
        2:{}
        3:{}
        4:{}
        5:{}
        6:{}
        7:{}

        '''.format(self.board[1], self.board[2], self.board[3], self.board[4], self.board[5],
                   self.board[6], self.board[7], ))
            self.get_winner()



if __name__ == '__main__':
    TicTac().game()