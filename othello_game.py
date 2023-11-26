
class OthelloGame:
    def __init__(self):
        self.board = OthelloBoard()
        self.players = [OthelloPlayer(Players.BLACK), OthelloPlayer(Players.WHITE)]
        self.turn = 0
        self.game_over = False

    def play(self):
        while not self.game_over:
            self.board.print_board()
            self.player.get_move(self.board)
            self.board.print_board()
            self.computer.get_move(self.board)
            self.turn += 1
            if self.turn == 60:
                self.game_over = True
        self.board.print_board()
        print("Game Over")
        self.board.print_score()