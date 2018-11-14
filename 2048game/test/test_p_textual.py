from src.p_textual import *
from pytest import *
import mock


def test_read_player_command(monkeypatch):
    monkeypatch.setattr('__builtin__.input',lambda x: 'l')
    assert read_player_command() == 'l'

def test_menu(monkeypatch):
    monkeypatch.setattr('__builtin__.input',lambda x: '1')
    assert menu() == 1
    monkeypatch.setattr('__builtin__.input',lambda x: '4')
    assert menu() == 4
