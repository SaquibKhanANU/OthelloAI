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

    def get_legal_moves(self):
        legal_moves = []
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 0:
                    if self.is_legal_move(i, j):
                        legal_moves.append((i, j))
        return legal_moves

    def is_legal_move(self, i, j):
        if self.board[i][j] != 0:
            return False
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                if self.is_legal_move_dir(i, j, di, dj):
                    return True
        return False

    def is_legal_move_dir(self, i, j, di, dj):
        if i + di < 0 or i + di >= 8 or j + dj < 0 or j + dj >= 8:
            return False
        if self.board[i + di][j + dj] == 0 or self.board[i + di][j + dj] == self.turn:
            return False
        i += di
        j += dj
        while i >= 0 and i < 8 and j >= 0 and j < 8:
            if self.board[i][j] == 0:
                return False
            if self.board[i][j] == self.turn:
                return True
      
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
        pygame.draw.rect(screen, colors.OTHELLO_GREEN, (x, y, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, colors.BLACK, (x, y, CELL_SIZE, CELL_SIZE), 2)
        pygame.draw.circle(screen, color, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 2 - 5)

