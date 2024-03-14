from config import *


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


def update():
    pass


def draw():
    screen.fill(BKGCOLOR)
    pygame.display.flip()


def main():
    while True:
        events()
        update()
        draw()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
