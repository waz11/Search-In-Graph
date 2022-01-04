from Graph.vertex import Vertex
from Ranker.matrix import Matrix
from Ranker.sematch.semantic.similarity import WordNetSimilarity

class Ranker:
    def __init__(self):
        self.__wns = WordNetSimilarity()

    def __word_sim(self,word1, word2):
        wns = WordNetSimilarity()
        sim = wns.word_similarity(word1, word2)
        return sim

    def __type_sim(self,type1, typ2):
        m = Matrix()
        return m.vertex_matrix(type1, typ2)

    def get_rank(self, vertex1, vertex2):
        word_sim = self.__word_sim(vertex1.name, vertex2.name)
        type_sim = self.__type_sim(vertex1.type, vertex2.type)
        return (word_sim + type_sim) / 2



def main():
    v1 = Vertex(1,"yellow","class")
    v2 = Vertex(1, "blue", "method")
    ranker = Ranker()
    rank = ranker.get_rank(v1,v2)
    print(rank)


if __name__ == '__main__':
    main()