from textual_2048 import *
from pytest import *
import mock


def test_read_player_command(monkeypatch):

    
    monkeypatch.setattr('builtins.input', lambda x: "g")


    reponse = read_player_command()
    assert reponse == "g"