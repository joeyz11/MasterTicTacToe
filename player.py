import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(
                self.letter + f'\'s turn. Input move: ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(
                game, -math.inf, math.inf, self.letter)['position']
        return square

    def minimax(self, state, alpha, beta, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        # base cases
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
            for possible_move in state.available_moves():
                state.make_move(possible_move, player)
                sim_score = self.minimax(state, alpha, beta, other_player)
                state.board[possible_move] = ' '
                state.current_winner = None
                sim_score['position'] = possible_move

                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, sim_score['score'])
                if beta <= alpha:
                    # print('pruned')
                    break

        else:
            best = {'position': None, 'score': math.inf}
            for possible_move in state.available_moves():
                state.make_move(possible_move, player)
                sim_score = self.minimax(state, alpha, beta, other_player)
                state.board[possible_move] = ' '
                state.current_winner = None
                sim_score['position'] = possible_move

                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, sim_score['score'])
                if beta <= alpha:
                    # print('pruned')
                    break

        return best

        # def minimax(self, state, player):
        # max_player = self.letter
        # other_player = 'O' if player == 'X' else 'X'

        # ## base cases
        # if state.current_winner == other_player:
        #     return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
        #         state.num_empty_squares() + 1)}
        # elif not state.empty_squares():
        #     return {'position': None, 'score': 0}

        # if player == max_player:
        #     best = {'position': None, 'score': -math.inf}
        # else:
        #     best = {'position': None, 'score': math.inf}

        # for possible_move in state.available_moves():
        #     state.make_move(possible_move, player)
        #     # print('next move is ', state.print_board())

        #     sim_score = self.minimax(state, other_player)
        #     # print('sim score is ', sim_score)

        #     state.board[possible_move] = ' '
        #     state.current_winner = None
        #     sim_score['position'] = possible_move

        #     if player == max_player:
        #         if sim_score['score'] > best['score']:
        #             best = sim_score
        #     else:
        #         if sim_score['score'] < best['score']:
        #             best = sim_score

        # return best
