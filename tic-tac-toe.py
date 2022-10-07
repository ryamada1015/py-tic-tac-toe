import pygame, sys
import numpy as np

"""
back:
1. initialize board
2. listen for mouse event
3. read cell # and mark the cell with player #
4. check for completion 
5. switch player and repeat 2-4 until win or tie

UI:
1. display board
2. mark cell with either O or X
3. update board and display it
4. repeat 2 and 3 until win or tie

"""

pygame.init()

# constants
WIDTH, HEIGHT = 300, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (209, 128, 6)
FPS = 60
ROWS, COLS = 3, 3

CELLS = [
    [(15, 15), (115, 15), (215, 15)],
    [(15, 115), (115, 115), (215, 115)],
    [(15, 215), (115, 215), (215, 215)],
]

# images
MARK_X = pygame.image.load("mark-x.png")
MARK_O = pygame.image.load("mark-o.png")
SCALED_X = pygame.transform.scale(MARK_X, (70, 70))
SCALED_O = pygame.transform.scale(MARK_O, (70, 70))
MARK = {1: SCALED_O, 2: SCALED_X}


# create a new window with defined width and height
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def draw_board():
    SCREEN.fill(WHITE)
    pygame.draw.line(SCREEN, BLACK, (0, 100), (300, 100), 5)
    pygame.draw.line(SCREEN, BLACK, (0, 200), (300, 200), 5)
    pygame.draw.line(SCREEN, BLACK, (100, 0), (100, 300), 5)
    pygame.draw.line(SCREEN, BLACK, (200, 0), (200, 300), 5)


def cell_available(x, y):
    return board[x][y] == 0


def mark_cell(x, y, player):
    if cell_available(x, y):
        board[x][y] = player


def board_full():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def completed():
    # horizontal or vertical
    for i in range(3):
        if (
            board[i][0] == board[i][1] == board[i][2] != 0
            or board[0][i] == board[1][i] == board[2][i] != 0
        ):
            return True
    # diagnal
    if (
        board[0][0] == board[1][1] == board[2][2] != 0
        or board[0][2] == board[1][1] == board[2][0] != 0
    ):
        return True
    return False


def update_board(x, y, player):
    SCREEN.blit(MARK[player], CELLS[x][y])
    pygame.display.flip()


def init():
    global player, board
    SCREEN.fill(WHITE)
    draw_board()
    player = 1
    board = np.zeros((ROWS, COLS))
    pygame.display.flip()


def main():

    clock = pygame.time.Clock()
    running = True
    global player

    init()

    while running:
        # make sure while loop is running 60 times per sec
        clock.tick(FPS)

        # for each event occuring while the game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if completed():
                # switch player
                if player == 1:
                    player = 2
                else:
                    player = 1
                font = pygame.font.SysFont(None, 40)
                img = font.render(f"Player {player} won!", True, ORANGE)
                SCREEN.blit(img, (60, 120))
                pygame.display.flip()
                pygame.time.wait(1000 * 5)
                init()
            if board_full():
                font = pygame.font.SysFont(None, 40)
                img = font.render("It's a tie...", True, ORANGE)
                SCREEN.blit(img, (60, 120))
                pygame.display.flip()
                pygame.time.wait(1000 * 5)
                init()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseY = event.pos[0]
                mouseX = event.pos[1]

                x = mouseX // 100  # divide by 100 and round down
                y = mouseY // 100

                mark_cell(x, y, player)
                update_board(x, y, player)
                pygame.display.flip()

                # switch player
                if player == 1:
                    player = 2
                else:
                    player = 1

    pygame.quit()


# # check main() is running directly through main.py file, not through other files that have main.py imported
# if __name__ == "__main__":
#     main()

main()
