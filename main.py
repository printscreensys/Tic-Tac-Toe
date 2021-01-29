class Game:
    def __init__(self, level):
        self.level = level
    
    def side(self, user):
        if user.count('X') == user.count('O'):
            side = 'X'
        else:
            side = 'O'
        
        return side

    def elements(self, user):
        user = user.replace('_',' ')
        elements = []
        for i in range(3):
            elements.append([])
        for i in range(3):
            elements[i] = [char for char in user[3*i:3*(i+1)]]
    
        return elements

    def move(self, x,y,elements):
        global user
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

game = Game(None)
user = input()
print('Enter the cells:'+user)
elements = game.elements(user)
for row in game.board(elements):
    print(row)

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
                    elements = game.move(x,y,elements)
                    for row in game.board(elements):
                        print(row)
                    correct = True
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')
    except ValueError:
        print('You should enter numbers!')
if game.check_win(elements) != None:
    print(game.check_win(elements)+' wins')
elif user.count('_')>1:
    print('Game not finished')
else:
    print('Draw')
