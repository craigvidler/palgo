from enum import IntEnum
from heapq import heappop, heappush
from config import *


class NodeState(IntEnum):
    UNEXPLORED = 0
    CURRENT = 1
    NEIGHBOR = 2
    QUEUED = 3
    VISITED = 4
    PATH = 5
    START = 6
    END = 7


class Node:
    def __init__(self, row, col, cost, graph):
        self.location = (row, col)
        self.x = col * NODESIZE + col * NODEMARGIN
        self.y = row * NODESIZE + row * NODEMARGIN
        self.cost = cost
        self.orig_cost = str(cost)
        self.rect = (self.x, self.y, NODESIZE, NODESIZE)
        self.state = NodeState.UNEXPLORED
        self.graph = graph

    def draw(self, surface):
        pygame.draw.rect(surface, NODECOLORS[self.state], self.rect)
        label = font.render(self.orig_cost, True, TEXTCOLORS[self.state])
        surface.blit(label, (self.x + XPADDING, self.y + YPADDING))

    def neighbors(self):
        r, c = self.location
        for neighbor in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            if neighbor in self.graph:
                yield self.graph[neighbor]

    def __repr__(self):
        return f'Node {self.location}, cost {self.cost}'

    def __lt__(self, other):
        return self.cost < other.cost


class GraphSearch(dict):
    def __init__(self, file, start, end, algo):
        graph = self.parse(file)
        super().__init__(graph)
        self.search = algo(self, graph[start], graph[end])
        self.search_state = None

    def parse(self, file):
        with open(file) as f:
            return {
                (row, col): Node(row, col, int(n), self)
                for row, line in enumerate(f.read().splitlines())
                for col, n in enumerate(line)
            }

    def step(self):
        try:
            self.search_state = next(self.search)
        except StopIteration:
            pass

        for node in self.search_state['previous']:
            node.state = NodeState.VISITED
        for node in self.search_state['path']:
            node.state = NodeState.PATH
        for node in self.search_state['pq']:
            node.state = NodeState.QUEUED

        self.search_state['start'].state = NodeState.START
        self.search_state['end'].state = NodeState.END
        self.search_state['current'].state = NodeState.CURRENT

    def path(self, node, start, previous):
        if node == start:
            return [node]
        else:
            return self.path(previous[node], start, previous) + [node]

    def draw(self, panel):
        for node in self.values():
            node.draw(panel)


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
