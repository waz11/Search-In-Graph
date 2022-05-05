import string
from Graph.vertex import Vertex
from Searcher.BeamSearch.Ranker.matrix import Matrix
import snowballstemmer
import Searcher.BeamSearch.model.BOW as BOW
from Searcher.BeamSearch.model.WordEmbedding import WordEmbedding


class Ranker:

    def __init__(self, vectors):
        self.matrix = Matrix()
        self.stemmer = snowballstemmer.stemmer('english')
        # self.wns = WordNetSimilarity()
        self.model :WordEmbedding = vectors


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
        return BOW.get_scores(bow_q, bow_v)

    def euclidean_distnace_between_vertices(self,vertex1,vertex2):
        vec1 = self.model[vertex1.key]
        vec2 = self.model[vertex2.key]
        return self.model.cossin_distance(vec1, vec2)
