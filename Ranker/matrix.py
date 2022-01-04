class Matrix:

    def __init__(self):
        self.Similarity_matrix_vertex = {}
        self.Similarity_matrix_vertex['class','project'] = 0
        self.Similarity_matrix_vertex['class','class'] = 1
        self.Similarity_matrix_vertex['method','method'] = 1
        self.Similarity_matrix_vertex['class','method'] = 0.5

        self.Similarity_matrix_edge = {}
        self.Similarity_matrix_edge['implements','implements'] = 1
        self.Similarity_matrix_edge['extends', 'extends'] = 1
        self.Similarity_matrix_edge['contains', 'contains'] = 1
        self.Similarity_matrix_edge['method', 'method'] = 1
        self.Similarity_matrix_edge['implements', 'extends'] = 0.75
        self.Similarity_matrix_edge['implements', 'contains'] = 0.5
        self.Similarity_matrix_edge['implements', 'method'] = 0.5
        self.Similarity_matrix_edge['extends','contains'] = 0.5
        self.Similarity_matrix_edge['extends','method'] = 0.5
        self.Similarity_matrix_edge['contains','method'] = 0.5


    def vertex_matrix(self, type1, type2):
        if (type1,type2) in self.Similarity_matrix_vertex.keys():
            sim = self.Similarity_matrix_vertex[type1,type2]
            print(type1,type2, "in1")
        elif (type2,type1) in self.Similarity_matrix_vertex.keys():
            sim = self.Similarity_matrix_vertex[type2,type1]
            print(type2,type1, "in2")
        # print(sim)
        return sim

    def edge_matrix(self, type1, type2):
        sim = 0.1
        if (type1, type2) in self.Similarity_matrix_vertex.keys():
            sim = self.Similarity_matrix_vertex[type1, type2]
        elif (type2, type1) in self.Similarity_matrix_vertex.keys():
            sim = self.Similarity_matrix_vertex[type2, type1]
        return sim

def main():
    m = Matrix()
    m.vertex_matrix('class','project')


if __name__ == '__main__':
    main()
