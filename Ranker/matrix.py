class Matrix:

    def __init__(self):
        self.Similarity_matrix_vertex = {}
        self.Similarity_matrix_vertex['class']['project'] = 0
        self.Similarity_matrix_vertex['project']['class'] = 0
        self.Similarity_matrix_vertex['class']['class'] = 1
        self.Similarity_matrix_vertex['class']['method'] = 0.5
        self.Similarity_matrix_vertex['method']['method'] = 1
        self.Similarity_matrix_vertex['method']['class'] = 0.5

        self.Similarity_matrix_edge = {}
        self.Similarity_matrix_edge['class']['class'] = 1
        self.Similarity_matrix_edge['class']['method'] = 0.5
        self.Similarity_matrix_edge['class']['implements'] = 0.5
        self.Similarity_matrix_edge['class']['extends'] = 0.5

    def vertex_matrix(self, type1, type2) -> int:
        return self.Similarity_matrix_vertex[type1][type2]

    def edge_matrix(self, type1, type2) -> int:
        return self.Similarity_matrix_edge[type1][type2]



