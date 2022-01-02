import string
from Ranker.similarity import sim_edges


class Edge:
    def __init__(self, type, source, to):
        self.type :string = type
        self.source  = source
        self.to  = to

    def __str__(self):
        return "({},{}):{}".format(self.source.key, self.to.key, self.type)
