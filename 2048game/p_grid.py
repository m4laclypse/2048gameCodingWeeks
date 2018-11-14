from random import randint,random

probability = 0.5

THEMES = {"0": {"name": "Default", 0: " ", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: " ", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: " ", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

def create_grid(taille):
    """
    Function that generate a grid of size: taille*taille
    The grid is empty (only ' ')
    """
    game_grid = []
    for i in range(0,taille):
        game_grid.append([' ' for j in range(taille)])
    return game_grid

def grid_initialiser(taille):
    """
    Function that take an empty grid and randomly add 2 elements in it and return the grid
    """
    game_grid=create_grid(taille)
    game_grid=grid_add_new_tile(game_grid)
    game_grid=grid_add_new_tile(game_grid)
    return game_grid
def grid_get_all_tiles(game_grid):
    L=[]
    for T in game_grid:
        L.extend(T)
    return L

def grid_add_new_tile(game_grid,themeIndex=0):
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
        val=THEMES['0'][2]
    else:
        val=THEMES['0'][2]
    game_grid[x][y]=val
    return game_grid



def grid_to_string(game_grid):
    """
    Function that take a grid and return a string element containing what to show to the people
    """
    taille=len(game_grid)
    al=" ".join(["===" for i in range(taille)])
    ligne=" "+al+"\n"
    LIST=grid_get_all_tiles(game_grid)
    max=0
    for x in LIST:
        if len(x)>max:
            max=len(x)
    def afficher_ligne(T):
        TT=T[:]
        for t in TT:
            t.ljust(max)
        l=' | '.join(TT)
        t='| '+l+' |\n'
        print(t)
        return t
    L=[afficher_ligne(T) for T in game_grid]
    
    txt=ligne.join(L)
    return ligne+txt+' '+al
    