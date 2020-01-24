class Edges(object):
    # creates two lists for connections
    def __init__(self, source):
        self.x = source
        print(f"The source for this exercise is: {source}")


    def operation_neighbours(self):
        with open(self.x, "r") as f:
            splitted = [line.split() for line in f]
            no_nodes = splitted[0]
            print(f"The number of nodes is: {no_nodes}")
        for sub in splitted[1:]:
            for i in sub:
                for x in range(0, len(sub)):
                    sub[x] = int(sub[x])
        list_of_neighbours = splitted[1:]
        return list_of_neighbours

    def operation_dict(self, neigh):
        taken_nums = []
        adj_dict = {}
        for i in neigh:
            x = i[0]
            temp_list = set()
            if x not in taken_nums:
                taken_nums.append(x)
                for line in neigh:
                    while x == line[0]:
                        temp_list.add(line[1])
                        break
                    adj_dict[x] = temp_list
        return adj_dict

    def dfs_alg(self, graph, starting_node, visited=None, queue=None):
        if visited is None:
            visited = set()
        if queue is None:
            queue = []
        visited.add(starting_node)
        if starting_node not in queue:
            queue.append(starting_node)
        for next in graph[starting_node] - visited:
            self.dfs_alg(graph, next, visited, queue)
        return queue

if __name__ == '__main__':
    a = Edges("text.txt")
    b = a.operation_neighbours()
    l = a.operation_dict(b)
    n = str(a.dfs_alg(l, 0))
    print(f'Queue is {n}')
