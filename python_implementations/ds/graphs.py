class Graph:
    def __init__(self):
        self.nodes = set()
        self.adjacents = {}

    def insert_edge(self, i, j, cost=0):
        if i not in self.adjacents:
            self.adjacents[i] = {}
        if j not in self.adjacents:
            self.adjacents[j] = {}

        self.nodes.add(i)
        self.nodes.add(j)
        self.adjacents[i][j] = cost
        self.adjacents[j][i] = cost

    def adjacents_of(self, node):
        return self.adjacents[node].keys()

    def cost(self, src, dest):
        return self.adjacents[src][dest]
