from connect4 import converter
from connect4.models import Player, Tile
from tests.unit import helper


class TestOptionalIntToPlayer:
    def test_none(self):
        assert converter.optional_int_to_player(None) == None

    def test_1(self):
        assert converter.optional_int_to_player(1) == Player.ONE

    def test_2(self):
        assert converter.optional_int_to_player(2) == Player.TWO


class TestOptionalPlayerToInt:
    def test_none(self):
        assert converter.optional_player_to_int(None) == None

    def test_1(self):
        assert converter.optional_player_to_int(Player.ONE) == 1

    def test_2(self):
        assert converter.optional_player_to_int(Player.TWO) == 2


class TestIntToPlayer:
    def test_1(self):
        assert converter.int_to_player(1) == Player.ONE

    def test_2(self):
        assert converter.int_to_player(2) == Player.TWO


class TestPlayerToInt:
    def test_1(self):
        assert converter.player_to_int(Player.ONE) == 1

    def test_2(self):
        assert converter.player_to_int(Player.TWO) == 2


class TestStrToBoard:
    def test_str_to_board_empty(self):
        empty_board = helper.get_empty_board()
        assert empty_board == converter.str_to_board(
            "000000" + "000000" + "000000" + "000000" + "000000" + "000000" + "000000"
        )

    def test_str_to_board_one_tile(self):
        board = helper.get_empty_board()
        board[1][0] = Tile.ONE
        assert board == converter.str_to_board(
            "000000" + "100000" + "000000" + "000000" + "000000" + "000000" + "000000"
        )


class TestIntToTile:
    def test_int_to_tile_empty(self):
        tile = converter.int_to_tile(0)

        assert tile == Tile.EMPTY

    def test_int_to_tile_one(self):
        tile = converter.int_to_tile(1)

        assert tile == Tile.ONE

    def test_int_to_tile_two(self):
        tile = converter.int_to_tile(2)

        assert tile == Tile.TWO


class TestPlayerToTile:
    def test_player_to_tile_one(self):
        tile = converter.player_to_tile(1)

        assert tile == Tile.ONE

    def test_player_to_tile_two(self):
        tile = converter.player_to_tile(2)

        assert tile == Tile.TWO


class TestTileToInt:
    def test_tile_to_int_zero(self):
        tile = converter.tile_to_int(Tile.EMPTY)

        assert tile == 0

    def test_tile_to_int_one(self):
        tile = converter.int_to_tile(Tile.ONE)

        assert tile == 1

    def test_tile_to_int_two(self):
        tile = converter.int_to_tile(Tile.TWO)

        assert tile == 2


class TestBoardToStr:
    board = helper.get_empty_board()
    board[0][0] = Tile.ONE
    board[0][1] = Tile.TWO
    str_board = converter.board_to_str(board)

    assert str_board[0] == "1"
    assert str_board[1] == "2"
    assert str_board[2] == "0"
