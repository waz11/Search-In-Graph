import fasttext
from scipy import spatial
from Parser.codeToGraph.code_to_graph import CodeParser
from Searcher.BeamSearch.model.VectorsDB import VecDB


class WordEmbedding:

    def __init__(self, graph, project_name="src"):
        self.db = VecDB(project_name)
        self.graph = graph
        self.model = fasttext.load_model('./cc.en.300.bin')
        print("ok!")

    def build_table(self):
        for vertex in self.graph.get_vertices():
            key = vertex.key
            vector = self.model[vertex.name]
            self.db.insert_vector(key, vector)

    def euclid_distance(self, v1, v2):
        # distance.euclidean(v1, v2)
        return 1.0 - spatial.distance.cosine(v1, v2)


def main():
    g = CodeParser('../../../Files/codes/src1').graph
    model = WordEmbedding(g, 'src1')

    # g.print_vertices()
    # v1 = model[2]
    # v2 = model[1]
    # d = model.euclid_distance(v1, v2)
    # print(d)


if __name__ == '__main__':
    main()