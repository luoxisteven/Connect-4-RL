import Connect4 as c4
import Connect_4_Q_Table as Q_Table

class SARSA:
    def __init__(self):
        self.game = c4.Connect4()
        self.q_table = {}
        self.discount_factor = 0.9