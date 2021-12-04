import pytest


@pytest.mark.timeout(30)
def test_sequential():
    from tests.acceptance.test_game import test_vertical_win_1

    for _ in range(10):
        test_vertical_win_1()
