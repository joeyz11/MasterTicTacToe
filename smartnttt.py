import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self, size):
        self.size = size
        self.board = self.make_board()
        self.current_winner = None

    def make_board(self):
        return [' ' for _ in range(self.size**2)]

    def print_board(self):
        for row in [self.board[i*self.size:(i+1) * self.size] for i in range(self.size)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_board_nums(self):
        number_board = [[str(i) for i in range(j*self.size, (j+1)*self.size)]
                        for j in range(self.size)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = math.floor(square / self.size)
        row = self.board[row_ind*self.size:(row_ind+1)*self.size]
        if all([s == letter for s in row]):
            return True
        col_ind = square % self.size
        column = [self.board[col_ind+i*self.size] for i in range(self.size)]
        if all([s == letter for s in column]):
            return True

        diagonal1 = [self.board[i]
                     for i in [j*(self.size+1) for j in range(self.size)]]
        if all([s == letter for s in diagonal1]):
            return True
        diagonal2 = [self.board[i]
                     for i in [(j+1)*(self.size-1) for j in range(self.size)]]
        if all([s == letter for s in diagonal2]):
            return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        # t0 = time.time()

        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.8)
        # t1 = time.time()

        # print('it took ', t1 - t0, 'seconds')

    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':

    board_size = input('What is the board size? Enter integer: ')
    t = TicTacToe(int(board_size))

    player1_ready = False
    while not player1_ready:
        player1 = input(
            '\nWho is player X? (1) Human, (2) RandomComputer, (3) GenuisComputer ')
        if player1 == '1':
            x_player = HumanPlayer('X')
            player1_ready = True
        elif player1 == '2':
            x_player = RandomComputerPlayer('X')
            player1_ready = True
        elif player1 == '3':
            x_player = SmartComputerPlayer('X')
            player1_ready = True
        else:
            print('\nInvalid input. Try again')

    player2_ready = False
    while not player2_ready:
        player2 = input(
            '\nWho is player O? (1) Human, (2) RandomComputer, (3) GenuisComputer ')
        if player2 == '1':
            o_player = HumanPlayer('O')
            player2_ready = True
        elif player2 == '2':
            o_player = RandomComputerPlayer('O')
            player2_ready = True
        elif player2 == '3':
            o_player = SmartComputerPlayer('O')
            player2_ready = True
        else:
            print('\nInvalid input. Try again')
    print('\n')
    if (player1 == '1' and player2 == '3') or (player1 == '3' and player2 == '1'):
        print('GenuisComputer: Omea wa mou shindeiru!\n')

    # size_range = 4
    # iters = 10
    # d = dict()

    # for size in range(size_range+1):
    #     cumulativeTime = 0
    #     for iter in range(iters):
    #         t0 = time.time()

    #         t = TicTacToe(size)
    #         result = play(t, x_player, o_player, print_game=False)

    #         t1 = time.time()
    #         cumulativeTime += t1-t0
    #     d[f'{size}x{size} average time/round'] = round(
    #         cumulativeTime / iters, 10)

    # for item in d.items():
    #     print(item)

    play(t, x_player, o_player, print_game=True)
