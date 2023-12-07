import pygame
import sys
from othello_board import OthelloBoard
from othello_player import OthelloPlayer, OthelloAI
from othello_game import OthelloGame    
import colors
import time


WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 8

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Grid")
    clock = pygame.time.Clock()

    board = OthelloBoard()
    players = [OthelloAI(colors.BLACK, 1, 3), OthelloAI(colors.WHITE, -1, 3)]
    players[1].set_opponent(players[0])
    players[0].set_opponent(players[1])
    game = OthelloGame(board, players)
    
    current_player = game.get_current_player()
    board.draw_board(screen, WIDTH, CELL_SIZE)

    while True:
        if (isinstance(current_player, OthelloAI)):
            if current_player.make_ai_move(board.get_board()):
                # time.sleep(0.5)
                board.draw_board(screen, WIDTH, CELL_SIZE)
                current_player = game.next_turn()
            else: 
                current_player = game.next_turn()
                board.draw_board(screen, WIDTH, CELL_SIZE)
        elif (isinstance(current_player, OthelloPlayer)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if  event.button == 1:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        col = mouse_x //  CELL_SIZE
                        row = mouse_y //  CELL_SIZE
                        if current_player.make_move(board.get_board(), row, col):
                            current_player = game.next_turn()
                            board.draw_board(screen, WIDTH, CELL_SIZE)
                        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()