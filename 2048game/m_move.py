# -*-coding:Latin-1 -*
import random

def move_row_left(row) :
    """Moves all tiles to the left according to the rules"""
    taille = len(row)
    has_been_modified = [0] * taille 
    #This list tells us if a tile has already merged during this move (and thus must not be moved again)
    for position in range(taille) :
        leftmost_tile_value, leftmost_tile_position = row_check_tile_direction(row,"left",position) #We retrieve the value of the first encountered tile
        if leftmost_tile_value == row[position] and has_been_modified[leftmost_tile_position] == 0 :
            row[position] = " "
            row[leftmost_tile_position] = str(2*int(leftmost_tile_value)) #We fuse the two tiles
            has_been_modified[leftmost_tile_position] = 1
        else :
            tempValue = row[position]
            row[position] = " "
            row[leftmost_tile_position + 1] = tempValue
    return row
    
def move_row_right(row) : 
    """Similar function but for the right"""
    taille = len(row)
    has_been_modified = [0] * taille 
    #This list tells us if a tile has already merged during this move (and thus must not be moved again)
    for position in range(taille-1,-1,-1) :
        rightmost_tile_value, rightmost_tile_position = row_check_tile_direction(row,"right",position) #We retrieve the value of the first encountered tile
        if rightmost_tile_value == row[position] and has_been_modified[rightmost_tile_position] == 0 :
            row[position] = " "
            row[rightmost_tile_position] = str(2*int(rightmost_tile_value)) #We fuse the two tiles
            has_been_modified[rightmost_tile_position] = 1
        else :
            tempValue = row[position]
            row[position] = " "
            row[rightmost_tile_position - 1] = tempValue
    return row
    
    
def row_check_tile_direction(row,direction,index) :
    """Returns the value of the first tile encountered when moving from index in the direction given and the position of this tile. "-1" is a wall"""
    taille = len(row)
    currentPosition = index
    if direction =="left" :
        currentPosition -= 1
        while currentPosition >= 0 and row[currentPosition] == " " :
            currentPosition -= 1
        if currentPosition == -1 :
            return("-1", -1)
        else :
            return (row[currentPosition], currentPosition)
    if direction == "right" :
        currentPosition += 1
        while currentPosition < taille and row[currentPosition] == " " :
            currentPosition += 1
        if currentPosition == taille :
            return("-1", taille)
        else :
            return (row[currentPosition], currentPosition)
            
def change_orientation_matrix(game_grid) :
    """This function transforms the way the matrix is coded so that we code each column and not each row"""
    size = len(game_grid)
    new_grid = []
    for i in range(size) :
        tempRow=[]
        for j in range(size) :
            tempRow.append(game_grid[j][i])
        new_grid.append(tempRow)
    return new_grid
    
def move_grid(game_grid, direction) :
    """Moves the whole grid according to the rules of 2048 along a certain direction"""
    size = len(game_grid)
    if direction == "l" :
        for i in range(size):
            game_grid[i] = move_row_left(game_grid[i])
        return game_grid
    if direction == "r" :
        for i in range(size):
            game_grid[i] = move_row_right(game_grid[i])
        return game_grid
    game_grid = change_orientation_matrix(game_grid)
    if direction == "u" :
        for i in range(size):
            game_grid[i] = move_row_left(game_grid[i])
        return change_orientation_matrix(game_grid)
    if direction == "d" :
        for i in range(size):
            game_grid[i] = move_row_right(game_grid[i])
        return change_orientation_matrix(game_grid)
    
        
