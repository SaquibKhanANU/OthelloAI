from enum import Enum
import copy

class OthelloPlayer:
    def __init__(self, color, value):
        self.color = color
        self.points = 0
        self.value = value

    def make_move(self, board, row, col):
        directions = self.find_all_flanking_directions(board, row, col)
        if (directions):
            for direction in directions:
                self.flip_pieces(board, row, col, direction)
            board[row][col] = self.value
            return True
        return False
    
    def flip_pieces(self, board, row, col, direction):
        r, c = direction
        current_row, current_col = row + r, col + c
        while 0 <= current_row < len(board) and 0 <= current_col < len(board[0]):
            if board[current_row][current_col] == self.value:
                break
            board[current_row][current_col] = self.value
            current_row += r
            current_col += c
            
    def find_all_flanking_directions(self, board, row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        found_directions = []
        for direction in directions:
            if (self.find_flanking_directions(board, row, col, direction)):
                found_directions.append(direction)
        return found_directions

    def find_flanking_directions(self, board, row, col, direction):
        r, c = direction
        if board[row][col] != 0:
            return False
        current_row, current_col = row + r, col + c
        if not (0 <= current_row < len(board) and 0 <= current_col < len(board[0])):
            return False
        if board[current_row][current_col] == 0 or board[current_row][current_col] == self.value:
            return False
        while 0 <= current_row < len(board) and 0 <= current_col < len(board[0]):
            if board[current_row][current_col] == 0:
                return False
            elif board[current_row][current_col] == self.value:
                return True
            else:
                current_row += r
                current_col += c
        return False

    def generate_legal_moves(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.find_all_flanking_directions(board, row, col):
                    yield (row, col)
    
    def apply_move(self, board, move):
        new_board = copy.deepcopy(board)
        self.make_move(new_board, move[0], move[1])
        return new_board

    def get_color(self):
        return self.color

class OthelloAI(OthelloPlayer):
    def __init__(self, color, value, max_depth=3):
        super().__init__(color, value)
        self.max_depth = max_depth
        self.opponent = None
    
    def set_opponent(self, opponent):
        self.opponent = opponent
    
    def make_ai_move(self, board):
        legal_moves = self.generate_legal_moves(board)
        try:
            best_eval = float("-inf")
            best_move = None
            for move in legal_moves:
                new_board = self.apply_move(board, move)
                evaluate_board = self.minimax(new_board, self.max_depth, True)
                if evaluate_board > best_eval:
                    best_eval = evaluate_board
                    best_move = move
            return self.make_move(board, best_move[0], best_move[1])
        except:
            print("NO POSSIBLE MOVES")
            return False
    
    def minimax(self, board, depth, maximizing_player):
        if depth == 0 or self.is_terminal_node(board):
            return self.evaluate(board)
        
        if maximizing_player:
            max_eval = float('-inf')
            legal_moves = self.generate_legal_moves(board)
            for move in legal_moves:
                new_board = self.apply_move(board, move)
                evaluate_board = self.minimax(new_board, depth - 1, False)
                max_eval = max(max_eval, evaluate_board)
            return max_eval
        else:
            min_eval = float('inf')
            legal_moves = self.opponent.generate_legal_moves(board)
            for move in legal_moves:
                new_board = self.opponent.apply_move(board, move)
                evaluate_board = self.minimax(new_board, depth - 1, True)
                min_eval = min(min_eval, evaluate_board)
            return min_eval

    def is_terminal_node(self, board):
        current_legal_moves = self.generate_legal_moves(board)
        opponent_legal_moves = self.opponent.generate_legal_moves(board)
        if (current_legal_moves or opponent_legal_moves):
            return False
        black, white = self.get_score(board)
        if black > white:
            print("BLACK WIN")
            return True
        elif white > black:
            print("WHITE WIN")
            return True
        else:
            print("DRAW")
            return True
        
    def generate_legal_moves(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.find_all_flanking_directions(board, row, col):
                    yield (row, col)

    def evaluate(self, board):
        black = 0
        white = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    black += 1
                elif board[i][j] == -1:
                    white += 1
        if self.value == 1:
            return black - white
        else:
            return white - black
    
  
class OthelloAIMinmax(OthelloAI):
    pass

class OthelloAIMinmaxAlphaBeta(OthelloAIMinmax):
    pass

class OthelloAIMCTS(OthelloAI):
    pass


class OthelloAIReinforcementLearning(OthelloAI):
    pass