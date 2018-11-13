from random import randint,random

probability = 0.5


def create_grid(taille):
    """
    Function that generate a grid of size: taille*taille
    The grid is empty (only ' ')
    """
    game_grid = []
    for i in range(0,taille):
        game_grid.append([' ' for j in range(taille)])
    return game_grid

def grid_initialiser(game_grid):
    """
    Function that take an empty grid and randomly add 2 elements in it and return the grid
    """
    game_grid=grid_add_random(game_grid)
    game_grid=grid_add_random(game_grid)
    return game_grid

def grid_add_random(game_grid):
    """
    Function that take a grid and add one element (a '2' of a '4' depending on the probability)
    Only in an empty tile 
    Return the grid
    
    """
    taille=len(game_grid)
    x=randint(0,taille-1)
    y=randint(0,taille-1)
    while game_grid[x][y]!=' ':
        x=randint(0,taille-1)
        y=randint(0,taille-1)
    if random()>probability:
        val="2"
    else:
        val='4'
    grid_add_new_tile_at_position(game_grid,x,y,val)
    return game_grid


def grid_add_new_tile_at_position(game_grid,x,y,val):
    game_grid[x][y]=val
    return game_grid


def grid_to_string(game_grid):
    """
    Function that take a grid and return a string element containing what to show to the people
    """
    taille=len(game_grid)
    al=" ".join(["===" for i in range(taille)])
    ligne=" "+al+"\n"
    
    def afficher_ligne(T):
        l=' | '.join(T)
        t='| '+l+' |\n'
        print(t)
        return t
    L=[afficher_ligne(T) for T in game_grid]
    
    txt=ligne.join(L)
    return ligne+txt+' '+al
    
    return txt
    