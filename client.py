import pygame

WIDTH, HEIGHT = 500, 500

# create a new window with defined width and height 
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

WHITE = (255,255,255)

# how many frames per second to update the game 
FPS = 60

# identify current client
clientNumber = 0

# initialize the window 
def redraw_window():
    win.fill(WHITE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        # make sure while loop is run 60 times per sec
        clock.tick(FPS)
        # for each event occuring while the game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        redraw_window()

    pygame.quit()

# check main() is run directly through main.py file, not through other files that have main.py imported
if __name__ == "__main__":
    main()