from connect4 import game_logic
from connect4.models import Tile, Player
from tests.unit import helper
import pytest

# game_logic.make_move
def test_make_move_returns_new_object():
    game_input = helper.get_initial_game_state()

    game_output = game_logic.make_move(game_input, 0)

    assert game_input != game_output


def test_make_move_set_tile_one():
    game_input = helper.get_initial_game_state()

    game_output = game_logic.make_move(game_input, 0)

    assert Tile.ONE == game_output.board[0][0]


def test_make_move_set_tile_two():
    game_input = helper.get_initial_game_state()
    game_input.activePlayer = Player.TWO

    game_output = game_logic.make_move(game_input, 0)

    assert Tile.TWO == game_output.board[0][0]


def test_make_move_horizontal_win_one():
    game_input = helper.get_initial_game_state()
    game_input.board[0][0] = Tile.ONE
    game_input.board[1][0] = Tile.ONE
    game_input.board[2][0] = Tile.ONE

    game_output = game_logic.make_move(game_input, 3)

    assert False == game_output.active
    assert Player.ONE == game_output.winner


def test_make_move_horizontal_win_two():
    game_input = helper.get_initial_game_state()
    game_input.activePlayer = Player.TWO
    game_input.board[0][0] = Tile.TWO
    game_input.board[1][0] = Tile.TWO
    game_input.board[2][0] = Tile.TWO

    game_output = game_logic.make_move(game_input, 3)

    assert False == game_output.active
    assert Player.TWO == game_output.winner


def test_make_move_vertical_win_one():
    game_input = helper.get_initial_game_state()
    game_input.board[0][0] = Tile.ONE
    game_input.board[0][1] = Tile.ONE
    game_input.board[0][2] = Tile.ONE

    game_output = game_logic.make_move(game_input, 0)

    assert False == game_output.active
    assert Player.ONE == game_output.winner


def test_make_move_vertical_win_two():
    game_input = helper.get_initial_game_state()
    game_input.activePlayer = Player.TWO

    game_input.board[0][0] = Tile.TWO
    game_input.board[0][1] = Tile.TWO
    game_input.board[0][2] = Tile.TWO

    game_output = game_logic.make_move(game_input, 0)

    assert False == game_output.active
    assert Player.TWO == game_output.winner


def test_make_move_diagonal_win_one():
    game_input = helper.get_initial_game_state()

    game_input.board[0][0] = Tile.ONE

    game_input.board[1][0] = Tile.TWO
    game_input.board[1][1] = Tile.ONE

    game_input.board[2][0] = Tile.TWO
    game_input.board[2][1] = Tile.TWO
    game_input.board[2][2] = Tile.ONE

    game_input.board[3][0] = Tile.TWO
    game_input.board[3][1] = Tile.TWO
    game_input.board[3][2] = Tile.TWO

    game_output = game_logic.make_move(game_input, 3)

    assert False == game_output.active
    assert Player.ONE == game_output.winner


def test_make_move_diagonal_win_two():
    game_input = helper.get_initial_game_state()
    game_input.activePlayer = Player.TWO
    game_input.board[0][0] = Tile.ONE
    game_input.board[0][1] = Tile.ONE
    game_input.board[0][2] = Tile.ONE
    game_input.board[0][3] = Tile.TWO

    game_input.board[1][0] = Tile.ONE
    game_input.board[1][1] = Tile.ONE
    game_input.board[1][2] = Tile.TWO

    game_input.board[2][0] = Tile.ONE
    game_input.board[2][1] = Tile.TWO

    game_output = game_logic.make_move(game_input, 3)

    assert False == game_output.active
    assert Player.TWO == game_output.winner


def test_make_move_row_full_exception():
    game_input = helper.get_initial_game_state()
    game_input.board[0][0] = Tile.ONE
    game_input.board[0][1] = Tile.TWO
    game_input.board[0][2] = Tile.ONE
    game_input.board[0][3] = Tile.TWO
    game_input.board[0][4] = Tile.ONE
    game_input.board[0][5] = Tile.TWO

    with pytest.raises(Exception) as exc:
        game_output = game_logic.make_move(game_input, 0)
    assert "Row is full" in str(exc.value)


# game_logic.is_column_full
def test_is_column_full_empty():
    game_input = helper.get_initial_game_state()

    is_column_full = game_logic.is_column_full(game_input, 0)

    assert False == is_column_full


def test_is_column_full_full():
    game_input = helper.get_initial_game_state()
    for y in range(6):
        game_input.board[0][y] = Tile.ONE

    is_column_full = game_logic.is_column_full(game_input, 0)

    assert True == is_column_full


def test_is_board_full():
    game_input = helper.get_initial_game_state()
    columns = len(game_input.board)
    rows = len(game_input.board[0])

    for column in range(columns):
        for row in range(rows):
            game_input.board[column][row] = Tile.TWO
    print(game_input.board)
    is_board_full = game_logic.is_board_full(game_input)
    assert is_board_full == True


def test_get_tile():
    game_input = helper.get_initial_game_state()

    game_input.board[0][0] = Tile.ONE
    tile = game_logic.get_tile(game_input, 0, 0)

    assert tile == game_input.board[0][0]
