import pygame
import sys
from othello_board import OthelloBoard

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 8
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Grid")

board = OthelloBoard()

board.draw_board(screen, WIDTH/8, HEIGHT/8)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button down")
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check which cell was clicked
            clicked_col = mouse_x //  (WIDTH//8)
            clicked_row = mouse_y //  (WIDTH//8)

            # Draw a piece on the clicked cell
            board.draw_piece(screen, clicked_col, clicked_row, (0, 0, 0),  WIDTH//8)


    # Draw the grid

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(60)
