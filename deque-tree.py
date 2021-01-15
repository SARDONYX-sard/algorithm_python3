from collections import deque


def bfs(graph, root):
    distances = {root: 0}
    q = deque([root])
    while q:
        # The oldest seen (but not yet visited) node will be the left most one.
        current = q.popleft()
        for neighbor in graph[current]:
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                # When we see a new node, we add it to the right side of the queue.
                q.append(neighbor)
    return distances


graph1 = {1: [2, 3], 2: [4], 3: [4, 5], 4: [3, 5], 5: []}
print(bfs(graph1, 1))
