class Player:

    def __init__(self, turn):
        self.selected = set()
        self.turn = turn
        self.win = False

    def select(self, item):
        if self.turn:
            self.selected.add(item)
            self.turn = False
