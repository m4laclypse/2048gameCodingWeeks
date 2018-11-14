from functools import reduce
from functools import partial

def is_grid_full(game_grid):
    for L in game_grid:
        for x in L:
            if x==' ':
                return False
    return True

def and_function(a,b) :
    return (a and b)

def not_void_tile(tile) :
    return tile != " "
    
def is_game_over(game_grid) :
    temp=[]
    for row in game_grid :
        temp.append(reduce(and_function,([not_void_tile(x) for x in row])))
    return reduce(and_function,temp)
    
def get_row_tile_max(row) :
    maxValue = 0
    for x in row :
        if x != " " :
            maxValue = max(maxValue,int(x))
    return maxValue
    
def get_grid_tile_max(game_grid) :
    maxValue = 0
    for row in game_grid :
        maxValue = max(maxValue, get_row_tile_max(row))
    return maxValue
    
def is_game_won(game_grid) :
    return get_grid_tile_max(game_grid) >= 2048
