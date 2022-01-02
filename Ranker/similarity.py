from nltk.corpus import wordnet
from Ranker.matrix import Matrix


def similarity_names(name1, name2):
    syn1 = wordnet.synsets(name1)[0]
    print(syn1)
    syn2 = wordnet.synsets(name2)[0]
    print(syn2)
    sim = syn1.wup_similarity(syn2)
    print(sim)
    return sim


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
    similarity_names("list","list")
