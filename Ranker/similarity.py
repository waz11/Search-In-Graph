from Graph.vertex import Vertex
from Ranker.matrix import Matrix
from sematch.semantic.similarity import WordNetSimilarity


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


def sim_edges(edge1, edge2):
    m = Matrix()
    sim_types = m.edge_matrix(edge1.type, edge2.type)
    return sim_types

def sim_vertics(vertex1, vertex2):
    m = Matrix()
    sim_types = m.vertex_matrix(vertex1.type, vertex2.type)
    sim_names = similarity_names(vertex1.name, vertex2.name)
    return (sim_types + sim_names) / 2


if __name__ == '__main__':
    # v1 = Vertex(1,"yellow","class")
    # v2 = Vertex(1, "blue", "method")
    similarity_names("big", "huge")
    # print(sim)