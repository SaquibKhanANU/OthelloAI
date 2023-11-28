import pygame
import sys
from othello_board import OthelloBoard
from othello_player import OthelloPlayer
from othello_game import OthelloGame    
import colors

WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 8

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Grid")
    clock = pygame.time.Clock()

    board = OthelloBoard()
    players = [OthelloPlayer(colors.BLACK), OthelloPlayer(colors.WHITE)]
    game = OthelloGame(board, players)
    
    current_player = game.get_current_player()
    board.draw_board(screen, WIDTH, CELL_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x //  CELL_SIZE
                row = mouse_y //  CELL_SIZE
                print(current_player.is_flanking(board, col, row))
                board.draw_piece(screen, col, row, current_player.color, CELL_SIZE)
                current_player = game.next_turn()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()