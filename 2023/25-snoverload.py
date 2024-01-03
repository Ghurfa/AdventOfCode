import copy

def get_shortest_path(graph, start, end, deleted_edges):
    queue = [start]
    parents = { start: None }
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == end:
            path_walker = curr
            path = []
            while path_walker:
                path.append(path_walker)
                path_walker = parents[path_walker]
            return path
        neighbors = graph[curr]
        for neigh in neighbors:
            if (curr, neigh) in deleted_edges:
                continue
            if neigh in parents:
                continue
            parents[neigh] = curr
            queue.append(neigh)
    return None

def is_reachable_n_ways(graph, start, end, n):
    deleted_edges = set()
    for _ in range(0, n):
        path = get_shortest_path(graph, start, end, deleted_edges)
        if path == None:
            return False
        for i, node in enumerate(path[:-1]):
            edge = (node, path[i + 1])
            rev_edge = (edge[1], edge[0])
            deleted_edges.add(edge)
            deleted_edges.add(rev_edge)
    return True

def main():
    raw_graph = {}
    with open("25-input.txt", encoding='UTF-8') as file:
        for line in file:
            name, connections_str = line.strip().split(':')
            connections = connections_str.strip().split(' ')
            raw_graph[name] = connections

    # Convert to undirected graph

    graph = copy.deepcopy(raw_graph)
    for node in raw_graph:
        for edge in raw_graph[node]:
            if edge in graph:
                graph[edge].append(node)
            else:
                graph[edge] = [node]

    nodes = [x for x in graph]

    # Commented code was used on test-input to verify that is_reachable_4_ways is an equivalence relation

    # relation_matrix = [[False] * len(nodes) for _ in range(0, len(nodes))]
    # for i, node_a in enumerate(nodes):
    #     for j, node_b in enumerate(nodes):
    #         relation_matrix[i][j] = is_reachable_n_ways(graph, node_a, node_b, 4)
    
    # for x in relation_matrix:
    #     c = [1 if m else 0 for m in x]
    #     print(c)
    
    group_a = [nodes[0]]
    group_b = []

    for node in nodes[1:]:
        if is_reachable_n_ways(graph, nodes[0], node, 4):
            group_a.append(node)
        else:
            group_b.append(node)
    print(f'Group A size: {len(group_a)}')
    print(f'Group B size: {len(group_b)}')
    print(f'Answer: {len(group_a) * len(group_b)}')

if __name__ == "__main__":
    main()
