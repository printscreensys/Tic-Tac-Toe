from random import choice

class Game:
    def __init__(self, level):
        self.level = level
    
    def side(self, user = 'X'):

        return user

    def elements(self, user):
        user = user.replace('_',' ')
        elements = []
        for i in range(3):
            elements.append([])
        for i in range(3):
            elements[i] = [char for char in user[3*i:3*(i+1)]]
    
        return elements

    def move(self, x, y, elements, user):
        elements[x-1][y-1] = self.side(user)

        return elements

    def board(self, elements):
        out = []
        out.append('---------')
        for row in elements:
            out.append('| '+' '.join(row)+' |')
        out.append('---------')

        return out

    def check_win(self, elements):
        for i in range(3):
            if elements[i][0] == elements[i][1] and elements[i][1] == elements[i][2] and elements[i][0] != ' ':
                return elements[i][0]
        for j in range(3):
            if elements[0][j] == elements[1][j] and elements[1][j] == elements[2][j] and elements[0][j] != ' ':
                return elements[0][j]
        if elements[0][0] == elements[1][1] and elements[1][1] == elements[2][2] and elements[0][0] != ' ':
            return elements[0][0]
        if elements[2][0] == elements[1][1] and elements[1][1] == elements[0][2] and elements[2][0] != ' ':
            return elements[2][0]

    def free_cells(self, elements):
        free_cells = []
        for i in range(3):
            for j in range(3):
                if elements[i][j] == ' ':
                    free_cells.append((i+1,j+1))
        
        return free_cells

game = Game('easy')
user = '_________'
elements = game.elements(user)
for row in game.board(elements):
    print(row)
while game.check_win(elements) == None or game.free_cells(elements) != []:
    correct = False
    while correct == False:
        try:
            x,y = input().split()
            print('Enter the coordinates:'+x+' '+y)
            if x.isdigit() and y.isdigit():
                x = int(x)
                y = int(y)
                if {x,y}.issubset({1,2,3}):
                    target = elements[x-1][y-1]
                    if target != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        elements = game.move(x,y,elements, 'X')
                        for row in game.board(elements):
                            print(row)
                        correct = True
                else:
                    print('Coordinates should be from 1 to 3!')
            else:
                print('You should enter numbers!')
        except ValueError:
            print('You should enter numbers!')
    if game.free_cells(elements) != []:
        print('Making move level "easy"')
        elements = game.move(*choice(game.free_cells(elements)), elements, 'O')
        for row in game.board(elements):
            print(row)
    else:
        break
    
if game.check_win(elements) != None:
    print(game.check_win(elements)+' wins')
else:
    print('Draw')
