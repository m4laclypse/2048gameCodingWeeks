from grid_2048 import *
from pytest import *


def test_create_grid():
    assert create_grid(4) == [[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]

   
def test_grid_add_new_tile():
    game_grid=create_grid(4)
    game_grid=grid_add_new_tile(game_grid)
    game_grid=grid_add_new_tile(game_grid)
    assert '2' or '4' in game_grid
    
    
    
def test_grid_to_string():
    a =""" === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
|   |   |   |   |
 === === === ===
| 2 |   |   | 2 |
 === === === ==="""
    aa=grid_to_string([[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], ['2', ' ', ' ', '2']])

    assert aa==a
    b=""" === === ===
|   |   |   |
 === === ===
|   |   |   |
 === === ===
| 2 |   | 2 |
 === === ==="""
    bb=grid_to_string([[' ', ' ', ' '], [' ', ' ', ' '], ['2', ' ', '2']])
    
    
    assert bb==b