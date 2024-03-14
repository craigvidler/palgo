import pygame

SCREENRECT = pygame.Rect(0, 0, 1200, 596)
BKGCOLOR = 'gray35'
TEXTSIZE = 14
FPS = 10


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
    pygame.init()
    pygame.display.set_caption('Palgo')
    screen = pygame.display.set_mode(SCREENRECT.size)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Menlo', TEXTSIZE)
    main()
