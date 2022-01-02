import re

from gensim.parsing import PorterStemmer
from gensim.parsing.preprocessing import remove_stopwords
from nltk.corpus import wordnet

class Tokenizer:

    def __init__(self, content):
        self.p = PorterStemmer()
        self.tokens :set = {}
        self.synonyms :set = {}
        self.__add_tokens(content)
        self.__add_synonyms()

    def __add_tokens(self, content, rm_stopwords=False, stem=False):
        words = re.split('[^A-Za-z]+', content)
        ret = []
        for word in words:
            ret += self.__camel_case_split(word)
        tmp = []
        for word in ret:
            if rm_stopwords:
                word = remove_stopwords(word)
            if len(word) > 0:
                if stem:
                    word = self.p.stem(word)
                if not tmp.__contains__(word):
                    tmp.append(word)
        if len(ret) > 0:
            self.tokens = set(ret)


    def __camel_case_split(self, word):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
        return [m.group(0).lower() for m in matches]

    def __add_synonyms(self):
        synonyms = []
        for token in self.tokens:
            for syn in wordnet.synsets(token):
                for l in syn.lemmas():
                    synonyms.append(l.name())
        if len(synonyms) != 0:
            self.synonyms = set(synonyms)


def main():
    t = Tokenizer("")
    print(t.tokens)
    print(t.synonyms)



if __name__ == '__main__':
    main()
