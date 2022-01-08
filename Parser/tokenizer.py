import re
from gensim.parsing import PorterStemmer
from gensim.parsing.preprocessing import remove_stopwords

class Tokenizer:

    def __init__(self):
        self.p = PorterStemmer()

    def get_tokens(self, content, rm_stopwords=False, stem=False)->set:
        tokens: set = {}
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
        ret = tmp
        if len(ret) > 0:
            tokens = set(ret)
        return tokens

    def __camel_case_split(self, word)->list:
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)
        return [m.group(0).lower() for m in matches]

def main():
    t = Tokenizer("list_iterable")
    print(t.tokens)


if __name__ == '__main__':
    main()
