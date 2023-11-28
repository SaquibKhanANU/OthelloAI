from enum import Enum

class OthelloPlayer:
    def __init__(self, color):
        self.color = color
        self.points = 0

    def make_move(self, board, row, col):
        if (is_flanking(board, row, col)):
            flip_pieces(board, row, col)
            return True
        return False
    
    def flip_pieces(self, board, row, col):
        pass
    
    def is_flanking(self, board, row, col):
        pass

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