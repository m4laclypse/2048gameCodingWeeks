from Ptextual_2048 import *
from pytest import *
import mock


def test_read_player_command(monkeypatch):
    monkeypatch.setattr('__builtin__.input',lambda x: 'l')
    assert read_player_command() == 'l'