from Searcher.GreedySearch.Ranker.matrix import Matrix
from Graph.vertex import VertexTypeEnum


class VerticesSimilarityMatrix(Matrix):

    def __init__(self):
        super().__init__()

        CLASS = VertexTypeEnum.CLASS
        METHOD = VertexTypeEnum.METHOD
        INTERFACE = VertexTypeEnum.INTERFACE

        # self.matrix[CLASS, 'abstract'] = 0.7
        self.matrix[CLASS, METHOD] = 0.8
        self.matrix[CLASS, INTERFACE] = 0.7
        self.matrix[METHOD, INTERFACE] = 0.5

