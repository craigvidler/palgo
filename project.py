from heapq import heappop, heappush
from config import *
from pathfinding import Node, NodeState


def main():
    graph = parse(FILE)
    algo = dijkstra
    search = algo(graph, graph[START], graph[END])

    while True:
        events()

        try:
            state = next(search)
        except StopIteration:
            pass

        update(state)
        draw(graph)
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


def draw(graph):
    screen.fill(BKGCOLOR)
    panel = pygame.Surface((GRIDWIDTH, GRIDHEIGHT))
    panel.fill(PANELCOLOR)

    for node in graph.values():
        node.draw(panel)

    screen.blit(panel, (GRIDMARGIN, GRIDMARGIN))
    pygame.display.flip()


def update(state):
    for node in state['previous']:
        node.state = NodeState.VISITED
    for node in state['path']:
        node.state = NodeState.PATH
    for node in state['pq']:
        node.state = NodeState.QUEUED

    state['start'].state = NodeState.START
    state['end'].state = NodeState.END
    state['current'].state = NodeState.CURRENT


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


if __name__ == '__main__':
    main()
