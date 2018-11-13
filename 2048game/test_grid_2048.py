from grid_2048 import *
from pytest import *


def test_create_grid():
    assert create_grid(4) == [[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]

def test_grid_add_new_tile_at_position():
    game_grid=create_grid(4)
    game_grid=grid_add_new_tile_at_position(game_grid,1,1,'2')
    assert game_grid==[[' ',' ',' ', ' '],[' ', '2' ,' ', ' '],[' ',' ',' ', ' '],[' ',' ',' ', ' ']]
    
def test_grid_add_random():
    game_grid=create_grid(4)
    game_grid=grid_add_random(game_grid)
    game_grid=grid_add_random(game_grid)
    assert '2' or '4' in game_grid