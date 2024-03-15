from heapq import heappop, heappush
from config import *
from pathfinding import Node


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
        return [
            [Node(row, col, int(n)) for col, n in enumerate(line)]
            for row, line in enumerate(f.read().splitlines())
        ]


def draw_grid():
    panel = pygame.Surface((GRIDWIDTH, GRIDHEIGHT))
    panel.fill(PANELCOLOR)
    for row in GRID:
        for node in row:
            node.draw(panel)
    screen.blit(panel, (GRIDMARGIN, GRIDMARGIN))


def dijkstra(grid, start, end):
    pq = [(Node(0, *start))]
    previous = {}

    while pq:
        current = heappop(pq)
        yield current
        if current.location == end:
            yield current, path(end, previous)
            break
        for neighbor in neighbors(current, *end):
            if neighbor.location not in previous:
                previous[neighbor.location] = current.location
                heappush(pq, neighbor)
        clock.tick(FPS)


def path(node, previous):
    return [node] if node == START else path(previous[node], previous) + [node]


def neighbors(current, maxrow, maxcol):
    r, c = current.row, current.col
    for row, col in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if 0 <= row <= maxrow and 0 <= col <= maxcol:
            yield Node(row, col, current.cost + GRID[row][col].cost)


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
