from algorithm2.Ranker.matrix import Matrix
from algorithm1.Ranker.sematch.semantic.similarity import WordNetSimilarity
import snowballstemmer


class Ranker:
    def __init__(self):
        stemmer = snowballstemmer.stemmer('english')
        self.matrix = Matrix()
        self.wns = WordNetSimilarity()
        stemmer = snowballstemmer.stemmer('english');

    def sim(self, bow1, bow2)->float:
        rank = 0
        if bow1 == bow2:
                rank = self.matrix['full_name']
        else:
            for b1 in bow1:
                for b2 in bow2:
                    rank = 0
                    if b1 == b2:
                        rank = self.matrix['part_name']
                    elif self.stemmer.stemWord(b1) == self.stemmer.stemWord(b2):
                        rank = self.matrix['stemming']
                    else:
                        rank = self.wns.word_similarity(b1,b2)
        score_relevant = 0
        score_irrelevant = 0
        return rank

def main():
    pass


if __name__ == '__main__':
    main()
