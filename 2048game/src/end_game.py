
def is_grid_full(game_grid):
    for L in game_grid:
        for x in L:
            if x==' ':
                return False
    return True

def is_game_over(game_grid) :
    tempBool = True
    for row in game_grid :
        tempBool = tempBool and not " " in row
    return tempBool
    
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
