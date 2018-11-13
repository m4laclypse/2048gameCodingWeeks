import random

def create_grid(taille):
    #Crée une grille vide et l'initialise avec une tuile 2 et une 4
    game_grid = []
    for i in range(0,taille):
        game_grid.append([' ']*taille)
    return game_grid
    
def get_value_new_tile() :
    #On renvoie 9 fois sur 10 une tuile de valeur 2 et sinon une tuile de valeur 4
    tamponchoix = random.random()
    if random.random() < 0.9 :
        return "2"
    else :
        return "4"
        
def grid_add_new_tile(game_grid,taille, forceValue = "-1") : 
    #ajoute une nouvelle tuile de valeur aléatoire
    game_grid = normalize_grid_value(game_grid)
    if not "0" in grid_get_all_tiles(game_grid) : #On vérifie qu'il y a au moins une place de libre
        return game_grid
    newtilex, newtiley = get_new_position(game_grid)
    if forceValue == "-1" :      #Ici forceValue permet de décider de la valeur à attribuer à la tuile, par défaut on donne une valeur aléatoire à la tuile
        game_grid[newtilex][newtiley] = get_value_new_tile()
    else :
        game_grid[newtilex][newtiley] = forceValue
    return game_grid
    
        
def grid_get_all_tiles(game_grid) :
    #Renvoie une liste de toutes les tuiles, ligne par ligne, de la grille
    game_grid = normalize_grid_value(game_grid)
    all_tiles_list = []
    for row in game_grid :
        for i in range(len(row)) : #On transforme les vides en "0"
            if row[i] == " " :
                row[i] = "0"
        all_tiles_list += row
    game_grid = normalize_grid_value(game_grid)
    return all_tiles_list
    
    
def addFirstTiles(game_grid,taille) :
    game_grid = normalize_grid_value(game_grid)
    #Prend une grille supposée vide et ajoute aléatoirement une tuile 2 et une 4
    place2x, place2y = random.randint(0,taille-1),random.randint(0,taille-1)
    place4x, place4y = random.randint(0,taille-1),random.randint(0,taille-1)
    while (place4x,place4y) == (place2x,place2y) : #On veut deux places différentes pour les tuiles
        place4x, place4y = random.randint(0,taille-1),random.randint(0,taille-1)
    game_grid[place2x][place2y] = "2"
    game_grid[place4x][place4y] = "4" #On place les deux tuiles

def get_empty_tiles_positions(game_grid) :
    #On renvoie la liste des coordonnées des tuiles vides
    game_grid = normalize_grid_value(game_grid)
    taille = len(game_grid)
    empty_tiles_positions_list = []
    for i in range(taille) :
        for j in range(taille) :
            if game_grid[i][j] == " " :
                empty_tiles_positions_list.append((i,j))
    return empty_tiles_positions_list

def normalize_grid_value(game_grid) :
    #Renvoie une grille dont toutes les valeurs sont normalisées de la forme "x" avec x un nombre et " " pour une tuile vide
    taille = len(game_grid)
    for i in range(taille) :
        for j in range(taille) :
            if game_grid[i][j] == 0 or game_grid[i][j] == "0" :
                game_grid[i][j] = " "
            else :
                game_grid[i][j] = str(game_grid[i][j])
    return game_grid
    
def get_new_position(game_grid) :
    #On récupère la liste des positions des tuiles vides et on sélectionne une telle position au hasard que l'on renvoie
    game_grid = normalize_grid_value(game_grid)
    empty_tiles_positions_list = get_empty_tiles_positions(game_grid)
    number_empty_tiles = len(empty_tiles_positions_list)
    random_empty_tile = random.randint(0,number_empty_tiles-1) #On choisit la position au hasard
    return empty_tiles_positions_list[random_empty_tile]
    
def grid_get_value(game_grid,x,y) :
    #on renvoie la valeur de la grille aux coordonnées données
    game_grid = normalize_grid_value(game_grid)
    return game_grid[x][y]
    
def init_game(taille) :
    game_grid = create_grid(taille)
    game_grid = grid_add_new_tile(game_grid,taille, forceValue = "2")
    game_grid = grid_add_new_tile(game_grid,taille, forceValue = "4")
    return game_grid