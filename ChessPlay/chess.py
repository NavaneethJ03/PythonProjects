# import pygame


# pygame.init()
# WIDTH = 1000
# HEIGHT = 900
# screen = pygame.display.set_mode([WIDTH,HEIGHT])
# font = pygame.font.Font("freesansbold.ttf",20)
# big_font = pygame.font.Font("freesansbold.ttf",50)
import tkinter as tk

# Create the board
class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.colors = [['white' for _ in range(8)] for _ in range(8)]
        self.colors[0][0] = 'black'
        self.colors[0][7] = 'black'
        self.colors[7][0] = 'black'
        self.colors[7][7] = 'black'

    def draw_board(self, canvas):
        for i in range(8):
            for j in range(8):
                if self.colors[i][j] == 'white':
                    canvas.create_rectangle(i * 60, j * 60, (i + 1) * 60, (j + 1) * 60, fill='white')
                else:
                    canvas.create_rectangle(i * 60, j * 60, (i + 1) * 60, (j + 1) * 60, fill='gray')

# Create the pieces
class Piece:
    def __init__(self, x, y, color, piece_type):
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type

    def draw_piece(self, canvas):
        if self.color == 'white':
            if self.piece_type == 'pawn':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=white_pawn_image)
            elif self.piece_type == 'rook':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=white_rook_image)
            elif self.piece_type == 'knight':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=white_knight_image)
            elif self.piece_type == 'bishop':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=white_bishop_image)
            elif self.piece_type == 'queen':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=white_queen_image)
            elif self.piece_type == 'king':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=white_king_image)
        else:
            if self.piece_type == 'pawn':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=black_pawn_image)
            elif self.piece_type == 'rook':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=black_rook_image)
            elif self.piece_type == 'knight':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=black_knight_image)
            elif self.piece_type == 'bishop':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=black_bishop_image)
            elif self.piece_type == 'queen':
                canvas.create_image(self.x * 60 + 30, self.y * 60 + 30, image=black_queen_image)
            elif self.piece_type == 'king':
                canvas.create_image(self.x * 60 + 30, self.y * 