class Edges(object):
    # creates two lists for connections
    def __init__(self, source):
        self.x = source
        print(f"The source for this exercise is: {source}")

    def decompose(self):
        with open(self.x, "r") as f:
            splitted = [line.split() for line in f]
            first_line = splitted[0]
            matrix_size = int(first_line[0])
            print(f"The number of nodes is: {matrix_size}")
            edges = []
            for sub in splitted[1:]:
                for i in sub:
                    if int(i) not in edges:
                        edges.append(int(i))
            edges.sort()
            return edges

    def list_of_neighbours(self):
        with open(self.x, "r") as f:
            neigh_only = [line.split() for line in f]
            # converting strings to integers
            for sub in neigh_only:
                for i in sub:
                    for x in range(0, len(sub)):
                        sub[x] = int(sub[x])
            list_of_neighbours = neigh_only[1:]
            return list_of_neighbours

    def list_to_dict(lst):
        res_dct = {}
        for sub in lst:
            res_dct.update({sub[0]: sub[1:]})
        return res_dct

    def matrix(self):
        import numpy as np
        e = Edges.decompose(self) # all nodes
        neigh = Edges.list_of_neighbours(self)
        empty_array = np.zeros((len(e), len(e)), dtype=int)
        res_dct = Edges.list_to_dict(neigh)
        full_array = empty_array
        for key in res_dct:
            for value in res_dct[key]:
                full_array[key][value] = int(1)
                full_array[key][value] = int(1)
        print(' ', *e, sep = ' ')
        for i in range(len(e)):
            x = full_array[i]
            print(i, *x, sep =' ')

if __name__ == '__main__':
    a = Edges("text.txt")
    a.matrix()