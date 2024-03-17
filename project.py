from heapq import heappop, heappush
from config import *
from pathfinding import Node, NodeState, Search


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


def update(search):
    search.step()


def draw(search):
    screen.fill(BKGCOLOR)
    search.draw()
    pygame.display.flip()


def dijkstra(search, start, end):
    pq = [(Node(0, *start))]
    previous = {}

    while pq:
        current = heappop(pq)
        yield current
        current.state = NodeState.CURRENT
        search.graph[current.location].state = NodeState.CURRENT
        if current.location == end:
            yield current, search.path(end, previous)
            break
        for neighbor in search.neighbors(*current.location):
            if neighbor.location not in previous:
                neighbor.cost += current.cost
                previous[neighbor.location] = current.location
                heappush(pq, neighbor)
        clock.tick(FPS)


def main(search):
    while True:
        events()
        update(search)
        draw(search)
        clock.tick(FPS)


if __name__ == '__main__':
    search = Search(FILE, START, END, dijkstra)
    main(search)
