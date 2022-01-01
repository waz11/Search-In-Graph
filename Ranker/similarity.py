from nltk.corpus import wordnet


def similarity_names(name1,name2):
    syn1 = wordnet.synsets(name1)[0]
    syn2 = wordnet.synsets(name2)[0]
    sim = syn1.wup_similarity(syn2)
    print(sim)
    return sim

def similarity_type(type1, type2):
    pass

if __name__ == '__main__':
    similarity_names("blue","orange")