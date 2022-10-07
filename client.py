from network import Network
from game import Game
import pickle
import pygame


"""constants"""
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


def update_board(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                SCREEN.blit(MARK[1], CELLS[i][j])
            elif board[i][j] == 2:
                SCREEN.blit(MARK[2], CELLS[i][j])
    pygame.display.flip()


def init_UI():
    draw_board()
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    running = True
    n = Network()
    player = int(n.player)
    pygame.init()

    while running:
        clock.tick(FPS)

        try:
            game = n.send("get")
        except:
            print("ERROR: Couldn't load game")
            running = False
            break

        update_board(game.board)

        if game.board_empty():
            init_UI()

        elif game.completed():
            font = pygame.font.SysFont(None, 40)
            img = font.render(f"Player {player} won!", True, ORANGE)
            SCREEN.blit(img, (60, 120))
            pygame.display.flip()
            pygame.time.delay(500)
            n.send("reset")
            init_UI()

        elif game.board_full():
            font = pygame.font.SysFont(None, 40)
            img = font.render("It's a tie", True, ORANGE)
            SCREEN.blit(img, (60, 120))
            pygame.display.flip()
            pygame.time.delay(500)
            n.send("reset")
            init_UI()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.lock:
                    font = pygame.font.SysFont(None, 40)
                    img = font.render(
                        "Wait for your opponent to finish...", True, ORANGE
                    )
                    SCREEN.blit(img, (60, 120))
                    pygame.display.flip()
                    game.lock = False
                    break
                mouseY = event.pos[0]
                mouseX = event.pos[1]

                x = mouseX // 100  # divide by 100 and round down
                y = mouseY // 100

                n.send(str(x) + str(y))

                update_board(game.board)
                pygame.display.flip()

    pygame.quit()


main()
