from enum import IntEnum
from math import inf
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
        self.f_cost = inf
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
        if ALGO == 'dijkstra':
            return self.cost < other.cost
        else:
            return self.f_cost < other.f_cost

    @property
    def g_cost(self):
        return self.cost

    @g_cost.setter
    def g_cost(self, value):
        self.cost = value


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
        self.search_state['current'].state = NodeState.CURRENT
        self.search_state['end'].state = NodeState.END

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


def manhattan(a, b):
    return abs(sum(a.location) - sum(b.location))


def chebyshev(a, b):
    x1, y1 = a.location
    x2, y2 = b.location
    return max(x2 - x1, y2 - y1)


def a_star(gs, start, end, heuristic=manhattan):
    start.f_cost = heuristic(start, end)
    pq = [start]
    previous = {}

    while pq:
        current = heappop(pq)
        path = gs.path(current, start, previous)
        yield locals()
        if current == end:
            break

        for neighbor in current.neighbors():
            new_g = current.g_cost + neighbor.cost
            # second condition required if heuristic not consistent (as here)
            if neighbor not in previous or new_g < neighbor.g_cost:
                neighbor.g_cost = new_g
                neighbor.f_cost = new_g + heuristic(neighbor, end)
                heappush(pq, neighbor)
                previous[neighbor] = current


algos = {'dijkstra': dijkstra, 'a_star': a_star}
