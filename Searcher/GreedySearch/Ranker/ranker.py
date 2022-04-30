import string
from Graph.vertex import Vertex, VertexTypeEnum
from Searcher.GreedySearch.Ranker.EdgesSimilarityMatrix import EdgesSimilarityMatrix
from Searcher.GreedySearch.Ranker.VerticesSimilarityMatrix import VerticesSimilarityMatrix
from Searcher.GreedySearch.Ranker.sematch.semantic.similarity import WordNetSimilarity


class Ranker:
    def __init__(self):
        self.wns = WordNetSimilarity()
        self.VerticesSimilarityMatrix = VerticesSimilarityMatrix()
        self.EdgesSimilarityMatrix = EdgesSimilarityMatrix()

    def semantic_sim(self, vertex1:Vertex, vertex2:Vertex)->float:
        rank = 0
        for word1 in vertex1.tokens:
            for word2 in vertex2.tokens:
                rank += self.words_sim(word1, word2)
        rank /= max(len(vertex1.tokens), len(vertex2.tokens))
        return rank

    def types_sim(self, type1 :VertexTypeEnum, typ2 :VertexTypeEnum)->float:
        m = VerticesSimilarityMatrix()
        return m[type1, typ2]

    def get_vertices_rank(self, vertex1:Vertex, vertex2:Vertex)->float:
        sim = 0
        word_sim = self.semantic_sim(vertex1, vertex2)
        type_sim = self.types_sim(vertex1.type, vertex2.type)
        sim = (word_sim + type_sim) / 2
        return sim

    def words_sim(self, word1: string, word2: string) -> float:
        if word1 == word2: sim = 1
        else: sim = self.wns.word_similarity(word1, word2)
        return sim



if __name__ == '__main__':
    # v1 = Vertex(1, "listIterator", "class")
    # v2 = Vertex(1, "list iterator", "class")
    # v3 = Vertex(1, "list iterator", "method")
    # ranker = Ranker()
    # sim1 = ranker.get_rank(v1, v2)
    # sim2 = ranker.get_rank(v1, v3)
    # print(sim1, sim2)

    ranker = Ranker()
    x = ranker.wns.word_similarity('remove', 'delete')
    print(x)
    x = ranker.wns.word_similarity('high', 'low')
    print(x)
