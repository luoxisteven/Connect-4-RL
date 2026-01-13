from Connect4 import *

class Game:
    def __init__(self):
        self.game = Connect4(None)
        self.player = ''
    
    def play(self):
        self.print_welcome_message()
        input = ""
        while input != "exit":
            self.game.reset_game()
            input = input("Type 'o' to play first and Type 'x' to play next: ")
            if input == 'o' or input == 'O':
                print("You choose start first. You will be player 'o'.")
                self.player = 'o'
                self.game.print_board()
            elif input == 'x' or input == 'X':
                print("You choose start next. You will be player 'x'.")
                self.player = 'x'
                self.game.take_random_action()
                self.game.print_board()
    
    def game_loop(self):
        input = ""
        while input != "exit":
            input = input("Please take an action: ")
            if input.isdigit():
                action = (self.player, int(input))
                if self.game.is_legal_action(action):
                    self.game.take_action(action)
                    if self.game.check_winner() == self.player:
                        print("You win!!")
                    else: 
                        self.game.take_random_action()
                        if self.game.check_winner() == self.player:
                            print("You lost!!")
                else:
                    print("This is not an illegal action, please choose the action again.")



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