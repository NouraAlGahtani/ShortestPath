import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances[end]

graph = {
    'A': {'B': 11, 'C': 10},
    'B': {'A': 0, 'D': 21},
    'C': {'A': 10, 'D': 13},
    'E': {'B': 20, 'C': 1, 'D': 21},
    'D': {'D': 5, 'F': 3},
    'F': {'E': 3, 'G': 2},
    'G': {'F': 2}
}

start = "A"
end = "G"

shortest_distance = dijkstra(graph, start, end)

print(f"The shortest distance from {start} to {end} is {shortest_distance}")