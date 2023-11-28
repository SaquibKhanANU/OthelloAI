
class OthelloGame:
    def __init__(self, othello_board, players): # (players as input could be two AI/ two humans/ one AI one human)
        self.board = othello_board
        self.players = players
        self.num_players = len(players)
        self.current_player_index = 0
    
    def get_board(self):
        return self.board
    
    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % self.num_players
        return self.get_current_player()
    
    def get_current_player(self):
        return self.players[self.current_player_index]
