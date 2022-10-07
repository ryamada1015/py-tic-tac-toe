"""game.py for holding information about the game"""

from inspect import formatargvalues
from re import X
import numpy as np


ROWS, COLS = 3, 3


class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.lock = False
        self.id = id
        self.board = np.zeros((ROWS, COLS))

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    # def winner(self, player):
    #     winner = -1
    #     if self.completed(self):
    #         if player == 0:
    #             winner = 0
    #         else:
    #             winner = 1
    #     return winner

    def cell_available(self, x, y):
        return self.board[x][y] == 0

    def board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return False
        return True

    def board_empty(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    return False
        return True

    def completed(self):
        # horizontal or vertical
        for i in range(3):
            if (
                self.board[i][0] == self.board[i][1] == self.board[i][2] != 0
                or self.board[0][i] == self.board[1][i] == self.board[2][i] != 0
            ):
                return True
        # diagnal
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] != 0
            or self.board[0][2] == self.board[1][1] == self.board[2][0] != 0
        ):
            return True
        return False

    def mark_cell(self, x, y, player):
        if self.cell_available(x, y):
            self.board[x][y] = player

    def switch_player(self, player):
        if player == 1:
            player = 2
            self.p1Went = True
            self.p2Went = False
        else:
            player = 1
            self.p2Went = True
            self.p1Went = False

    def play(self, player, pos):
        self.mark_cell(int(pos[0]), int(pos[1]), player)
        self.switch_player(player)

    def reset_game(self):
        self.board = np.zeros((ROWS, COLS))
        self.p1Went = False
        self.p2Went = False
