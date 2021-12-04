from connect4 import app_logic, models, database, exceptions
from unittest.mock import patch
from tests.unit import helper
import pytest


def test_index():
    message, code = app_logic.index()
    assert message == "Game Server"
    assert code == 200


def test_status():
    message, code = app_logic.status()
    assert message == "Running"
    assert code == 200


@patch("connect4.database.create_game")
@patch("connect4.database.add_player_to_game")
@patch("connect4.tokens.generate_token")
def test_create_game(mock_generate_token, mock_add_player_to_game, mock_create_game):
    mock_generate_token.side_effect = ["token1", "token2"]
    mock_create_game.return_value = None
    mock_add_player_to_game.return_value = None
    message, code = app_logic.create_game({})
    assert {
        "gameId": "token1",
        "active": True,
        "playerId": "token2",
        "winner": None,
        "playerNumber": models.Player.ONE,
        "activePlayer": models.Player.ONE,
        "playerCount": 1,
        "board": helper.get_empty_board(),
    } == message
    assert code == 201


@patch("connect4.database.get_game")
@patch("connect4.database.get_players")
@patch("connect4.tokens.generate_token")
@patch("connect4.database.add_player_to_game")
def test_join_game(
    mock_add_player_to_game, mock_generate_token, mock_get_players, mock_get_game
):
    mock_generate_token.return_value = "token1"
    mock_get_players.return_value = ["player1"]
    mock_add_player_to_game.return_value = None
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    req = {"gameId": "1"}
    message, code = app_logic.join_game(req)
    assert message["gameId"] == "1"
    assert message["active"] == True
    assert message["playerId"] == "token1"
    assert message["winner"] == None
    assert message["playerNumber"] == 2
    assert message["activePlayer"] == models.Player.ONE
    assert message["playerCount"] == 2
    assert message["board"] == helper.get_empty_board()
    assert code == 202


@patch("connect4.database.get_game")
def test_join_game_not_found(mock_get_game):
    mock_get_game.return_value = None
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.join_game({"gameId": "1"})
    assert "Game not found" in str(exc.value)


@patch("connect4.database.get_players")
@patch("connect4.database.get_game")
def test_join_game_full(mock_get_game, mock_get_players):
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_players.return_value = ["player1", "player2"]
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.join_game({"gameId": "1"})
    assert "Game is full" in str(exc.value)


@patch("connect4.database.get_players")
@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_get_game(mock_get_game, mock_get_player, mock_get_players):
    game_return = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_game.return_value = game_return
    mock_get_player.return_value = database.PlayerEntity(
        playerId="player1", gameId="1", number=1
    )
    mock_get_players.return_value = ["player1", "player2"]
    message, code = app_logic.get_game("1", "player1")

    assert message["gameId"] == "1"
    assert message["active"] == True
    assert message["playerId"] == "player1"
    assert message["winner"] == None
    assert message["playerNumber"] == models.Player.ONE
    assert message["activePlayer"] == models.Player.ONE
    assert message["playerCount"] == 2
    assert message["board"] == helper.get_empty_board()
    assert code == 200


@patch("connect4.database.get_game")
def test_get_game_not_found(mock_get_game):
    mock_get_game.return_value = None
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.get_game("1", "player1")
    assert "Game not found" in str(exc.value)


@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_get_game_player_not_found(mock_get_game, mock_get_player):
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_player.return_value = None
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.get_game("1", "player1")
    assert "Player not found" in str(exc.value)


@patch("connect4.database.update_game")
@patch("connect4.database.get_players")
@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_make_move(mock_get_game, mock_get_player, mock_get_players, mock_update_game):
    req = {"gameId": "1", "playerId": "player1", "column": 0}
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_player.return_value = database.PlayerEntity(
        playerId="player1", gameId="1", number=1
    )
    mock_get_players.return_value = ["player1", "player2"]
    mock_update_game.return_value = None

    message, code = app_logic.make_move(req)
    assert message["gameId"] == "1"
    assert message["active"] == True
    assert message["playerId"] == "player1"
    assert message["winner"] == None
    assert message["playerNumber"] == models.Player.ONE
    assert message["activePlayer"] == models.Player.TWO
    assert message["playerCount"] == 2
    assert message["board"] != helper.get_empty_board()
    assert message["board"][0][0] == models.Player.ONE
    assert code == 202


@patch("connect4.database.get_game")
def test_make_move_game_not_found(mock_get_game):
    req = {"gameId": "1", "playerId": "player1", "column": 0}
    mock_get_game.return_value = None
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.make_move(req)
    assert "Game not found" in str(exc.value)


@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_make_move_player_not_found(mock_get_game, mock_get_player):
    req = {"gameId": "1", "playerId": "player1", "column": 0}
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_player.return_value = None
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.make_move(req)
    assert "Player not found" in str(exc.value)


@patch("connect4.database.get_players")
@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_make_move_game_not_started(mock_get_game, mock_get_player, mock_get_players):
    req = {"gameId": "1", "playerId": "player1", "column": 0}
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_player.return_value = database.PlayerEntity(
        playerId="player1", gameId="1", number=1
    )
    mock_get_players.return_value = ["player1"]
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.make_move(req)
    assert "Game not started" in str(exc.value)


@patch("connect4.database.get_players")
@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_make_move_game_not_your_turn(mock_get_game, mock_get_player, mock_get_players):
    req = {"gameId": "1", "playerId": "player1", "column": 0}
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_player.return_value = database.PlayerEntity(
        playerId="player1", gameId="1", number=2
    )
    mock_get_players.return_value = ["player1", "player2"]
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.make_move(req)
    assert "Not your turn" in str(exc.value)


@patch("connect4.database.get_players")
@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_make_move_game_is_over(mock_get_game, mock_get_player, mock_get_players):
    req = {"gameId": "1", "playerId": "player1", "column": 0}
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=False,
        winner=None,
        activePlayer=1,
        board="100000"
        + "200000"
        + "100000"
        + "200000"
        + "100000"
        + "200000"
        + "100000",
    )
    mock_get_player.return_value = database.PlayerEntity(
        playerId="player1", gameId="1", number=1
    )
    mock_get_players.return_value = ["player1", "player2"]
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.make_move(req)
    assert "Game is over" in str(exc.value)


@patch("connect4.database.update_game")
@patch("connect4.database.get_players")
@patch("connect4.database.get_player")
@patch("connect4.database.get_game")
def test_make_move_game_column_full(
    mock_get_game, mock_get_player, mock_get_players, mock_update_game
):
    req = {"gameId": "1", "playerId": "player1", "column": 0}
    mock_get_game.return_value = database.GameEntity(
        gameId="1",
        active=True,
        winner=None,
        activePlayer=1,
        board="121212"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000"
        + "000000",
    )
    mock_get_player.return_value = database.PlayerEntity(
        playerId="player1", gameId="1", number=1
    )
    mock_get_players.return_value = ["player1", "player2"]
    mock_update_game.return_value = None
    with pytest.raises(exceptions.ApiException) as exc:
        app_logic.make_move(req)
    assert "Column is full" in str(exc.value)
