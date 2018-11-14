from pytest import *
from end_game import *


def test_is_grid_full():
    grille1=[['1','2','2'],['1','2','2'],['1','2','2']]
    grille2=[['1',' ','2'],['1','2','2'],['1','2','2']]
    assert (is_grid_full(grille1)==True)
    assert (is_grid_full(grille2)==False)
    