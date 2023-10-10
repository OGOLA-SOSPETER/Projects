class Game:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.current_player = 'X'

    def printboard(self):
        for row in self.board:
            print('| ' + ' | ' .join(row) + ' |')

    def makemove(self):
        print(f'\n Player {self.current_player}, make your move.')
        row = int(input('Enter row'))
        column = int(input('Enter column'))

        try:
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player

            else:
                print('Invalid move!!!')
                self.makemove()
        except IndexError:
            print('Invalid move! Move out of index!!')
            self.makemove()



    def changeplayer(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def iswinner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def isboardfull(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True



    def playgame(self):
        while True:
            print('\n')
            self.printboard()
            self.makemove()
            if self.iswinner():
                print('\n')
                print(self.current_player + ' wins!')
                break

            if self.isboardfull():
                print('\n')
                print('Tie Game!')
                break

            self.changeplayer()

game = Game()
game.playgame()
