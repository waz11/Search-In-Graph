from nltk.corpus import wordnet
from matrix import Matrix

def similarity_names(name1,name2):
    syn1 = wordnet.synsets(name1)[0]
    syn2 = wordnet.synsets(name2)[0]
    sim = syn1.wup_similarity(syn2)
    print(sim)
    return sim


def sim_edges(edge1, edge2):
    m = Matrix()
    sim_types =  m.edge_matrix(type1, type2)




if __name__ == '__main__':
    similarity_names("blue","orange")