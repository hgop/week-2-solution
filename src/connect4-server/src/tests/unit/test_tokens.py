from connect4 import tokens


def test_generate_token():
    token = tokens.generate_token(20)

    assert len(token) == 20
