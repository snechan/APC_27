from collections import deque

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    graph[node] = input("Enter neighbours: ").split()

start = input("Enter starting node: ")

visited = []
queue = deque([start])
visited.append(start)

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)