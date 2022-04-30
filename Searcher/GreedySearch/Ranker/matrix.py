class Matrix:

    def __init__(self):
        self.matrix = {}

    def __getitem__(self, types):
        if(len(types) != 2): return 0
        if(types[0] == types[1]): return 1
        if types in self.matrix: return self.matrix[types]
        reversed = types[::-1]
        if reversed in self.matrix: return self.matrix[reversed]
        else: return 0

