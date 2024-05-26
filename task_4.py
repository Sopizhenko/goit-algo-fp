import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
	def __init__(self, key, color="skyblue"):
		self.left = None
		self.right = None
		self.val = key
		self.color = color
		self.id = str(uuid.uuid4())

def add_edges_heap(graph, node, pos, x=0, y=0, layer=1):
	if node is not None:
		graph.add_node(node.id, color=node.color, label=node.val)
		if node.left:
			graph.add_edge(node.id, node.left.id)
			l = x - 1 / 2 ** layer
			pos[node.left.id] = (l, y - 1)
			l = add_edges_heap(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
		if node.right:
			graph.add_edge(node.id, node.right.id)
			r = x + 1 / 2 ** layer
			pos[node.right.id] = (r, y - 1)
			r = add_edges_heap(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
	return graph

def draw_heap(heap_root):
	heap = nx.DiGraph()
	pos = {heap_root.id: (0, 0)}
	heap = add_edges_heap(heap, heap_root, pos)

	colors = [node[1]['color'] for node in heap.nodes(data=True)]
	labels = {node[0]: node[1]['label'] for node in heap.nodes(data=True)}

	plt.figure(figsize=(8, 5))
	nx.draw(heap, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
	plt.show()

def build_heap(array):
	heap = []
	for element in array:
		heapq.heappush(heap, element)
	root = HeapNode(heapq.heappop(heap))
	for element in heap:
		insert(root, element)
	return root

def insert(node, value):
	if node.left is None:
		node.left = HeapNode(value)
	elif node.right is None:
		node.right = HeapNode(value)
	elif node.left is not None and node.right is not None:
		if node.left.val > node.right.val:
			insert(node.right, value)
		else:
			insert(node.left, value)


if __name__ == "__main__":
	array = [3, 7, 1, 4, 10, 2, 8]
	heap_root = build_heap(array)
	draw_heap(heap_root)