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
            elements = [[' ' for j in range(3)] for i in range(3)]
            game.print_board(elements)
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
                        x, y = int(x), int(y)
                        elements = player1.move(elements, 'user', x, y)
                        game.print_board(elements)
                        correct = True
                    else:
                        print(player1.check_input(x,y,elements))
                except ValueError:
                    print('You should enter numbers!')
        else:
            print('Making move level "{}"'.format(player1.level))
            elements = player1.move(elements = elements, level = player1.level)
            game.print_board(elements)
        if player1.free_cells(elements) != [] and game.check_win(elements) == None:
            if player2.level == 'user':
                print('Enter the coordinates:')
                correct = False
                while correct == False:
                    try:
                        x,y = input().split()
                        print('Enter the coordinates: ' + x + ' ' + y)
                        if player2.check_input(x,y,elements) == None:
                            x, y = int(x), int(y)
                            elements = player2.move(elements, 'user', x, y)
                            game.print_board(elements)
                            correct = True
                        else:
                            print(player2.check_input(x,y,elements))
                    except ValueError:
                        print('You should enter numbers!')
            else:
                print('Making move level "{}"'.format(player2.level))
                elements = player2.move(elements = elements, level = player2.level)
                game.print_board(elements)
    if game.check_win(elements) != None:
        print(game.check_win(elements)+' wins')
    else:
        print('Draw')
    command = input().split()
    print('Input command: '+ ' '.join(command))