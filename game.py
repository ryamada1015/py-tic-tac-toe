import pygame, sys
import numpy as np

pygame.init()

# constants
WIDTH, HEIGHT = 320, 320
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60
ROWS, COLS = 3, 3


# create a new window with defined width and height 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


# console board
board = np.zeros((ROWS, COLS))


def draw_board():
    SCREEN.fill(WHITE)
    pygame.draw.line(SCREEN, BLACK, (10,110), (310,110), 5)
    pygame.draw.line(SCREEN, BLACK, (10,220), (310,220), 5)
    pygame.draw.line(SCREEN, BLACK, (110,10), (110,310), 5)
    pygame.draw.line(SCREEN, BLACK, (210,10), (210,310), 5)
    pygame.display.update()

def mark_cell(row, col, player):
    board[row][col] = player


def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        # make sure while loop is running 60 times per sec
        clock.tick(FPS)
        # for each event occuring while the game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()
    
    pygame.quit()


# # check main() is running directly through main.py file, not through other files that have main.py imported
# if __name__ == "__main__":
#     main()

main()