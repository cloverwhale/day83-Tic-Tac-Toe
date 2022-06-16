from player import Player
import random

winning_conditions = [{(0, 0), (0, 1), (0, 2)},
                      {(1, 0), (1, 1), (1, 2)},
                      {(2, 0), (2, 1), (2, 2)},
                      {(0, 0), (1, 0), (2, 0)},
                      {(0, 1), (1, 1), (2, 1)},
                      {(0, 2), (1, 2), (2, 2)},
                      {(0, 0), (1, 1), (2, 2)},
                      {(0, 2), (1, 1), (2, 0)}]


class Game:

    def __init__(self, boolean):
        self.grid_xy = [(0, 0), (0, 1), (0, 2),
                        (1, 0), (1, 1), (2, 2),
                        (2, 0), (2, 1), (1, 2)]

        self.player_first = boolean
        self.user = Player(self.player_first)
        self.pc = Player(not self.player_first)
        self.winner = None
        self.winning_items = []

    def pc_action(self):
        if self.pc.turn:
            host_picked = random.choice(self.grid_xy)
            self.pc.select(host_picked)
            self.grid_xy.remove(host_picked)
            return host_picked
        return None

    def check(self, player):
        if len(player.selected) >= 3:
            self.winning_items = self.compare(player.selected)
            if len(self.winning_items) > 0:
                self.winner = player
        return self.winning_items

    def compare(self, selected):
        for item in winning_conditions:
            if item <= selected:
                return item
        return []
