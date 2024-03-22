from config import *
from pathfinding import GraphSearch, algos


def main():
    gs = GraphSearch(FILE, START, END, algos[ALGO])

    while True:
        events()
        gs.step()
        draw(gs)
        clock.tick(FPS)


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


def draw(gs):
    screen.fill(BKGCOLOR)
    panel = pygame.Surface((GRIDWIDTH, GRIDHEIGHT))
    panel.fill(PANELCOLOR)
    gs.draw(panel)
    screen.blit(panel, (GRIDMARGIN, GRIDMARGIN))
    pygame.display.flip()


if __name__ == '__main__':
    main()
