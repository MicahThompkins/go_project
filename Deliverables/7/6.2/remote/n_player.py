import sys
import json
from streamy import stream
from rule_checker import rule_checker, get_opponent_stone
from board import make_point, board, get_board_length

maxIntersection = get_board_length()
empty = " "
black = "B"
white = "W"
n = 1
crazy = "GO has gone crazy!"

class n_player:
    def __init__(self, stone, name):
        self.stone = stone
        self.name = name
        self.register_flag = False
        self.receive_flag = False

    def query(self, query_lst):
        # get method and arguments from input query
        method = query_lst[0].replace("-", "_")
        args = query_lst[1:]
        method = getattr(self, method)
        if method:
            return method(*args)
        return crazy

    def register(self):
        if self.receive_flag or self.register_flag:
            return crazy
        self.register_flag = True
        return "no name"

    def receive_stones(self, stone):
        if not self.is_stone(stone):
            return crazy
        if self.receive_flag or not self.register_flag:
            return crazy
        self.receive_flag = True
        self.stone = stone
        return True

    def is_stone(self, stone):
        if stone == black or stone == white:
            return True
        return False

    def is_maybe_stone(self, maybe_stone):
        if self.is_stone(maybe_stone) or maybe_stone == empty:
            return True
        return False

    def check_boards_object(self, boards):
        min_boards_size = 1
        max_boards_size = 3
        # check to make sure input is actually a list
        if not isinstance(boards, list):
            return False
        # board history between length 1 and 3
        if len(boards) >= min_boards_size and len(boards) <= max_boards_size:
            return False
        for board in boards:
            if not self.check_board_object(board):
                return False
        return True

    def check_board_object(self, board):
        # check types
        if not isinstance(board, list):
            return False
        if not isinstance(board[0], list):
            return False
        # check dimensions
        if len(board) != maxIntersection or len(board[0]) != maxIntersection:
            return False
        # make sure all boards contain only maybe stones
        for i in range(maxIntersection):
            for j in range(maxIntersection):
                if not self.is_maybe_stone(board[i][j]):
                    return False
        return True




    def make_a_move_dumb(self, boards):
        # don't make a move until a player has been registered with a given stone
        if self.receive_flag and self.register_flag:
            if rule_checker().check_history(boards, self.stone):
                curr_board = boards[0]
                # go through rows and columns to find a point
                # check_validity of that move
                for i in range(maxIntersection):  # row
                    for j in range(maxIntersection):  # col
                        if curr_board[j][i] == empty:
                            point = make_point(i, j)
                            if rule_checker().check_validity(self.stone, [point, boards]):
                                return point
                return "pass"
            return "This history makes no sense!"
        return crazy

    def make_a_move(self, boards):
        # don't make a move until a player has been registered with a given stone
        if self.receive_flag and self.register_flag:
            if self.check_boards_object(boards):
                if rule_checker().check_history(boards, self.stone):
                    curr_board = boards[0]
                    non_capture_move = None
                    # go through rows and columns to find a point
                    # check_validity of that move
                    for i in range(maxIntersection):  # row
                        for j in range(maxIntersection):  # col
                            point = make_point(i, j)
                            if curr_board[j][i] == empty:
                                if rule_checker().check_validity(self.stone, [point, boards]):
                                    if self.make_capture_n_moves(n, curr_board, self.stone, point, boards):
                                        return point
                                    elif non_capture_move is None:
                                        non_capture_move = point
                    if non_capture_move:
                        return non_capture_move
                    return "pass"
                return "This history makes no sense!"
            return crazy
        return crazy

    def make_capture_n_moves(self, n, curr_board, stone, point, boards):
        if n == 1:
            return self.make_capture_1_move(curr_board, stone, point)
        new_boards = self.randomize_next_move(n, curr_board, stone, point, boards)
        updated_board = new_boards[0]
        for i in range(maxIntersection):
            for j in range(maxIntersection):
                new_point = make_point(i, j)
                if updated_board[j][i] == empty and rule_checker().check_validity(stone, [new_point, new_boards]):
                    if self.make_capture_1_move(updated_board, stone, new_point):
                        return True
        return False

    def randomize_next_move(self, n, curr_board, stone, point, boards):
        if n == 1:
            return boards
        curr_board = board(curr_board)
        updated_board = curr_board.place(stone, point)
        new_boards = [updated_board] + boards[:min(2, len(boards))]
        opponent_random_move = self.next_player_move(stone, new_boards)
        if opponent_random_move == "pass":
            new_boards = [new_boards[0]] + [new_boards[0]] + [new_boards[1]]
        else:
            new_boards = [board(new_boards[0]).place(get_opponent_stone(stone), opponent_random_move)] + \
                         [new_boards[0]] + [new_boards[1]]
        point = self.make_a_move_dumb(new_boards)
        return self.randomize_next_move(n - 1, new_boards[0], stone, point, new_boards)

    def next_player_move(self, stone, new_boards):
        next_player = n_player(get_opponent_stone(stone))
        next_player.register_flag = True
        next_player.receive_flag = True
        return next_player.make_a_move_dumb(new_boards)

    def make_capture_1_move(self, curr_board, stone, point):
        curr_board = board(curr_board)
        updated_board = curr_board.place(stone, point)
        stones_to_remove = board(updated_board).get_no_liberties(get_opponent_stone(stone))
        if len(stones_to_remove) > 0:
            return True
        return False


def main():
    """
    Test Driver reads json objects from stdin
    Uses the streamy library to parse
    Queries player
    :return: list of json objects
    """
    output = []
    file_contents = ""  # read in all json objects to a string
    special_json = sys.stdin.readline()
    while special_json:
        file_contents += special_json
        special_json = sys.stdin.readline()
    lst = list(stream(file_contents))  # parse json objects
    # assuming input is correctly formatting,
    # the second item in the second input obj should contain the stone
    stone = lst[1][1]
    curr_player = n_player(stone)
    for query in lst:
        result = curr_player.query(query)
        if result:
            output.append(result)
    print(json.dumps(output))


if __name__ == "__main__":
    main()