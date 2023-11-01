class Edge:
    def __init__(self, source, dest, cost=0):
        self.source = source
        self.dest = dest
        self.cost = cost


class Graph:
    def __init__(self):
        self.nodes = set()
        self.adjacents = {}

    @property
    def number_of_nodes(self):
        return len(self.nodes)

    @property
    def edges(self):
        _edges = []
        for src in self.adjacents:
            for dest, cost in self.adjacents[src].items():
                _edges.append(Edge(src, dest, cost))

        return _edges

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
