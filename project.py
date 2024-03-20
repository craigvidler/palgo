from heapq import heappop, heappush
from config import *
from pathfinding import Node, NodeState


def main(graph, start, end, algo):
    search = algo(graph, start, end)

    while True:
        events()

        try:
            state = next(search)
        except StopIteration:
            pass

        draw(state)
        clock.tick(FPS)


def parse(file):
    with open(file) as f:
        return {
            (row, col): Node(row, col, int(n))
            for row, line in enumerate(f.read().splitlines())
            for col, n in enumerate(line)
        }


def neighbors(graph, node):
    r, c = node.location
    for neighbor in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
        if neighbor in graph:
            yield graph[neighbor]


def get_path(node, start, previous):
    if node == start:
        return set([node])
    else:
        return get_path(previous[node], start, previous) | set([node])


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


def draw(state):
    screen.fill(BKGCOLOR)

    panel = pygame.Surface((GRIDWIDTH, GRIDHEIGHT))
    panel.fill(PANELCOLOR)
    for node in state['graph'].values():

        if node == state['start']:
            node.draw(panel, NodeState.START)
        elif node == state['end']:
            node.draw(panel, NodeState.END)
        elif node == state['current']:
            node.draw(panel, NodeState.CURRENT)
        elif node in state['path']:
            node.draw(panel, NodeState.PATH)
        elif node in state['pq']:
            node.draw(panel, NodeState.QUEUED)
        elif node in state['previous']:
            node.draw(panel, NodeState.VISITED)
        else:
            node.draw(panel, NodeState.UNEXPLORED)
    screen.blit(panel, (GRIDMARGIN, GRIDMARGIN))

    pygame.display.flip()


def dijkstra(graph, start, end):
    pq = [start]
    previous = {}

    while pq:
        current = heappop(pq)
        path = get_path(current, start, previous)
        yield locals()
        if current == end:
            break
        for neighbor in neighbors(graph, current):
            if neighbor not in previous:
                neighbor.cost += current.cost
                previous[neighbor] = current
                heappush(pq, neighbor)
        clock.tick(FPS)


if __name__ == '__main__':
    graph = parse(FILE)
    start, end = graph[START], graph[END]
    main(graph, start, end, dijkstra)
