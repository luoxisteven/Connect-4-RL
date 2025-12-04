class Connect4:
    def __init__(self):
        self.board = [["_" for _ in range(7)] for _ in range(6)]
        self.current_player = "x"
        self.game_over = False
        self.winner = None
        # self.action = (player, column_index)

    def get_current_state(self):
        return self.board
    
    def is_legal_action(self, action):
        if self.board[0][action[1]] != "_":
            return False
        return True

    def take_action(self, action):
        if not self.is_legal_action(action):
            return False
        else:
            for i in range(5,-1,-1):
                if self.board[i][action[1]] == "_":
                    self.board[i][action[1]] = action[0]
                    break
            return True

    def check_winner(self):
        return
    
    def reset_game(self):
        return
    
    def switch_player(self):
        return
    
    def get_reward(self):
        return

    def get_start_state(self):
        return
    
    def is_goal_state(self):
        return