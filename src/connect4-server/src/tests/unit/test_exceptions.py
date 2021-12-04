from connect4 import exceptions


def test_api_exception():
    new_exception = exceptions.ApiException("Game is full", 404)

    assert new_exception.message == "Game is full"
    assert new_exception.status_code == 404
