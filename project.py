from heapq import heappop, heappush
from config import *
from pathfinding import GraphSearch


def main():
    gs = GraphSearch(FILE, START, END, dijkstra)

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


def dijkstra(gs, start, end):
    pq = [start]
    previous = {}

    while pq:
        current = heappop(pq)
        path = gs.path(current, start, previous)
        yield locals()
        if current == end:
            break
        for neighbor in current.neighbors():
            if neighbor not in previous:
                neighbor.cost += current.cost
                previous[neighbor] = current
                heappush(pq, neighbor)


if __name__ == '__main__':
    main()
