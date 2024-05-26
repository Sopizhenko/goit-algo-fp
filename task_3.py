import heapq

def dijkstra(graph, start):
	# Ініціалізація відстаней
	distances = {vertex: float('infinity') for vertex in graph}
	distances[start] = 0
	
	# Ініціалізація черги з пріоритетами
	priority_queue = [(0, start)]
	
	while priority_queue:
		# Вибір вершини з найменшою відстанню
		current_distance, current_vertex = heapq.heappop(priority_queue)
		
		# Якщо поточна відстань більша за найкоротшу відстань, ігноруємо її
		if current_distance > distances[current_vertex]:
			continue
		
		# Перегляд сусідів поточної вершини
		for neighbor, weight in graph[current_vertex].items():
			distance = current_distance + weight
			# Якщо нова відстань коротша за поточну
			if distance < distances[neighbor]:
				distances[neighbor] = distance
				heapq.heappush(priority_queue, (distance, neighbor))
	
	return distances

# Приклад графа
graph = {
	'A': {'B': 1, 'C': 4},
	'B': {'A': 1, 'C': 2, 'D': 5},
	'C': {'A': 4, 'B': 2, 'D': 1},
	'D': {'B': 5, 'C': 1}
}

# Початкова вершина
start_vertex = 'A'

# Знаходження найкоротших шляхів
shortest_paths = dijkstra(graph, start_vertex)

print("Найкоротші шляхи від вершини", start_vertex)
for vertex, distance in shortest_paths.items():
	print(f"Від {start_vertex} до {vertex}: {distance}")
