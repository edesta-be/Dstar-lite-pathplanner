import math
from typing import List


class Vertex:
    def __init__(self, pos: (int, int, int)):
        self.pos = pos
        self.edges_and_costs = {}

    def add_edge_with_cost(self, succ: (int, int, int), cost: float):
        if succ != self.pos:
            self.edges_and_costs[succ] = cost

    @property
    def edges_and_c_old(self):
        return self.edges_and_costs


class Vertices:
    def __init__(self):
        self.list = []

    def add_vertex(self, v: Vertex):
        self.list.append(v)

    @property
    def vertices(self):
        return self.list


def heuristic(p: (int, int, int), q: (int, int, int)) -> float:
    """
    Helper function to compute distance between two points.
    :param p: (x,y,z)
    :param q: (x,y,z)
    :return: manhattan distance
    """
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)

def midvertex(p: (int, int, int), q: (int, int, int)):
    return (round((p[0]+q[0])/2), round((p[1]+q[1])/2), round((p[2]+q[2])/2))

def get_movements_4n(x: int, y: int, z: int) -> List:
    """
    get all possible 4-connectivity movements.
    :return: list of movements with cost [(dx, dy, movement_cost)]
    """
    return [(x + 1, y + 0, z + 0),
            (x + 0, y + 1, z + 0),
            (x - 1, y + 0, z + 0),
            (x + 0, y - 1, z + 0)]

def get_movements_8n(x: int, y: int, z: int) -> List:
    """
    get all possible 8-connectivity movements.
    :return: list of movements with cost [(dx, dy, movement_cost)]
    """
    return [(x + 1, y + 0, z + 0),
            (x + 0, y + 1, z + 0),
            (x - 1, y + 0, z + 0),
            (x + 0, y - 1, z + 0),
            (x + 1, y + 1, z + 0),
            (x - 1, y + 1, z + 0),
            (x - 1, y - 1, z + 0),
            (x + 1, y - 1, z + 0)]

def get_movements_26n(x: int, y: int, z: int) -> List:
    """
    get all possible 8-connectivity movements.
    :return: list of movements with cost [(dx, dy, dz, movement_cost)]
    """
    return [(x + 0, y + 0, z - 1),
            (x + 0, y + 0, z + 1),
            (x + 0, y - 1, z + 0),
            (x + 0, y - 1, z - 1),
            (x + 0, y - 1, z + 1),
            (x + 0, y + 1, z + 0),
            (x + 0, y + 1, z - 1),
            (x + 0, y + 1, z + 1),
            (x - 1, y + 0, z + 0),
            (x - 1, y + 0, z - 1),
            (x - 1, y + 0, z + 1),
            (x - 1, y - 1, z + 0),
            (x - 1, y - 1, z - 1),
            (x - 1, y - 1, z + 1),
            (x - 1, y + 1, z + 0),
            (x - 1, y + 1, z - 1),
            (x - 1, y + 1, z + 1), 
            (x + 1, y + 0, z + 0), 
            (x + 1, y + 0, z - 1), 
            (x + 1, y + 0, z + 1), 
            (x + 1, y - 1, z + 0), 
            (x + 1, y - 1, z - 1), 
            (x + 1, y - 1, z + 1), 
            (x + 1, y + 1, z + 0), 
            (x + 1, y + 1, z - 1), 
            (x + 1, y + 1, z + 1)]
