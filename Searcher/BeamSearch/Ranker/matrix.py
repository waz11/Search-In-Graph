class Matrix:

    def __init__(self):
        self.__similarity_vertex = {}
        self.__similarity_vertex['full_name'] = 1
        self.__similarity_vertex['partial_name'] = 1
        self.__similarity_vertex['stemming'] = 1
        self.__similarity_vertex['abbreviation'] = 1

    def get_sim(self, obj1,obj2):
        pass


    def __getitem__(self, item):
        sim = 0
        if item in self.__similarity_vertex:
            sim = self.__similarity_vertex[item]
        return sim

def main():
    m = Matrix()
    x = m['full_name']
    print(x)


if __name__ == '__main__':
    main()
