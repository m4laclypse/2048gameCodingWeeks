from game2048 import grid_2048
from random import randint
import time




def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move

def read_gridsize():
    """
    Lit la taille de la grille demandée par l'utilisateur
    valeur renvoyée: (int) la taille de la grille
    """
    number = input('What grid size do you want to play? (between 3 and 10) ')
    while int(number) < 3 or 10 < int(number):
        number = input('What grid size do you want to play? (between 3 and 10) ')
    return int(number)

def read_theme():
    """
    Lit le theme demandée par l'utilisateur
    valeur renvoyée: (str) l'identifiant du theme
    """
    theme = input('What grid theme do you want? ((0)Default, (1)Chemistry, (2)Alphabet) ')
    while theme not in grid_2048.THEMES:
        theme = input('What grid theme do you want? ((0)Default, (1)Chemistry, (2)Alphabet) ')
    return theme




def randomplay():
    """
    Lancement de la partie avec l'ordinateur qui joue à la place du joueur
    """
    n = read_gridsize()
    numbertheme = read_theme()
    grid = grid_2048.init_game(n)
    theme = grid_2048.THEMES[numbertheme]
    print(theme)
    print(grid_2048.grid_to_string_with_size_and_theme(grid,theme,n ))
    directions=["left", "right", "up","down"]
    while not grid_2048.is_game_over(grid):
        move = randint(0,3)
        possible_moves = grid_2048.move_possible(grid)
        while possible_moves[move] != True:
            move = randint(0,3)
        # Application of the move
        grid = grid_2048.move_grid(grid, directions[move])
        # Ajout d'une nouvelle tuile
        grid =grid_2048.grid_add_new_tile(grid)
        # Affichage de la grille et du mouvement effectue
        print("move : ",directions[move])
        print(grid_2048.grid_to_string_with_size_and_theme(grid, theme, n))
        # Pause de 700ms
        time.sleep(0.7)
    if grid_2048.grid_get_grid_max_tile(grid) >= 2048:
        print("Computer won !")
    else:
        print("Computer lose !")
    print("Please restart the program to play a new game")


# def play():
#     """
#     Lancement de la partie
#     """
#
#     number = read_gridsize()
#     grid = grid_2048.init_game(number)
#     theme = grid_2048.THEMES[read_theme()]
#
#     print(grid_2048.grid_to_string_with_size_and_theme(grid, theme, number))
#     # Arrêt si la grille est pleine ou aucun mouvement possible
#     while not grid_2048.is_game_over():
#         # Lecture de la direction souhaitée
#         move = read_player_command()
#
#         # Retour arrière
#         elif move == "B":
#             if last_grid is not None and last_grid != grid:
#                 if undo > 0:
#                     undo -= 1
#                     grid = last_grid
#                     print("Success. "+str(undo)+" undo left")
#                 else:
#                     print("No more undo available")
#             else:
#                 print("There is no move to replace")
#             grid_print(grid, number, theme)
#             continue
#         elif move == "H":
#             if hint > 0:
#                 best_move, evaluation = grid_max(grid)
#                 hint -= 1
#                 print("The best move is "+best_move+". "+str(hint)+" hint left")
#             else:
#                 print("No more hint available")
#             continue
#         new_grid  = grid_move(grid, COMMANDS[move])
#         # Pas de déplacement dans la direction d donc on demande une autre direction
#         if new_grid == grid:
#             continue
#         grid, last_grid = new_grid, grid
#         # Ajout d'une nouvelle tuile
#         grid_add_new_tile(grid)
#         # Affichage de la grille
#         grid_print(grid, number, theme)
#     if grid_get_max_value(grid) >= 2048:
#         print("You win !!")
#     else:
#         print("You lose...")
#     # Ajout du score dans le classement
#     add_leaderboard("leaderboard", pseudo, grid_score(grid), number)
#     # Fin de la partie
#     print("Your score is "+str(grid_score(grid)))
#     print("Please restart the program to play a new game")




randomplay()
