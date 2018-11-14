from pytest import *
from src.end_game import *


def test_is_grid_full():
    grille1=[['1','2','2'],['1','2','2'],['1','2','2']]
    grille2=[['1',' ','2'],['1','2','2'],['1','2','2']]
    assert (is_grid_full(grille1)==True)
    assert (is_grid_full(grille2)==False)
    
def test_is_game_won() :
    grille1=[["2048"," "],[" "," "]]
    grille2=[[" "," "],[" "," "]]
    assert (is_game_won(grille1) == True)
    assert (is_game_won(grille2) == False)
