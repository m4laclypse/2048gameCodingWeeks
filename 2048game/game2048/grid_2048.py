import random




# Variable that contains the different themes of the 2048 game
THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256",
                512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"},
          "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O",
                512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"},
          "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H",
                512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}

DIRECTIONS = {"right": (0,1), "left": (0,-1), "up": (-1,0), "down": (1,0)}


def create_grid(n=4):
    """
    Create a new game grid
    :param n: (int) the size of the grid nxn
    :return: (list) the grid as a list of lists
    """
    game_grid = []
    # Grid of size n x n
    for i in range(0, n):
        game_grid.append([0 for j in range(n)])
    return game_grid


def init_game(n=4):
    """
    Create a new game grid with two tiles
    :param n: (int) the size of the grid nxn
    :return: (list) the game grid as a list of lists
    """
    game_grid = create_grid(n)
    game_grid = grid_add_new_tile(game_grid)
    game_grid = grid_add_new_tile(game_grid)
    return game_grid




def get_all_tiles(grid):
    """
    Return a list with all the values of the tiles of the grid
    :param grid: (list) the game grid as a lits of list
    :return: (list) a list with all the values of the game
    """
    tiles = []
    for row in grid:
        for tile in row:
            tiles.append(tile)
    return tiles



def long_value(grid):
    """
    Return the length of the longest tile
    :param grid: (list) the game grid
    :return: (int) size ot the longest tile value
    """

    length = 0
    for tile in get_all_tiles(grid):
        if len(str(tile)) > length:
            length = len(str(tile))
    return length


def grid_get_value(grid, x,y):
    """
    Retourne la valeur de la tuile possédant les coordonnées dans le couple
    paramètre grid: (list) la grille sous forme de liste
    paramètre coord: (tuple) un couple de coordonnée (x, y)
    valeur renvoyée: (int) la valeur de la tuile possédant les coordonnées du couple, None sinon
    Exemples:
    >>> grid = [[0, 2, 4, 0], [2048, 512, 32, 0], [16, 32, 0, 4], [0, 0, 128, 254]]
    >>> grid_get_value(grid, (4, 4)) is None
    True
    >>> grid_get_value(grid, (1, 0))
    2048
    >>> grid_get_value(grid, (3, 2))
    128
    """
    try:
        return grid[x][y]
    except:
        return None




def long_value_with_theme(grid,theme):
    """
    Return the length of the longest tile according to the theme
    :param grid: (list) the game grid
    :param theme: (dict) the targeted theme
    :return: (int) size ot the longest tile value
    """

    themegrid=theme
    length = 0
    for tile in get_all_tiles(grid):
        a = themegrid[tile]
        if len(str(themegrid[tile])) > length:
            length = len(str(themegrid[tile]))
    return length


def grid_to_string(grid, n=4):
    """

    :param grid:
    :param n:
    :return:
    """
    string_grid = ' ===' * ((n)) + '\n'
    for row in grid:
        s = ''
        for tile in row:
            if tile == 0:
                tile = ' '
            s = s + '|{:{align}{width}}'.format(str(tile), align='^', width=3)
        s = s + '|' + "\n"
        s = s + ' ===' * ((n)) + '\n'
        string_grid = string_grid + s
    return (string_grid)



def grid_to_string_with_size(grid, n=4):
    """

    :param grid:
    :param n:
    :return:
    """
    size_tile = long_value(grid)
    string_grid = '=' * ((n+1) + size_tile * n ) + '\n'
    for row in grid:
        s = ''
        for tile in row:
            if tile == 0:
                tile = ' '
            s = s + '|{:{align}{width}}'.format(str(tile), align='^', width=str(size_tile))
        s = s + '|' + "\n"
        s = s + '=' * ((n+1) + size_tile * n ) + '\n'
        string_grid = string_grid + s
    return (string_grid)


def grid_to_string_with_size_and_theme(grid,theme,n=4):
    """

    :param grid:
    :param theme:
    :param n:
    :return:
    """
    size_tile = long_value_with_theme(grid, theme)
    string_grid = '=' * ((n+1) + size_tile * n ) + '\n'
    for row in grid:
        s = ''
        for tile in row:
            if tile == 0:
                tile = ' '

            else:
                tile =theme[tile]
            s = s + '|{:{align}{width}}'.format(tile, align='^', width=str(size_tile))
        s = s + '|' + "\n"
        s = s + '=' * ((n+1) + size_tile * n ) + '\n'
        string_grid = string_grid + s
    return string_grid









def grid_add_new_tile(grid):
    """
    Add a new tile in the grid game at a free position
    :param grid: (list) the game grid
    :return: (list) the game grid
    """
    x, y = get_new_position(grid)
    grid[x][y] = get_value_new_tile()
    return grid


def get_all_tiles(grid):
    """
    Return the set of all tiles of a grid in a single list
    :param grid: (list) the game grid
    :return: (list) a list with the values of the tiles of the game_grid. If the position is free, the 0 value is returned
    """
    tiles = []
    for row in grid:
        for tile in row:
            if tile == ' ':
                tile = 0
            tiles.append(tile)
    return tiles


def get_value_new_tile():
    """
    Get the value 2 or 4 randomly with 90% of chance for 2
    :return: (int )  tile value between 2 or 4
    """
    tile_value = 4
    a = random.random()
    if a < 0.9:
        tile_value = 2
    return tile_value


def grid_get_value(grid, x, y):
    """
    Returns the value of the grid in coordinate (x,y)
    :param grid: (list)the grid game
    :param x: (int) the first coordinate
    :param y: (int) the second coordiate
    :return: (int) the value of the tile in (x,y). If there is no tile, return 0
    """
    value = grid[x][y]
    if value == ' ':
        value = 0
    return value


def get_empty_tiles_positions(grid):
    """
    Return a list of tuples of coordinates of the empty tiles
    :param grid: (list) the game grid
    :return: (list of tuples) the list of tuple coordinates
    """
    empty_tiles = []
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid_get_value(grid, x, y) == 0:
                empty_tiles.append((x, y))
    return empty_tiles


def get_new_position(grid):
    """
    Return the coordinate of a free position for a new tile in the grid
    :param grid: (list) the game grid
    :return: (tuple) the coordinate for the new tile
    """
    return random.choice(get_empty_tiles_positions(grid))



def move_row_left(row):
    """
    Apply a move of the row to the left according to the 2048 game rules
    :param row: (list) a row
    :return: the moved row
    """

    new_row =[0 for i in range(len(row))]
    previous_tile = None
    index_tile = 0

    for i in range(len(row)):
        if row[i]!=0:
            if previous_tile is None:
                previous_tile=row[i]
            else:
                # Comparison with the previous tile
                if row[i] == previous_tile:
                    # tile of the same value
                    new_row[index_tile] = row[i]*2
                    index_tile = index_tile +1
                    previous_tile = None
                else:
                # we move the tile
                    new_row[index_tile] = previous_tile
                    index_tile = index_tile +1
                    previous_tile=row[i]
    if previous_tile is not None:
        new_row[index_tile] = previous_tile
    return new_row


def reverse(row):
    """

    :param row:
    :return:
    """

    if len(row)==0:
        return []
    if len(row)==1:
        return row
    else:
        return [row[len(row)-1]] + reverse(row[0:len(row)-1])




def transpose_grid(grid):
    """
    Inverse the order of the grid (reading from up to bottom)
    :param grid:
    :return: the transposed grid
    """
    new = []
    for j in range(len(grid)):
        new.append([grid[i][j] for i in range(len(grid))])
    return new








def move_row_right(row):
    """
    Apply a move of the row to the right according to the 2048 game rules
    :param row: (list) a row
    :return: the moved row
    """
    row_moved = reverse(row)
    row_moved = move_row_left(row_moved)
    return reverse(row_moved)



def move_grid(grid, d):
    """
    Apply the move to the grid in the direction d
    paramètre grid: (list) the grid
    paramètre d: (str) the code of the move
    Exemples:
    """
    new = grid.copy()
    d = DIRECTIONS[d]
    x, y = d[0], d[1]
    # Gauche
    if y == -1:
        for i in range(len(grid)):
            new[i] = move_row_left(grid[i])
    # Droite
    elif y == 1:
        for i in range(len(grid)):
            row = grid[i].copy()
            new[i] = move_row_right(grid[i])
    # Up
    elif x == -1:
        new = transpose_grid(grid)
        for i in range(len(new)):
            new[i] = move_row_left(new[i])
        new = transpose_grid(new)
    # Down
    elif x == 1:
        new = transpose_grid(grid)
        for i in range(len(new)):
            row = new[i].copy()
            new[i] = move_row_right(row)
        new = transpose_grid(new)
    return new


def is_grid_over(grid):
    """
    Teste si la grille passée en paramètre est pleine ou non
    paramètre grid: (list) la grille sous forme de liste
    valeur renvoyée: (bool) True si la grille est pleine (valeurs différents de 0), False sinon
    Exemples:
    >>> is_grid_over([[0,4,8,2], [0,0,0,0], [0,512,32,64], [1024,2048,512,0]])
    False
    >>> is_grid_over([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]])
    True
    """
    return not 0 in all_tiles(grid)



def all_tiles(grid):
    """
    Retourne une liste contenant toutes les valeurs dans la grilles
    paramètre grid: (list) la grille sous forme de liste
    valeur renvoyée: (list) une liste contenant toutes les valeurs dans la grille
    Exemples:
    >>> all_tiles([[0,4,8,2], [0,0,0,0], [0,512,32,64], [1024,2048,512,0]])
    [0, 4, 8, 2, 0, 0, 0, 0, 0, 512, 32, 64, 1024, 2048, 512, 0]
    >>> all_tiles([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]])
    [16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]
    """
    tiles = []
    for row in grid:
        for tile in row:
            tiles.append(tile)
    return tiles


def move_possible(grid):
    """
    Renvoie une liste de booléen si les déplacements dans chaques directions est possible
    paramètre grid: (list) la grille sous forme de liste
    Exemples:
    >>> move_possible([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]])
    [True, True, True, True]
    >>> move_possible([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]])
    [False, False, False, False]
    """
    moves = []
    # [RIGHT, LEFT, UP, DOWN]
    for d in DIRECTIONS.keys():
        new = move_grid(grid, d)
        if new == grid:
            moves.append(False)
        else:
            moves.append(True)
    return moves


def is_game_over(grid):
    if is_grid_over(grid):
        return True
    elif move_possible(grid)==[False,False,False,False]:
        return True
    else:
        return False



def grid_get_grid_max_tile(grid):
    """
    Retourne la plus grande valeur dans la grille passée en paramètre
    paramètre grid: (list) la grille sous forme de liste
    valeur renvoyée: (int) la valeur maximale contenue dans la grille
    Exemples:
    >>> grid_get_max_value([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]])
    2048
    >>> grid_get_max_value([[16,4,8,2], [2,4,2,128], [4,512,32,64], [16,0,512,2]])
    512
    """
    return max(get_all_tiles(grid))



# print(create_grid(4))
#
#
#
# a = """
#  === === === ===
# |   |   |   |   |
#  === === === ===
# |   |   |   |   |
#  === === === ===
# |   |   |   |   |
#  === === === ===
# | 2 |   |   | 2 |
#  === === === ===
#     """
#
# print(grid_to_string(init_game(4)))
#
# print(grid_to_string_with_size([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]]))
#
# print(grid_to_string_with_size_and_theme([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]],THEMES["1"]))
#
#
# a="""
# =============
# |Be|He|Li|H |
# =============
# |H |He|H |N |
# =============
# |He|F |B |C |
# =============
# |Ne|Na|F |H |
# =============
#
# """
# print(list(a))
# print(list(grid_to_string_with_size_and_theme([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]],THEMES["1"])))
# print( a == grid_to_string_with_size_and_theme([[16, 4, 8, 2], [2, 4, 2, 128], [4, 512, 32, 64], [1024, 2048, 512, 2]],THEMES["1"]))
