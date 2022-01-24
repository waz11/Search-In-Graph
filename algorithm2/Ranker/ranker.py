import string

from Graph.vertex import Vertex
from algorithm2.Ranker.matrix import Matrix
from algorithm1.Ranker.sematch.semantic.similarity import WordNetSimilarity
import snowballstemmer
from algorithm2.Searcher.BOW import get_scores

class Ranker:

    def __init__(self):
        self.matrix = Matrix()
        self.stemmer = snowballstemmer.stemmer('english')
        self.wns = WordNetSimilarity()


    # def sim(self, bow1, bow2)->float:
    #     rank = 0
    #     if bow1 == bow2:
    #             rank = self.matrix['full_name']
    #     else:
    #         for b1 in bow1:
    #             for b2 in bow2:
    #                 rank = 0
    #                 if b1 == b2:
    #                     rank = self.matrix['part_name']
    #                 elif self.stemmer.stemWord(b1) == self.stemmer.stemWord(b2):
    #                     rank = self.matrix['stemming']
    #                 else:
    #                     semantic_sim = self.wns.word_similarity(b1,b2)
    #                     if semantic_sim > 0.5:
    #                         rank = self.wns.word_similarity(b1,b2)
    #     return rank

    def __vertex_semantic_sim(self, vertex1: Vertex, vertex2: Vertex) -> float:
        rank = 0
        for word1 in vertex1.tokens:
            for word2 in vertex2.tokens:
                rank += self.words_sim(word1, word2)
                # print(word1, word2, rank)
        rank /= max(len(vertex1.tokens), len(vertex2.tokens))
        return rank


    def is_candidate_node(self, token: string, vertex: Vertex) -> bool:
        return self.__full_name_matching(token,vertex) or self.__part_name_matching(token,vertex) or self.__stemming_matching(token,vertex) or self.__similar_words_matching(token,vertex)

    def __full_name_matching(self, token: string, vertex: Vertex) -> bool:
        return token == vertex.name

    def __part_name_matching(self, token: string, vertex: Vertex) -> bool:
        for t1 in vertex.tokens:
            if token == t1: return True
        return False

    def __stemming_matching(self, token: string, vertex: Vertex) -> bool:
        for t1 in vertex.tokens:
            if self.stemmer.stemWord(token) == self.stemmer.stemWord(t1): return True
        return False

    def __similar_words_matching(self, token: string, vertex: Vertex) -> bool:
        # for t1 in vertex1.tokens():
        #     for t2 in vertex2.tokens():

        return False

    def get_scores(self, bow_q: list, bow_v: list):
        return get_scores(bow_q, bow_v)


def main():
    v1 = Vertex(1, 'list','class')
    v2 = Vertex(1, 'node', 'class')
    ranker = Ranker()
    ans = ranker.is_candidate_node(v1,v2)
    print(ans)



if __name__ == '__main__':
    main()
