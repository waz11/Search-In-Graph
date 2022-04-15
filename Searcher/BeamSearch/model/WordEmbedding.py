import os

import fasttext
import numpy
from scipy import spatial
from scipy.spatial import distance
from Graph.vertex import Vertex
from Parser.codeToGraph.code_to_graph import CodeParser
from Searcher.BeamSearch.model.VectorsDB import VectorsDB


class WordEmbedding:

    def __init__(self, graph, project_name="src1"):
        self.project_name = project_name
        self.db = VectorsDB()
        self.graph = graph

        if not self.db.is_table_exist(project_name):
            self.db.create_table(project_name)
            self.load_model()
            self.build_table()

    def load_model(self):
        print("loading model")
        self.model = fasttext.load_model('cc.en.300.bin')

    def build_table(self):
        for vertex in self.graph.get_vertices():
            key = vertex.key
            vector = self.model[vertex.name]
            self.db.insert_vector(self.project_name, key, vector)

    def __getitem__(self, item):
        if(isinstance(item, Vertex)):
            item = item.key
        elif(isinstance(item, str)):
            if not self.load_model():
                self.load_model()
            return self.model[item]
        return self.db.get(self.project_name, item)



    def cossin_distance(self, v1, v2):
        # distance.euclidean(v1, v2)
        return 1.0 - spatial.distance.cosine(v1, v2)

    def euclid(self, v1, v2):
        if isinstance(v1,numpy.ndarray):
            return distance.euclidean(v1, v2)
        if(isinstance(v1,Vertex) and isinstance(v2,Vertex)):
            print(v1.key, v2.key)
            v1 = self.__getitem__(v1)
            v2 = self.__getitem__(v2)
            return distance.euclidean(v1, v2)



def main():
    g = CodeParser('../../../Files/codes/src1').graph
    model = WordEmbedding(g, 'src1')
    # model.db.print_table("src1")
    print(os.getcwd())



if __name__ == '__main__':
    main()