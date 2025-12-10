import copy

class QTable:
    def __init__(self):
        self.q_table = dict()
    
    def get_q_table(self):
        return copy.deepcopy(self.q_table)

    def get_q_value(self, state):
        return self.q_table.get(state, 0)
    
    def set_q_table(self, q_table):
        self.q_table = copy.deepcopy(q_table)
    
    def update_q_table(self, state, value):
        self.q_table[state] = value
