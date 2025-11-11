INF = float("inf")

def BellmanFord(graph, V, source):
    dist = [INF] * V
    dist[source] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in graph:
        if dist[u] != INF and dist[u] + w < dist[v]:
            print("This graph contains a negative edge cycle")
            return

    return dist

graph = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

print(BellmanFord(graph, 5, 0))

