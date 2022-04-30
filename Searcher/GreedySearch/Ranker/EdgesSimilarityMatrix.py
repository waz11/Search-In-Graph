from Searcher.GreedySearch.Ranker.matrix import Matrix
from Graph.edge import EdgeTypeEnum


class EdgesSimilarityMatrix(Matrix):
    def __init__(self):
        super().__init__()

        IMPLEMENTS = EdgeTypeEnum.IMPLEMENTS
        EXTENDS = EdgeTypeEnum.EXTENDS
        CONTAINS = EdgeTypeEnum.CONTAINS
        METHOD = EdgeTypeEnum.METHOD

        self.matrix[IMPLEMENTS, EXTENDS] = 0.75
        self.matrix[IMPLEMENTS, CONTAINS] = 0.5
        self.matrix[IMPLEMENTS, METHOD] = 0.5
        self.matrix[EXTENDS, CONTAINS] = 0.5
        self.matrix[EXTENDS, METHOD] = 0.5
        self.matrix[CONTAINS, METHOD] = 0.5
