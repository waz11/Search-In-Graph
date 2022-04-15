import math

from Graph.vertex import Vertex

def getDelta(model, c:Vertex, v:Vertex) ->float:
    delta = model.euclid(c, v)
    return delta

class Group:
    def __init__(self, vertex:Vertex):
        self.vertices = set()
        self.vertices.add(vertex)
        self.cost = 0

    def __len__(self):
        return len(self.vertices)

    def select_candidate(self, candidates:list, model):
        min_delta = math.inf
        selected_candidate = None
        for c in candidates:
            delta = 0
            for v in self.vertices:
                delta += getDelta(model, c, v)
            if delta < min_delta:
                min_delta = delta
                selected_candidate = c
        self.cost += min_delta
        self.vertices.add(selected_candidate)
        return selected_candidate
