from Mmove_2048 import *

def test_move_row_left():
    assert move_row_left([" ", " ", " ", "2"]) == ["2", " ", " ", " "]
    assert move_row_left([" ", "2", " ", "4"]) == ["2", "4", " ", " "]
    assert move_row_left(["2", "2", " ", "4"]) == ["4", "4", " ", " "]
    assert move_row_left(["2", "2", "2", "2"]) == ["4", "4", " ", " "]
    assert move_row_left(["4", "2", " ", "2"]) == ["4", "4", " ", " "]
    assert move_row_left(["2", " ", " ", "2"]) == ["4", " ", " ", " "]
    assert move_row_left(["2", "4", "2", "2"]) == ["2", "4", "4", " "]
    assert move_row_left(["2", "4", "4", " "]) == ["2", "8", " ", " "]
    assert move_row_left(["4", "8", "16", "32"]) == ["4", "8", "16", "32"]

def test_move_row_right():
    assert move_row_right(["2", " ", " ", " "]) == [" ", " ", " ", "2"]
    assert move_row_right([" ", "2", " ", "4"]) == [" ", " ", "2", "4"]
    assert move_row_right(["2", "2", " ", "4"]) == [" ", " ", "4", "4"]
    assert move_row_right(["2", "2", "2", "2"]) == [" ", " ", "4", "4"]
    assert move_row_right(["4", "2", " ", "2"]) == [" ", " ", "4", "4"]
    assert move_row_right(["2", " ", " ", "2"]) == [" ", " ", " ", "4"]
    assert move_row_right(["2", "4", "2", "2"]) == [" ", "2", "4", "4"]
    assert move_row_right(["2", "4", "4", " "]) == [" ", " ", "2", "8"]
    assert move_row_right(["4", "8", "16", "32"]) == ["4", "8", "16", "32"]