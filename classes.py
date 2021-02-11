from random import choice
import copy


class Game:
    def __init__(self, command, level1, level2):
        self.command = command
        self.level1 = level1
        self.level2 = level2

    def board(self, elements):
        out = []
        out.append('---------')
        for row in elements:
            out.append('| '+' '.join(row)+' |')
        out.append('---------')

        return out

    def check_win(self, elements):
        for i in range(3):
            if elements[i][0] == elements[i][1] == elements[i][2] and elements[i][0] != ' ':
                return elements[i][0]
        for j in range(3):
            if elements[0][j] == elements[1][j] == elements[2][j] and elements[0][j] != ' ':
                return elements[0][j]
        if elements[0][0] == elements[1][1] == elements[2][2] and elements[0][0] != ' ':
            return elements[0][0]
        if elements[2][0] == elements[1][1] == elements[0][2] and elements[2][0] != ' ':
            return elements[2][0]
        
    def print_board(self, elements):
        for row in self.board(elements):
            print(row)

    class Player:
        def __init__(self, side, level):
            self.side = side
            self.level = level

        def check_input(self, x, y, elements):
            if x.isdigit() and y.isdigit():
                x = int(x)
                y = int(y)
                if {x, y}.issubset({1, 2, 3}):
                    if elements[x-1][y-1] != ' ':
                        return 'This cell is occupied! Choose another one!'
                else:
                    return 'Coordinates should be from 1 to 3!'
            else:
                return 'You should enter numbers!'

        def move(self, elements, level, x=None, y=None):
            if self.level == 'user':
                elements[x-1][y-1] = self.side
            if self.level == 'easy':
                x, y = choice(self.free_cells(elements))
                elements[x-1][y-1] = self.side
            if self.level == 'medium':
                can_win, can_block = None, None
                for cell in self.free_cells(elements):
                    x, y = cell
                    virtual = elements
                    virtual[x-1][y-1] = self.side
                    if Game.check_win(self, virtual) != None:
                        elements[x-1][y-1] = self.side
                        can_win = True
                        break
                    else:
                        elements[x-1][y-1] = ' '
                        x, y = cell
                        virtual = elements
                        virtual[x-1][y-1] = 'X' if self.side == 'O' else 'X'
                        if Game.check_win(self, virtual) != None:
                            can_block = True
                            elements[x-1][y-1] = self.side
                            break
                        elements[x-1][y-1] = ' '
                if not (can_win or can_block):
                    x, y = choice(self.free_cells(elements))
                    elements[x-1][y-1] = self.side
            if self.level == 'hard':
                def best_move(elements):
                    best_score = -10**6
                    move = []
                    for i in range(3):
                        for j in range(3):
                            if elements[i][j] == ' ':
                                elements[i][j] = self.side
                                score = minimax(elements, 0, False)
                                elements[i][j] = ' '
                                if score > best_score:
                                    best_score = score
                                    move = [i, j]
                    elements[move[0]][move[1]] = self.side

                    return move

                def minimax(elements, depth, isMaxi):
                    if Game.check_win(self, elements) != None:
                        if Game.check_win(self, elements) == self.side:
                            return 10
                        else:
                            return -10
                    elif Game.Player.free_cells(self, elements) == []:
                        return 0

                    if isMaxi:
                        best_score = -10**6
                        for i in range(3):
                            for j in range(3):
                                if elements[i][j] == ' ':
                                    elements[i][j] = self.side
                                    score = minimax(elements, depth + 1, False)
                                    elements[i][j] = ' '
                                    best_score = max(score, best_score)

                        return best_score

                    else:
                        best_score = 10**6
                        for i in range(3):
                            for j in range(3):
                                if elements[i][j] == ' ':
                                    elements[i][j] = 'X' if self.side == 'O' else 'O'
                                    score = minimax(elements, depth + 1, True)
                                    elements[i][j] = ' '
                                    best_score = min(score, best_score)

                        return best_score

                x, y = best_move(elements)
                elements[x][y] = self.side

            return elements

        def free_cells(self, elements):
            free_cells = []
            for i in range(3):
                for j in range(3):
                    if elements[i][j] == ' ':
                        free_cells.append((i+1, j+1))

            return free_cells