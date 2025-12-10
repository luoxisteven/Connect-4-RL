import os
import json

import Connect4 as c4
import Q_Table as Q_Table

class SARSA:
    def __init__(self):
        self.game = c4.Connect4()
        self.discount_factor = 0.9

        self.q_table_path = "metadata/q_table.json"
        self.q_table = self.load_q_table()
    
    def load_q_table(self):
        if os.path.exists(self.q_table_path):
            print("Loading Q-table from file...")
            with open(self.q_table_path, "r") as f:
                return json.load(f)
        else:
            print("No Q-table found, creating new one...")
            return {}

    def save_q_table(self):
        with open(self.q_table_path, "w") as f:
            json.dump(self.q_table, f)
