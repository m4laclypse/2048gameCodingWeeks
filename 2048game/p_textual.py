# -*-coding:Latin-1 -*
def read_player_command():
    move = input("Enter your order (l (left), r (right), t (top), b (bottom)):")
    while len(move)!=1 and move not in "lrtb":
        move = input("Error ! Enter your order (l (left), r (right), t (top), b (bottom)):")
    return move

def menu():
    size=4
    themeIndex=0
    print('====Menu====')
    print('1. Play')
    print('2. Game size')
    print('3. Game theme')
    print('4. Exit')
    answer=()
    while len(answer)!=1 and answer not in "1234":
        answer('Incorrect Answer ! Do it again correctly this time')
    if (answer=='1'):
        #Launching the game
        print('Launching the game')
    elif (answer=='2'):
        reponse=input('Size of the grid ?')
        while type(eval(reponse))!='int' and int(reponse)>1:
            reponse=input('Size of the grid ?')
        size=int(reponse)
    elif (answer=='3'):
        print('====Game Theme===')
        print('1. Classic theme')
        print('2. Chemistry theme')
        reponse=input('Theme of the game ?')
        while type(eval(reponse))!='int' and reponse not in '12':
            reponse=input('Theme of the game ?')
        themeIndex=int(reponse)-1
    elif (answer=='4'):
        print('\nGoodbye')
    
