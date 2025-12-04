class Connect4:
    def __init__(self, board):
        self.height = 6
        self.width = 7
        # Start from (0,0) the bottom left similar to regular (x,y) coordinates
        # a[x][y] = Location(x,y) start from the bottom left
        self.board = board or [["_" for _ in range(self.height)] for _ in range(self.width)]
        self.current_player = "x"
        self.game_over = False
        self.winner = None
        # self.action = (player, column_index)
    
    def is_legal_action(self, action, state=None):
        if state is None:
            state = self.board
        if self.game_over:
            return False
        action_player = action[0]
        action_col = action[1]
        if action_player != self.current_player:
            return False
        if state[action_col][self.height-1] != "_" \
            or (not isinstance(action_col, int)) \
            or (action_col < 0) \
            or (action_col > self.width-1):
            return False
        return True

    def take_action(self, action, state=None):
        if state is None:
            state = self.board
        else:
            self.board = state
        if not self.is_legal_action(action, state):
            return None
        else:
            for i in range(self.height):
                if state[action[1]][i] == "_":
                    state[action[1]][i] = action[0]
                    self.board = state
                    self.switch_player()
                    break
            return self.board

    def take_search_action(self, action, state=None):
        if state is None:
            state = self.board
        if not self.is_legal_action(action, state):
            return None
        else:
            for i in range(self.height):
                if state[action[1]][i] == "_":
                    state[action[1]][i] = action[0]
                    break
            return state

    def check_winner(self, board=None):
        if board is None:
            board = self.board
        else:
            self.board = board
        # Vertical check
        for x in range(self.width):
            for y in range(self.height - 3):
                player = board[x][y]
                if player == "_":
                    break
                if player == board[x][y+1] == board[x][y+2] == board[x][y+3]:
                    self.game_over = True
                    self.winner = player
                    return player  

        # Horizontal check
        for x in range(self.width - 3):
            for y in range(self.height):
                player = board[x][y]
                if player == "_":
                    break
                if player == board[x+1][y] == board[x+2][y] == board[x+3][y]:
                    self.game_over = True
                    self.winner = player
                    return player

        # Diagonal down-right
        for x in range(self.width - 3):
            for y in range(self.height - 3):
                player = board[x][y]
                if player == "_":
                    break
                if player != "_" and player == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]:
                    self.game_over = True
                    self.winner = player
                    return player

        # Diagonal up-right
        for x in range(3, self.width):
            for y in range(self.height - 3):
                player = board[x][y]
                if player == "_":
                    break
                if player != "_" and player == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3]:
                    self.game_over = True
                    self.winner = player
                    return player

        return None
    
    def reset_game(self):
        self.board = [["_" for _ in range(self.height)] for _ in range(self.width)]
        return self.board
    
    def switch_player(self):
        self.current_player = "o" if self.current_player == "x" else "x"
        return self.current_player
    
    def print_board(self):
        for y in reversed(range(self.height)):
            row = []
            for x in range(self.width):
                row.append(self.board[x][y])
            print(" ".join(row))

    # RL-related methods
    def get_current_state(self):
        return self.board

    def get_next_state(self, state, action):
        if state is None:
            state = self.board
        next_state = self.take_search_action(action, state)
        return next_state

    def is_goal_state(self, board=None):
        if board is None:
            board = self.board
        if self.check_winner(board) is not None:
            return True
        return False

    def get_reward(self, action, state=None, next_state=None):
        if state is None:
            state = self.board
        if next_state is None:
            next_state = self.get_next_state(state, action)
        if self.is_goal_state(next_state):
            if self.winner == self.current_player:
                return 1
        return 0
