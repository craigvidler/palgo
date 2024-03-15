from enum import IntEnum
from config import *


class NodeState(IntEnum):
    UNEXPLORED = 0


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
