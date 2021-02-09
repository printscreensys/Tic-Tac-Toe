from random import choice
from classes import Game
command = input().split()
print('Input command: '+ ' '.join(command))
while ' '.join(command) != 'exit':
    start = False
    exit_ = False
    while not start:
        try:
            game = Game(*command)
            elements = game.elements('_________')
            for row in game.board(elements):
                print(row)
            start = True
        except TypeError:
            print('Bad parameters!')
            command = input().split()
            print('Input command: '+ ' '.join(command))
            if command == ['exit']:
                exit_ = True
                break
    if exit_:
        break
    
    player1 = game.Player('X', game.level1)
    player2 = game.Player('O', game.level2)
 
    while game.check_win(elements) == None and player1.free_cells(elements) != []:
        if player1.level == 'user':
            print('Enter the coordinates:')
            correct = False
            while correct == False:
                try:
                    x,y = input().split()
                    print('Enter the coordinates: '+x+' '+y)
                    if player1.check_input(x,y,elements) == None:
                        x = int(x)
                        y = int(y)
                        elements = player1.move(x,y,elements)
                        for row in game.board(elements):
                            print(row)
                        correct = True
                    else:
                        print(player1.check_input(x,y,elements))
                except ValueError:
                    print('You should enter numbers!')
        else:
            print('Making move level "easy"')
            elements = player1.move(*choice(player1.free_cells(elements)), elements)
            for row in game.board(elements):
                print(row)
        if player1.free_cells(elements) != [] and game.check_win(elements) == None:
            if player2.level == 'user':
                print('Enter the coordinates:')
                correct = False
                while correct == False:
                    try:
                        x,y = input().split()
                        print('Enter the coordinates: '+x+' '+y)
                        if player2.check_input(x,y,elements) == None:
                            x = int(x)
                            y = int(y)
                            elements = player2.move(x,y,elements)
                            for row in game.board(elements):
                                print(row)
                            correct = True
                        else:
                            print(player2.check_input(x,y,elements))
                    except ValueError:
                        print('You should enter numbers!')
            else:
                print('Making move level "easy"')
                elements = player2.move(*choice(player2.free_cells(elements)), elements)
                for row in game.board(elements):
                    print(row)
    if game.check_win(elements) != None:
        print(game.check_win(elements)+' wins')
    else:
        print('Draw')
    command = input().split()
    print('Input command: '+ ' '.join(command))