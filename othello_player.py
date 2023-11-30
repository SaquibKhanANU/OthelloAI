from enum import Enum

class OthelloPlayer:
    def __init__(self, color, value):
        self.color = color
        self.points = 0
        self.value = value

    def make_move(self, board, row, col):
        directions = self.find_all_flanking_directions(board.get_board(), row, col)
        if (directions):
            for direction in directions:
                self.flip_pieces(board.get_board(), row, col, direction)
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

    def get_color(self):
        return self.color

class OthelloAI(OthelloPlayer):
    def __init__(self, color):
        super().__init__(color)

    def can_make_move(self):
        pass
    
    def find_best_move(self):
        pass
  
class OthelloAIMinmax(OthelloAI):
    pass

class OthelloAIMinmaxAlphaBeta(OthelloAIMinmax):
    pass

class OthelloAIMCTS(OthelloAI):
    pass


class OthelloAIReinforcementLearning(OthelloAI):
    pass