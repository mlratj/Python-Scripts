class Edges(object):
    # creates two lists for connections
    def __init__(self, source):
        self.x = source
        print(f"The source for this exercise is: {source}")


    def operation_lists(self):
        with open(self.x, "r") as f:
            splitted = [line.split() for line in f]
            firstline = splitted[0]
            no_nodes = int(firstline[0])
            no_connections = firstline[1]
            print(f"The number of nodes is: {no_nodes}")
            print(f"The number of connections is: {no_connections}")
            neighbours = splitted[1:]
            first_edge = []
            second_edge = []
            for l, k in neighbours:
                first_edge.append(int(l))
                second_edge.append(int(k))

        adj_list = [[] for k in range(no_nodes)]

        for i in range(len(first_edge)):
            u = first_edge[i]
            v = second_edge[i]
            adj_list[u].append(v)
        for k in range(len(adj_list)-1):
            print(k, ":", adj_list[k])

        return "Success!"


if __name__ == '__main__':
    a = Edges("dane.txt")
    print(a.operation_lists())