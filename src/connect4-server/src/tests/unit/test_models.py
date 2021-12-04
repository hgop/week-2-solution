from connect4 import models
from tests.unit import helper


def test_player_model():
    player = models.Player(1)

    assert player == models.Player.ONE
    assert isinstance(player, models.Player) == True


def test_tile_model():
    tile = models.Tile(1)

    assert tile == models.Tile.ONE
    assert isinstance(tile, models.Tile) == True


def test_game_model():
    board = helper.get_empty_board()
    game = models.Game("1", True, None, models.Player.TWO, board)

    assert game.gameId == "1"
    assert game.active == True
    assert game.winner == None
    assert game.activePlayer == models.Player.TWO
    assert game.board[0][0] == models.Tile.EMPTY
    assert isinstance(game, models.Game) == True


def test_base_game_response_model():
    board = helper.get_empty_board()
    response = models.BaseGameResponse(
        "1", True, "testID", None, models.Player.ONE, models.Player.ONE, 2, board
    )

    assert response.gameId == "1"
    assert response.active == True
    assert response.playerId == "testID"
    assert response.winner == None
    assert response.playerNumber == models.Player.ONE
    assert response.activePlayer == models.Player.ONE
    assert response.board[0][0] == models.Tile.EMPTY
    assert isinstance(response, models.BaseGameResponse) == True

    response_dict = response.to_json()

    assert response_dict["gameId"] == "1"
    assert isinstance(response_dict, dict) == True


def test_create_game_response():
    board = helper.get_empty_board()
    response = models.CreateGameResponse(
        "1", True, "testID", None, models.Player.ONE, models.Player.ONE, 2, board
    )

    assert response.gameId == "1"
    assert response.active == True
    assert response.playerId == "testID"
    assert response.winner == None
    assert response.playerNumber == models.Player.ONE
    assert response.activePlayer == models.Player.ONE
    assert response.board[0][0] == models.Tile.EMPTY
    assert isinstance(response, models.BaseGameResponse) == True

    response_dict = response.to_json()

    assert response_dict["gameId"] == "1"
    assert isinstance(response_dict, dict) == True


def test_create_game_request():
    board = helper.get_empty_board()
    response = models.BaseGameResponse(
        "1", True, "testID", None, models.Player.ONE, models.Player.ONE, 2, board
    )
    response_dict = response.to_json()

    create_game_request = models.CreateGameRequest(response_dict)

    assert isinstance(create_game_request, models.CreateGameRequest)


def test_join_game_request():
    a_dict = {"test": "yes", "gameId": "1"}
    join_req = models.JoinGameRequest(a_dict)

    assert join_req.gameId == "1"
    assert isinstance(join_req, models.JoinGameRequest)


def test_join_game_response():
    board = helper.get_empty_board()
    response = models.JoinGameResponse(
        "1", True, "testID", None, models.Player.ONE, models.Player.ONE, 2, board
    )

    assert response.gameId == "1"
    assert response.active == True
    assert response.playerId == "testID"
    assert response.winner == None
    assert response.playerNumber == models.Player.ONE
    assert response.activePlayer == models.Player.ONE
    assert response.board[0][0] == models.Tile.EMPTY
    assert isinstance(response, models.JoinGameResponse) == True

    response_dict = response.to_json()

    assert response_dict["gameId"] == "1"
    assert isinstance(response_dict, dict) == True


def test_get_game_response():
    board = helper.get_empty_board()
    response = models.GetGameResponse(
        "1", True, "testID", None, models.Player.ONE, models.Player.ONE, 2, board
    )

    assert response.gameId == "1"
    assert response.active == True
    assert response.playerId == "testID"
    assert response.winner == None
    assert response.playerNumber == models.Player.ONE
    assert response.activePlayer == models.Player.ONE
    assert response.board[0][0] == models.Tile.EMPTY
    assert isinstance(response, models.GetGameResponse) == True

    response_dict = response.to_json()

    assert response_dict["gameId"] == "1"
    assert isinstance(response_dict, dict) == True


def test_make_move_request():
    a_dict = {"test": "yes", "gameId": "1", "playerId": "9999", "column": "2"}
    make_move = models.MakeMoveRequest(a_dict)

    assert make_move.gameId == "1"
    assert make_move.playerId == "9999"
    assert make_move.column == "2"
    assert isinstance(make_move, models.MakeMoveRequest)
