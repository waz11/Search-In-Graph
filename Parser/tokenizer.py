import re

from gensim.parsing import PorterStemmer
from gensim.parsing.preprocessing import remove_stopwords

class Tokenizer:

    def get_tokens(self, content, rm_stopwords=False, stem=False):
        p = PorterStemmer()
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
                    word = p.stem(word)
                if not tmp.__contains__(word):
                    tmp.append(word)
        ret = tmp
        return ret


    def __camel_case_split(self, word):
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
        return [m.group(0).lower() for m in matches]

def main():
    t = Tokenizer()
    tokens = t.get_tokens("ronRon")
    print(tokens)


if __name__ == '__main__':
    main()
