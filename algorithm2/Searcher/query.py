import string

from Graph.graph import Graph
from Parser.tokenizer import Tokenizer

class Query:

    def __init__(self, query:string):
        self.content = query
        self.tokens = self.parse()

    def __str__(self):
        return str(self.content)

    def parse(self):
        tokens = Tokenizer().get_tokens(self.content, rm_stopwords=True)
        filtered = self.remove_java_words(tokens)
        return filtered

    def remove_java_words(self, tokens):
        core_terms = ['class','method','contains','implements']
        filtered = list(filter(lambda t: t not in core_terms, tokens))
        return filtered


def main():
    q = "class list implements class iterable,class list contains class node"
    query = Query(q)



if __name__ == '__main__':
    main()