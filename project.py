from heapq import heappop, heappush
from config import *


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


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


def dijkstra(graph, start, end):
    pq = [(0, start)]
    previous = {}

    while pq:
        cost, current = heappop(pq)
        yield current
        if current == end:
            yield cost, path(end, previous)
        for r, c in neighbors(*current, *end):
            if (r, c) not in previous:
                previous[(r, c)] = current
                heappush(pq, (cost + graph[r][c], (r, c)))
        clock.tick(FPS)


def path(node, previous):
    return [node] if node == START else path(previous[node], previous) + [node]


def neighbors(r, c, maxrow, maxcol):
    for row, col in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= row <= maxrow and 0 <= col <= maxcol:
            yield (row, col)


def main():
    d = dijkstra(GRID, START, END)
    while True:
        events()
        try:
            print(next(d))
        except StopIteration:
            pass
        draw()
        clock.tick(FPS)


if __name__ == '__main__':
    GRID = parse(FILE)
    main()
