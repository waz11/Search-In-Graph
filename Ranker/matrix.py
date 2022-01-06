class Matrix:

    def __init__(self):
        self.__Similarity_matrix_vertex = {}
        self.__Similarity_matrix_vertex['class', 'project'] = 0
        self.__Similarity_matrix_vertex['class', 'class'] = 1
        self.__Similarity_matrix_vertex['method', 'method'] = 1
        self.__Similarity_matrix_vertex['class', 'method'] = 0.5

        self.__Similarity_matrix_edge = {}
        self.__Similarity_matrix_edge['implements', 'implements'] = 1
        self.__Similarity_matrix_edge['extends', 'extends'] = 1
        self.__Similarity_matrix_edge['contains', 'contains'] = 1
        self.__Similarity_matrix_edge['method', 'method'] = 1
        self.__Similarity_matrix_edge['implements', 'extends'] = 0.75
        self.__Similarity_matrix_edge['implements', 'contains'] = 0.5
        self.__Similarity_matrix_edge['implements', 'method'] = 0.5
        self.__Similarity_matrix_edge['extends', 'contains'] = 0.5
        self.__Similarity_matrix_edge['extends', 'method'] = 0.5
        self.__Similarity_matrix_edge['contains', 'method'] = 0.5


    def vertex_matrix(self, type1, type2):
        if (type1,type2) in self.__Similarity_matrix_vertex.keys():
            sim = self.__Similarity_matrix_vertex[type1, type2]
        elif (type2,type1) in self.__Similarity_matrix_vertex.keys():
            sim = self.__Similarity_matrix_vertex[type2, type1]
        return sim

    def edge_matrix(self, type1, type2):
        sim = 0.1
        if (type1, type2) in self.__Similarity_matrix_vertex.keys():
            sim = self.__Similarity_matrix_vertex[type1, type2]
        elif (type2, type1) in self.__Similarity_matrix_vertex.keys():
            sim = self.__Similarity_matrix_vertex[type2, type1]
        return sim

def main():
    m = Matrix()
    m.vertex_matrix('class','project')


if __name__ == '__main__':
    main()
