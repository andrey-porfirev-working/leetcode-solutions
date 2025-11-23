def minReorder(self, n: int, connections: List[List[int]]) -> int:
    # Создаём граф
    roads = [[] for _ in range(n)]

    for a, b in connections:
        roads[a].append((b, 1))
        roads[b].append((a, 0))

    stack = [0]
    visited = [False] * n
    visited[0] = True
    changes = 0

    while stack:
        city = stack.pop()

        # Смотрим всех соседей
        for neighbor, direction in roads[city]:
            if not visited[neighbor]:
                visited[neighbor] = True
                changes += direction
                stack.append(neighbor)

    return changes