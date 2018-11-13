from tkinter import *
from tkinter.messagebox import *
from game2048 import grid_2048
from pygame import *

TILES_BG_COLOR = {0: "#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f1b078", \
                  16: "#eb8c52", 32: "#f67c5f", 64: "#f65e3b", \
                  128: "#edcf72", 256: "#edcc61", 512: "#edc850", \
                  1024: "#edc53f", 2048: "#edc22e", 4096: "#5eda92", \
                  8192: "#24ba63"}

TILES_FG_COLOR = {0: "#776e65", 2: "#776e65", 4: "#776e65", 8: "#f9f6f2", \
                  16: "#f9f6f2", 32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", \
                  256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", \
                  2048: "#f9f6f2", 4096: "#f9f6f2", 8192: "#f9f6f2"}

TILES_FONT = {"Verdana", 40, "bold"}

TILES_FONT = {"Verdana", 40, "bold"}

GAME_SIZE = 600
GAME_BG = "#92877d"
TILES_SIZE = GAME_SIZE // 4

COMMANDS = {"Up": "up", "Left": "left", "Right": "right", "Down": "down"}


gr_grid = []












# def key_pressed(event):
#         """
#         Lors de la pression d'une touche
#         """
#         global grid, finish, lose, last_grid
#         key = event.keysym
#         # Inutile dès que l'utilisateur a perdu
#         if not lose:
#             if key in COMMANDS:
#                 new_grid = grid_move(grid, COMMANDS[key])
#                 # Tant qu'un mouvement est possible on continuer a jouer
#                 if grid != new_grid and (not is_grid_over(grid) or True in move_possible(grid)):
#                     grid, last_grid = new_grid, grid
#                     grid_add_new_tile(grid)
#                 # Refresh de l'interface
#                 grid_display(grid)
#                 # Affichage du message de victoire
#                 if grid_get_max_value(grid) == 2048 and not finish:
#                     showinfo("2048", "You won !")
#                     finish = True
#                 # Affichage du message de fin
#                 if is_grid_over(grid) and not True in move_possible(grid):
#                     showinfo("2048", "You lose !")
#                     # Ajout du score dans le classement
#                     add_leaderboard("leaderboard", pseudo, grid_score(grid), n)
#                     lose = True
#

def sound_victory():
    mixer.init()
    son_Blop=mixer.Sound("./Sounds/blop.wav")
    son_Blop.play()


def play():

    def key_pressed(event):
        """
        Lors de la pression d'une touche
        """
        global grid
        key = event.keysym
        if key in COMMANDS:
            new_grid = grid_2048.move_grid(grid, COMMANDS[key])
            # Tant qu'un mouvement est possible on continuer a jouer
            if not grid_2048.is_game_over(grid):
                grid = new_grid
                grid_2048.grid_add_new_tile(grid)
                # Refresh de l'interface
            grid_display(grid)

    def grid_display(grid):
        global n, gr_grid, theme_id
        print(grid)
        for i in range(4):
            for j in range(4):
                number = grid_2048.grid_get_value(grid, i, j)
                gr_grid[i][j].configure(text=grid_2048.THEMES[theme_id][number], \
                                            bg=TILES_BG_COLOR[number], \
                                        fg=TILES_FG_COLOR[number])
        game.update_idletasks()

    global n, gr_grid,theme_id, grid
    theme_id = '0'
    n = 4
    game = Toplevel(root)
    game.title("2048")
    game.bind("<Key>", key_pressed)
    game.grid()
    n=4
    theme_id="0"
    background = Frame(game, bg=GAME_BG)
    background.grid()
    grid = grid_2048.init_game()
    gr_grid = []
    for i in range(n):
        gr_line = []
        for j in range(n):
            cell = Frame(background, bg=TILES_BG_COLOR[0], width=TILES_SIZE, height=TILES_SIZE)
            cell.grid(row=i, column=j, padx=1, pady=1)
            t = Label(master=cell, text="", bg=TILES_BG_COLOR[0], \
                          justify=CENTER, font=TILES_FONT, \
                          width=8, height=4)
            t.grid()
            gr_line.append(t)
        gr_grid.append(gr_line)
    grid_display(grid)
    game.mainloop()






if __name__ == '__main__':
    # Creation du menu
    root = Tk()
    root.title("2048")
    #root.geometry(get_center_position(root, 250, 215))
    root.resizable(False, False)
    # # Initialisation des widgets
    # label_pseudo = Label(root, text="Choose your pseudo")
    # pseudo_entry = Entry(root)
    label = Label(root, text="Choose grid size")
    spin = Spinbox(root, from_=4, to=8)
    label_theme = Label(root, text="Choose a theme")
    list_theme = Listbox(root, selectmode="single")
    list_theme.config(height=4)
    button = Button(root, text="Play", command=play)
    # button_autoplay = Button(root, text="Computer")
    button_quit = Button(root, text="Quit", command=sound_victory)
    # # Recuperation des themes dans le module game
    for key in grid_2048.THEMES.keys():
        list_theme.insert(key, grid_2048.THEMES[key]["name"])
    # # Affichage des widgets
    # label_pseudo.pack(pady=5)
    # pseudo_entry.pack()
    label.pack()
    spin.pack()
    label_theme.pack()
    list_theme.pack()
    button.pack(side=RIGHT, padx=5, pady=5)
    # button_autoplay.pack(side=RIGHT, pady=5)
    button_quit.pack(side=LEFT, padx=5, pady=5)
    # # Boucle
    root.mainloop()
