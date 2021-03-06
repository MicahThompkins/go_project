import sys
import json
from streamy import stream
from rule_checker import rule_checker, get_opponent_stone
from board import make_point, board, get_board_length, make_empty_board
from player_pkg.player_file import player
maxIntersection = get_board_length()
empty = " "
black = "B"
white = "W"
n = 1

empty_board = make_empty_board()


class referee:
    def __init__(self, player1, player2):
        self.player_count = 0
        self.player1 = player1
        self.player2 = player2
        if isinstance(player1, player) and isinstance(player2, player):
            self.player_count = 2
        self.pass_count = 0
        self.board_history = [empty_board]
        self.current_player = player1
        self.game_output = [black, white]

    def swap_player(self):
        self.current_player = self.get_opposite_player()

    def get_opposite_player(self):
        if self.current_player == self.player1:
            return self.player2
        else:
            return self.player1


    # returns true if game should continue, false if not
    def handle_move(self, input):
        self.game_output.append(self.board_history)
        if input == "pass":
            if self.pass_count == 1:
                self.game_output.append(self.get_winner())
                return False
            self.update_board_history(self.board_history[0])
            self.pass_count += 1
            self.swap_player()
            return True
        stone = self.current_player.stone
        move = [input, self.board_history]
        if rule_checker().check_validity(stone, move):
            new_board0 = board(self.board_history[0]).place(stone, input)
            new_board0 = board(new_board0).capture(get_opponent_stone(stone))
            self.update_board_history(new_board0)
            self.pass_count = 0
            self.swap_player()
            return True
        else:
            self.game_output.append(self.cheated())
            return False

    def update_board_history(self, new_board0):
        self.board_history = [new_board0] + self.board_history[:min(2, len(self.board_history))]

    # returns winner if someone current player cheated
    def cheated(self):
        self.swap_player()
        return [self.current_player.name]

    def get_winner(self):
        scores = board(self.board_history[0]).calculate_score()
        black_score = scores["B"] 
        white_score = scores["W"]
        # draw
        if black_score == white_score:
            return sorted([self.player1.name, self.player2.name])
        # player1 is always black
        if black_score > white_score:
            return [self.player1.name]
        return [self.player2.name]


def main():
    """
    Test Driver reads json objects from stdin
    Uses the streamy library to parse
    Queries player
    :return: list of json objects
    """
    file_contents = ""  # read in all json objects to a string
    special_json = sys.stdin.readline()
    while special_json:
        file_contents += special_json
        special_json = sys.stdin.readline()
    lst = list(stream(file_contents))  # parse json objects
    # assuming input is correctly formatting,
    # the second item in the second input obj should contain the stone
    player1 = player(black, lst[0])
    player2 = player(white, lst[1])
    ref = referee(player1, player2)
    for query in lst[2:]:
        result = ref.handle_move(query)
        if not result:
            break
    print(json.dumps(ref.game_output))


if __name__ == "__main__":
    main()
