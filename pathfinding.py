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
        self.location = (row, col)
        self.x = col * NODESIZE + col * NODEMARGIN
        self.y = row * NODESIZE + row * NODEMARGIN
        self.cost = cost
        self.orig_cost = str(cost)
        self.rect = (self.x, self.y, NODESIZE, NODESIZE)
        self.state = NodeState.UNEXPLORED

    def draw(self, surface):
        pygame.draw.rect(surface, NODECOLORS[self.state], self.rect)
        self.label = font.render(self.orig_cost, True, TEXTCOLORS[self.state])
        surface.blit(self.label, (self.x + XPADDING, self.y + YPADDING))

    def __repr__(self):
        return f'Node {self.location}, cost {self.cost}'

    def __lt__(self, other):
        return self.cost < other.cost
