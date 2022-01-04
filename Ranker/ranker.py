from Graph.vertex import Vertex
from Parser.tokenizer import Tokenizer
from Ranker.matrix import Matrix
from Ranker.sematch.semantic.similarity import WordNetSimilarity

class Ranker:
    def __init__(self):
        self.__wns = WordNetSimilarity()

    def __words_sim(self, vertex1, vertex2):
        rank = 0
        for word1 in vertex1.tokens:
            for word2 in vertex2.tokens:
                rank += self.__single_pair_word_sim(word1, word2)
                # print(word1, word2, rank)
        rank /= max(len(vertex1.tokens), len(vertex2.tokens))
        return rank


    def __single_pair_word_sim(self, word1, word2):
        wns = WordNetSimilarity()
        if word1==word2:
            sim=1
        else:
            sim = wns.word_similarity(word1, word2)
        return sim

    def __type_sim(self,type1, typ2):
        m = Matrix()
        return m.vertex_matrix(type1, typ2)

    def get_rank(self, vertex1, vertex2):
        word_sim = self.__words_sim(vertex1, vertex2)
        type_sim = self.__type_sim(vertex1.type, vertex2.type)
        return (word_sim + type_sim) / 2



def main():
    v1 = Vertex(1,"listIterator","class")
    v2 = Vertex(1, "list iterator", "method")
    ranker = Ranker()
    sim = ranker.get_rank(v1,v2)
    print(sim)

if __name__ == '__main__':
    main()