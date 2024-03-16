from enum import IntEnum
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
    def __init__(self, row, col, cost):
        self.row = row
        self.col = col
        self.x = col * NODESIZE + col * NODEMARGIN
        self.y = row * NODESIZE + row * NODEMARGIN
        self.cost = cost
        self.label = font.render(str(cost), True, TEXTCOLOR)
        self.rect = (self.x, self.y, NODESIZE, NODESIZE)
        self.state = NodeState.UNEXPLORED

    @property
    def location(self):
        return (self.row, self.col)

    def draw(self, surface):
        pygame.draw.rect(surface, NODECOLORS[self.state], self.rect)
        surface.blit(self.label, (self.x + XPADDING, self.y + YPADDING))

    def __repr__(self):
        return f'Node {self.location}, cost {self.cost}'

    def __lt__(self, other):
        return self.cost < other.cost


class Search():
    def __init__(self, file, start, end, algo):
        self.graph = self.parse(file)
        self.start = start
        self.end = end
        self.algo = algo(self, start, end)

    def parse(self, file):
        with open(file) as f:
            return [
                [Node(row, col, int(n)) for col, n in enumerate(line)]
                for row, line in enumerate(f.read().splitlines())
            ]

    def neighbors(self, current, maxrow, maxcol):
        r, c = current.row, current.col
        for row, col in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            if 0 <= row <= maxrow and 0 <= col <= maxcol:
                yield Node(row, col, current.cost + self.graph[row][col].cost)

    def step(self):
        try:
            print(next(self.algo))
        except StopIteration:
            pass

    def path(self, node, previous):
        return [node] if node == START else self.path(previous[node], previous) + [node]

    def draw(self):
        panel = pygame.Surface((GRIDWIDTH, GRIDHEIGHT))
        panel.fill(PANELCOLOR)
        for row in self.graph:
            for node in row:
                node.draw(panel)
        screen.blit(panel, (GRIDMARGIN, GRIDMARGIN))
