class Connect4:
    def __init__(self):
        self.board = [['' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 7)

    def make_move(self, column):
        if self.game_over:
            return
        if column < 0 or column >= 7:
            return
        for row in range(5, -1, -1):
            if self.board[row][column] == '':
                self.board[row][column] = self.current_player
                break
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.check_winner()

    def check_winner(self):
        return