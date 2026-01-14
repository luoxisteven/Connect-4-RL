from Connect4 import *

class Game:
    def __init__(self):
        self.game = Connect4(None)
        self.player = ''
    
    def play(self):
        self.print_welcome_message()
        user_input = ""
        while user_input != "exit":
            self.game.reset_game()
            user_input = input("Type 'o' to play first and Type 'x' to play next: ")
            if user_input == 'o' or user_input == 'O':
                print("You choose start first. You will be player 'o'.")
                self.player = 'o'
                self.game.print_board()
                user_input = self.game_loop()
            elif user_input == 'x' or user_input == 'X':
                print("You choose start next. You will be player 'x'.")
                self.player = 'x'
                self.game.take_random_action()
                self.game.print_board()
                user_input = self.game_loop()
    
    def game_loop(self):
        user_input = ""
        while user_input != "exit":
            user_input = input("Please take an action: ")
            if user_input.isdigit():
                action = (self.player, int(user_input))
                if self.game.is_legal_action(action):
                    self.game.take_action(action)
                    if self.check_winner() != None:
                        break
                    self.game.take_random_action()
                    self.game.print_board()
                    if self.check_winner() != None:
                        break
                else:
                    print("This is not an illegal action, please choose the action again.")
        return user_input
    
    def check_winner(self):
        if self.game.check_winner() == self.player:
            self.game.print_board()
            print("You win!!")
            return self.player
        elif self.game.check_winner() == None:
            return None
        else:
            print("You lost!!")
            return "o" if self.player == "o" else "x"

    def print_welcome_message(self):
        message = """
        ============================================================
                        Welcome to CONNECT 4!
        ============================================================

        GAME RULES:
        ------------------------------------------------------------
        • Drop pieces into columns (0-6) to stack them
        • Get 4 of your pieces in a row to win!
        • You can win horizontally, vertically, or diagonally
        • First player to get 4 in a row wins the game

        PLAYERS:
        ------------------------------------------------------------
        • O - Plays first
        • X - Plays second

        HOW TO PLAY:
        ------------------------------------------------------------
        • Enter a column number (0-6) to drop your piece
        • Pieces fall to the lowest available position
        • Watch out - you can block your opponent too!
        • You can enter "exit" to exit the game at any time

        ============================================================
                        Good luck! Let's begin...
        ============================================================
        """
        print(message)

if __name__ == "__main__":
    game = Game()
    game.play()