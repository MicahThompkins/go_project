import sys
import json
from streamy import stream
from board import get_board_length, make_empty_board, parse_point
from referee import referee

# configuration
config_file = open("go.config", "r")
info = list(stream(config_file.readlines()))[0]
default_player_file_path = info["default-player"]
player_pkg = __import__(default_player_file_path)
from player_pkg import proxy_remote_player, player
config_file.close()

default_player = player

maxIntersection = get_board_length()
empty = " "
black = "B"
white = "W"
n = 1
crazy = "GO has gone crazy!"
history = "This history makes no sense!"
bananas = "I am going bananas!"
empty_board = make_empty_board()
recv_size = 64


def read_input_from_file():
    file_contents = ""  # read in all json objects to a string
    file_contents_so_far = ""
    special_json = sys.stdin.readline()
    while special_json:
        file_contents += special_json
        special_json = sys.stdin.readline()
        decoded = ""
        # try to decode into json as we go
        # because if something later breaks the json formatting
        # we still want to be able to run all prior valid json
        try:
            decoded = list(stream(file_contents))
        except:
            continue
        if len(decoded) > 0:
            file_contents_so_far = list(stream(file_contents))
    try:
        return list(stream(file_contents))  # parse json objects
    except:
        if len(file_contents_so_far) > 0:
            return file_contents_so_far
        return [crazy]


class administrator:

    def __init__(self, player1, player2):
        self.player2 = player2
        self.player1 = player1
        self.referee = None
        self.client_done_flag = False

    # tuple of winner and whether the win was a result of cheating
    # (True means there was cheating, False means no cheating)
    def opposite_wins(self):
        return ([json.dumps(self.referee.get_opposite_player().name)], True)

    def check_input(self, input):
        if input == "pass":
            return True
        if crazy in input or history in input or bananas in input:
            return False
        try:
            parse_point(input)
        except:
            return False
        finally:
            return True

    # TODO add a while loop method that referees all moves until games over

    def referee_move(self, input):
        if self.referee.handle_move(input):
            return True
        return False

    def setup_game(self):
        self.referee = referee(self.player1, self.player2)
        self.register_receive_player(self.player1, black)
        self.register_receive_player(self.player2, white)


    def set_client_done_flag(self):
        self.client_done_flag = not self.client_done_flag

    def register_receive_player(self, p, stone):
        p.register()
        p.receive_stones(stone)

    def end_game_update_winner(self, original_winner, cheated):
        ok = "OK"
        original_winner_player = self.get_player_from_name(original_winner)
        original_loser_player = self.referee.get_opposite_player_from_name(original_winner)
        response1 = original_winner_player.end_game()
        original_loser_player.end_game()
        print(105)
        if not cheated and response1 != ok:
            return ([json.dumps(original_loser_player.name)], cheated)
        return ([json.dumps(original_winner_player.name)], cheated)

    def get_player_from_name(self, name):
        if name == self.player1.name:
            return self.player1
        if name == self.player2.name:
            return self.player2
        else:
            print(name, self.player1.name, self.player2.name)
            raise Exception("Invalid name given")

    def run_game(self):
        self.setup_game()
        while True:
            move = self.referee.current_player.make_a_move(self.referee.board_history)
            if isinstance(move, str):
                move = move.replace('"', '')
            print("admin @ 125", move)
            # if player didn't disconnect while making a move
            if move and self.check_input(move):
                not_over = self.referee.handle_move(move)
                print(128, not_over)
                # if the game didn't end, continue to next turn
                if not_over:
                    continue
                # game over, figure out the winner
                # alert players it's game over (check for disconnects)
                else:
                    original_winner, cheated = self.referee.get_winner()
                    # get the actual winner
                    print(137, original_winner)
                    return self.end_game_update_winner(original_winner[0], cheated)
            return self.opposite_wins()


if __name__ == '__main__':
    pass

