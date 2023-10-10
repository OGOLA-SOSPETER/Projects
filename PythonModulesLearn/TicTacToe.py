#Tic-tac-toe game
# Path: PythonModulesLearn\TicTacToe.py
#Tic-tac-toe game


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self):
        row = int(input('Enter row: '))
        col = int(input('Enter column: '))

        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
        else:
            print('Invalid move')

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def is_winner(self):
        # check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True

        # check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        # check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play_game(self):
        while True:
            self.print_board()
            self.make_move()

            if self.is_winner():
                print(self.current_player + ' wins!')
                break

            if self.is_board_full():
                print('Tie!')
                break

            self.switch_player()

game = TicTacToe()
game.play_game()
