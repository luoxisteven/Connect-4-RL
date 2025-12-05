import copy

class Connect4:
    def __init__(self, board):
        self.height = 6
        self.width = 7
        # Start from (0,0) the bottom left similar to regular (x,y) coordinates
        # a[x][y] = Location(x,y) start from the bottom left
        self.board = board or [["_" for _ in range(self.height)] for _ in range(self.width)]
        self.current_player = "x"
        self.players = ["x", "o"]
        self.game_over = False
        self.winner = None
        self.actions = []
        # self.action = (player, column_index)

    def is_legal_action(self, action, board=None):
        if self.game_over:
            return False
        if board is None:
            board = self.board
        action_col = action[1]
        if board[action_col][self.height-1] != "_" \
            or (not isinstance(action_col, int)) \
            or (action_col < 0) \
            or (action_col > self.width-1):
            return False
        return True
    
    def get_legal_actions(self, board=None):
        if board is None:
            board = self.board
        legal_actions = []
        for x in range(self.width):
            if board[x][self.height-1] == "_":
                legal_actions.append((self.current_player, x))
        return legal_actions

    def take_action(self, action):
        if not self.is_legal_action(action, self.board):
            return None
        else:
            for i in range(self.height):
                if self.board[action[1]][i] == "_":
                    self.board[action[1]][i] = action[0]
                    self.actions.append(action)
                    self.switch_player()
                    break
            return self.board

    def check_winner(self, board=None):
        if board is None:
            board = self.board
        
        # Vertical check
        for x in range(self.width):
            for y in range(self.height - 3):
                player = board[x][y]
                if player == "_":
                    break
                if player == board[x][y+1] == board[x][y+2] == board[x][y+3]:
                    return player  

        # Horizontal check
        for x in range(self.width - 3):
            for y in range(self.height):
                player = board[x][y]
                if player == "_":
                    break
                if player == board[x+1][y] == board[x+2][y] == board[x+3][y]:
                    return player

        # Diagonal down-right
        for x in range(self.width - 3):
            for y in range(self.height - 3):
                player = board[x][y]
                if player == "_":
                    break
                if player != "_" and player == board[x+1][y+1] == board[x+2][y+2] == board[x+3][y+3]:
                    return player

        # Diagonal up-right
        for x in range(3, self.width):
            for y in range(self.height - 3):
                player = board[x][y]
                if player == "_":
                    break
                if player != "_" and player == board[x-1][y+1] == board[x-2][y+2] == board[x-3][y+3]:
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

    def is_terminal(self, board=None):
        if board is None:
            board = self.board
        
        if self.check_winner(board) is not None:
            return True
        
        for x in range(self.width):
            if board[x][self.height-1] == "_":
                return False
        return True

    # RL-related methods
    def get_current_state(self):
        return self.board

    def take_search_action(self, action, state=None):
        if state is None:
            state = copy.deepcopy(self.board)
        else:
            state = copy.deepcopy(state)
        if not self.is_legal_action(action, state):
            return None
        else:
            for i in range(self.height):
                if state[action[1]][i] == "_":
                    state[action[1]][i] = action[0]
                    break
            return state

    def get_next_state(self, state, action):
        if state is None:
            state = self.board
        next_state = self.take_search_action(action, state)
        return next_state

    def is_goal_state(self, player, board=None):
        if board is None:
            board = self.board
        if self.check_winner(board) == player:
            return True
        return False

    def get_reward(self, action, state=None, next_state=None):
        if state is None:
            state = self.board
        if not self.is_legal_action(action, state):
            return -1
        if next_state is None:
            next_state = self.get_next_state(state, action)
        winner = self.check_winner(next_state)
        if winner == action[0]:
            return 1
        elif winner is None:
            return 0
        else:
            return -1
