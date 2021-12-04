from connect4 import models
from tests.acceptance import helper


def test_create_game():
    helper.initialize_game()


def test_vertical_win_1():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)

    assert state.active == False
    assert state.winner == models.Player.ONE


def test_vertical_win_2():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)

    assert state.active == False
    assert state.winner == models.Player.TWO


def test_horizontal_win_1():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 0)
    state = helper.make_move(game.gameId, game.playerOneId, 1)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 2)
    state = helper.make_move(game.gameId, game.playerOneId, 3)

    assert state.active == False
    assert state.winner == models.Player.ONE


def test_horizontal_win_2():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 0)
    state = helper.make_move(game.gameId, game.playerOneId, 1)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 3)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 2)

    assert state.active == False
    assert state.winner == models.Player.ONE


def test_diagonal_win_1():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 1)
    state = helper.make_move(game.gameId, game.playerTwoId, 2)
    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 4)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 3)

    assert state.active == False
    assert state.winner == models.Player.ONE


def test_diagonal_win_2():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 1)
    state = helper.make_move(game.gameId, game.playerTwoId, 2)
    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 4)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 4)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 3)
    state = helper.make_move(game.gameId, game.playerTwoId, 4)
    state = helper.make_move(game.gameId, game.playerOneId, 2)

    assert state.active == False
    assert state.winner == models.Player.ONE


def test_draw():
    game = helper.initialize_game()

    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 0)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 0)
    state = helper.make_move(game.gameId, game.playerOneId, 0)
    state = helper.make_move(game.gameId, game.playerTwoId, 0)

    state = helper.make_move(game.gameId, game.playerOneId, 1)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 1)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)
    state = helper.make_move(game.gameId, game.playerOneId, 1)
    state = helper.make_move(game.gameId, game.playerTwoId, 1)

    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 2)
    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 2)
    state = helper.make_move(game.gameId, game.playerOneId, 2)
    state = helper.make_move(game.gameId, game.playerTwoId, 2)

    state = helper.make_move(game.gameId, game.playerOneId, 4)

    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 3)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 3)
    state = helper.make_move(game.gameId, game.playerTwoId, 3)
    state = helper.make_move(game.gameId, game.playerOneId, 3)

    state = helper.make_move(game.gameId, game.playerTwoId, 4)
    state = helper.make_move(game.gameId, game.playerOneId, 4)
    state = helper.make_move(game.gameId, game.playerTwoId, 4)
    state = helper.make_move(game.gameId, game.playerOneId, 4)
    state = helper.make_move(game.gameId, game.playerTwoId, 4)

    state = helper.make_move(game.gameId, game.playerOneId, 5)
    state = helper.make_move(game.gameId, game.playerTwoId, 5)
    state = helper.make_move(game.gameId, game.playerOneId, 5)
    state = helper.make_move(game.gameId, game.playerTwoId, 5)
    state = helper.make_move(game.gameId, game.playerOneId, 5)
    state = helper.make_move(game.gameId, game.playerTwoId, 5)

    state = helper.make_move(game.gameId, game.playerOneId, 6)
    state = helper.make_move(game.gameId, game.playerTwoId, 6)
    state = helper.make_move(game.gameId, game.playerOneId, 6)
    state = helper.make_move(game.gameId, game.playerTwoId, 6)
    state = helper.make_move(game.gameId, game.playerOneId, 6)
    state = helper.make_move(game.gameId, game.playerTwoId, 6)

    assert state.active == False
    assert state.winner == None
