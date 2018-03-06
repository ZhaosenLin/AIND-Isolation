"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


def time_left():
    return 1000


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        # self.player1 = game_agent.MinimaxPlayer()
        self.player1 = game_agent.AlphaBetaPlayer()
        self.player2 = sample_players.RandomPlayer()
        self.game = isolation.Board(self.player1, self.player2)

    def test_min_max(self):
        min_max_player = self.player1
        random_palyer = self.player2
        move_list = []
        for move in range(20):
            my_move = min_max_player.get_move(self.game, time_left)
            print(my_move)
            move_list.append([my_move[0], my_move[1]])
            if my_move[0] == -1 and my_move[1] == -1:
                break
            self.game.apply_move(my_move)
            random_player_move = random_palyer.get_move(self.game, time_left)
            print(random_player_move)
            move_list.append([random_player_move[0], random_player_move[1]])
            if random_player_move[0] == -1 and random_player_move[1] == -1:
                break
            self.game.apply_move(random_player_move)
        print(move_list)
    def test_alpha_beta(self):
        alpha_beta_player = self.player1
        random_palyer = self.player2
        move_list = []
        for move in range(20):
            my_move = alpha_beta_player.get_move(self.game, time_left)
            print(my_move)
            move_list.append([my_move[0], my_move[1]])
            if my_move[0] == -1 and my_move[1] == -1:
                break
            self.game.apply_move(my_move)
            random_player_move = random_palyer.get_move(self.game, time_left)
            print(random_player_move)
            move_list.append([random_player_move[0], random_player_move[1]])
            if random_player_move[0] == -1 and random_player_move[1] == -1:
                break
            self.game.apply_move(random_player_move)
        print(move_list)


if __name__ == '__main__':
    unittest.main()
