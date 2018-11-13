from game2048.textual_2048 import read_player_command
from pytest import *




def test_read_player_command(monkeypatch):

    results = "h"

    def mock_input_return(request):
        return results

    monkeypatch.setattr('builtins.input',mock_input_return)
    assert read_player_command() == results











