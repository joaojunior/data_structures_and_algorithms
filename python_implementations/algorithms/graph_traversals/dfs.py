NOT_DISCOVERED, NOT_STARTED, STARTED, FINISHED = -1, 0, 1, 2


def dfs(graph):
    order_nodes_visited = []
    status = {}
    for node in graph.nodes:
        status[node] = NOT_DISCOVERED

    for node in graph.nodes:
        if status[node] == NOT_DISCOVERED:
            nodes_to_process = [node]
            while nodes_to_process:
                node = nodes_to_process.pop()
                status[node] = STARTED
                order_nodes_visited.append(node)
                for adjacent in sorted(graph.adjacents_of(node), reverse=True):
                    if status[adjacent] == NOT_DISCOVERED:
                        status[adjacent] = NOT_STARTED
                        nodes_to_process.append(adjacent)
                status[node] = FINISHED
    return order_nodes_visited
