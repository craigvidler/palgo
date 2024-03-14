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
    draw_grid()
    pygame.display.flip()


def parse(file):
    with open(file) as f:
        return [[int(n) for n in line] for line in f.read().splitlines()]


def draw_grid():
    panel = pygame.Surface((GRIDWIDTH, GRIDHEIGHT))
    panel.fill(PANELCOLOR)
    for r, row in enumerate(GRID):
        for c, cost in enumerate(row):
            draw_node(panel, r, c, cost)
    screen.blit(panel, (GRIDMARGIN, GRIDMARGIN))


def draw_node(surface, r, c, cost):
    x = c * NODESIZE + c * NODEMARGIN
    y = r * NODESIZE + r * NODEMARGIN
    rect = (x, y, NODESIZE, NODESIZE)
    text = font.render(str(cost), True, TEXTCOLOR)
    pygame.draw.rect(surface, NODECOLORS[0], rect)
    surface.blit(text, (x + XPADDING, y + YPADDING))


def main():
    while True:
        events()
        update()
        draw()
        clock.tick(FPS)


if __name__ == '__main__':
    GRID = parse(FILE)
    main()
