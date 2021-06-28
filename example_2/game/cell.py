class Cell:
    def __init__(self, state):
        self.state = state

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        if not state in [0, 1]:
            raise Exception("Invalid state")
        self._state = state
    
    def update_state(self, neighbors):
        if neighbors in [2, 3] and self.state == 1:
            self.state = 1
            return
        if neighbors == 3 and self.state == 0:
            self.state = 1
            return
        self.state = 0
