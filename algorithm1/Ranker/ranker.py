import string

from Graph.vertex import Vertex
from algorithm1.Ranker.matrix import Matrix
from algorithm1.Ranker.sematch.semantic.similarity import WordNetSimilarity


class Ranker:
    def __init__(self):
        self.wns = WordNetSimilarity()

    def __vertex_semantic_sim(self, vertex1:Vertex, vertex2:Vertex)->float:
        rank = 0
        for word1 in vertex1.tokens:
            for word2 in vertex2.tokens:
                rank += self.words_sim(word1, word2)
                # print(word1, word2, rank)
        rank /= max(len(vertex1.tokens), len(vertex2.tokens))
        return rank



    def __type_sim(self, type1:string, typ2:string)->float:
        m = Matrix()
        return m.vertex_matrix(type1, typ2)

    def get_rank(self, vertex1:Vertex, vertex2:Vertex)->float:
        sim = word_sim = self.__vertex_semantic_sim(vertex1, vertex2)
        if len(vertex1.type) > 0 and len(vertex2.type) > 0:
            type_sim = self.__type_sim(vertex1.type, vertex2.type)
            sim = (word_sim + type_sim) / 2
        return sim

    @staticmethod
    def words_sim(word1: string, word2: string) -> float:
        wns = WordNetSimilarity()
        if word1 == word2:
            sim = 1
        else:
            sim = wns.word_similarity(word1, word2)
        return sim

def main():
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

if __name__ == '__main__':
    main()
