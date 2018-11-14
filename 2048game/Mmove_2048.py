import random

def move_row_left(row) :
    """Moves all tiles to the left according to the rules"""
    taille = len(row)
    hasBeenModified = [0] * taille 
    """This list tells us if a tile has already merged during this move (and thus must not be moved again)"""
    for position in range(taille) :
        leftmostTileValue,leftmostTilePosition = row_check_tile_direction(row,"left",position) #On récupère la valeur de la première tuile rencontrée
        if leftmostTileValue == row[position] and hasBeenModified[leftmostTilePosition] == 0 :
            row[position] = " "
            row[leftmostTilePosition] = str(2*int(leftmostTileValue)) #On fusionne les deux tuiles !
            hasBeenModified[leftmostTilePosition] = 1
        else :
            tempValue = row[position]
            row[position] = " "
            row[leftmostTilePosition + 1] = tempValue
    return row
    
def move_row_right(row) : 
    """Similar function but for the right"""
    taille = len(row)
    hasBeenModified = [0] * taille 
    """This list tells us if a tile has already merged during this move (and thus must not be moved again)"""
    for position in range(taille-1,-1,-1) :
        rightmostTileValue,rightmostTilePosition = row_check_tile_direction(row,"right",position) #On récupère la valeur de la première tuile rencontrée
        if rightmostTileValue == row[position] and hasBeenModified[rightmostTilePosition] == 0 :
            row[position] = " "
            row[rightmostTilePosition] = str(2*int(rightmostTileValue)) #On fusionne les deux tuiles !
            hasBeenModified[rightmostTilePosition] = 1
        else :
            tempValue = row[position]
            row[position] = " "
            row[rightmostTilePosition - 1] = tempValue
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