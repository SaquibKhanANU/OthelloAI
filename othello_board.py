from enum import Enum
import pygame
import colors 

class OthelloBoard:
    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.board[3][3] = 1
        self.board[3][4] = -1
        self.board[4][3] = -1
        self.board[4][4] = 1

    def get_board(self):
        return self.board

    def get_score(self):
        black = 0
        white = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 1:
                    black += 1
                elif self.board[i][j] == -1:
                    white += 1
        return black, white
      
    def draw_board(self, screen, GRID_SIZE, CELL_SIZE):
        for row in range(self.board.__len__()):
            for col in range(self.board.__len__()):
                x, y = col * CELL_SIZE,row* CELL_SIZE
                if self.board[row][col] == 0:
                    pygame.draw.rect(screen, colors.OTHELLO_GREEN, (x, y, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, colors.BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)
                elif self.board[row][col] == 1:
                    self.draw_piece(screen, col, row, colors.BLACK, CELL_SIZE)
                elif self.board[row][col] == -1:
                    self.draw_piece(screen, col, row, colors.WHITE, CELL_SIZE)

    def draw_piece(self, screen, col, row, color, CELL_SIZE):
        x, y = col * CELL_SIZE,row * CELL_SIZE
        self.board[row][col] = color
        pygame.draw.rect(screen, colors.OTHELLO_GREEN, (x, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, colors.BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)
        pygame.draw.circle(screen, color, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

