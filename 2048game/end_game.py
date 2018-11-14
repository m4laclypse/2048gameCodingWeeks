
def is_grid_full(game_grid):
    for L in game_grid:
        for x in L:
            if x==' ':
                return False
    return True
