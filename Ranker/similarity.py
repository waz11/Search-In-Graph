from Graph.vertex import Vertex
from Ranker.matrix import Matrix
from Ranker.sematch.semantic.similarity import WordNetSimilarity


def similarity_names(name1, name2):
    wns = WordNetSimilarity()
    wns.word_similarity('dog', 'cat', 'li')
    # print("Enter two space-separated words")
    # words = input()
    # tokens = nlp(words)
    # for token in tokens:
    #     print(token.text, token.has_vector, token.vector_norm, token.is_oov)
    # token1, token2 = tokens[0], tokens[1]
    # return token1.similarity(token2)



if __name__ == '__main__':
    # v1 = Vertex(1,"yellow","class")
    # v2 = Vertex(1, "blue", "method")
    sim = similarity_names("big", "huge")
    print(sim)