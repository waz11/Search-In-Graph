import string
import fasttext
import numpy as np
from scipy import spatial
from scipy.spatial import distance
from Graph.graph import Graph
from Graph.vertex import Vertex
from Parser.codeToGraph.code_to_graph import CodeParser
from Searcher.BeamSearch.model.VectorsDB import VecDB


class WordEmbedding:

    def __init__(self, graph, project_name="src1"):
        self.db = VecDB(project_name)
        self.graph = graph

        if not self.db.is_table_exist():
            self.db.create_table()
            self.load_model()
            self.build_table()

    def load_model(self):
        self.model = fasttext.load_model('./cc.en.300.bin')

    def build_table(self):
        for vertex in self.graph.get_vertices():
            key = vertex.key
            vector = self.model[vertex.name]
            self.db.insert_vector(key, vector)

    def __getitem__(self, item):
        print("ron")
        if(isinstance(item, Vertex)):
            return self.db.get(item.key)
        elif(isinstance(item, int)):
            return self.db.get(item)
        elif(isinstance(item, str)):
            if not self.load_model():
                self.load_model()
            return self.model[item]



    def cossin_distance(self, v1, v2):
        # distance.euclidean(v1, v2)
        return 1.0 - spatial.distance.cosine(v1, v2)

    def euclid(self, v1, v2):
        return distance.euclidean(v1, v2)


def main():
    g = CodeParser('../../../Files/codes/src1').graph
    model = WordEmbedding(g, 'src1')
    v1 = model[1]
    v2 = model[2]


if __name__ == '__main__':
    main()