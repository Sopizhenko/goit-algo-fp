from task_4 import build_heap
import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, node, pos, x=0, y=0, layer=1):
	if node is not None:
		graph.add_node(node.id, label=node.val)
		if node.left:
			graph.add_edge(node.id, node.left.id)
			l = x - 1 / 2 ** layer
			pos[node.left.id] = (l, y - 1)
			add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
		if node.right:
			graph.add_edge(node.id, node.right.id)
			r = x + 1 / 2 ** layer
			pos[node.right.id] = (r, y - 1)
			add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root, traversal_order):
	tree = nx.DiGraph()
	pos = {tree_root.id: (0, 0)}
	add_edges(tree, tree_root, pos)

	colors = []
	labels = {}
	if traversal_order == "DFS":
		DFS(tree_root, colors, labels)
	elif traversal_order == "BFS":
		BFS(tree_root, colors, labels)

	plt.figure(figsize=(8, 5))
	nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
	plt.show()

def DFS(node, colors, labels, depth=1):
	if node:
		color = generate_color(depth)
		colors.append(color)
		labels[node.id] = node.val
		DFS(node.left, colors, labels, depth + 1)
		DFS(node.right, colors, labels, depth + 1)

def BFS(root, colors, labels):
	if not root:
		return
	queue = [(root, 1)]
	while queue:
		node, depth = queue.pop(0)
		color = generate_color(depth)
		colors.append(color)
		labels[node.id] = node.val
		if node.left:
			queue.append((node.left, depth + 1))
		if node.right:
			queue.append((node.right, depth + 1))

def generate_color(depth):
	# Генерувати RGB-колір від темного до світлого на основі глибини
	red = format(255 - int(255 * depth / 5), '02x')
	green = format(255 - int(255 * depth / 5), '02x')
	blue = format(255 - int(255 * depth / 5), '02x')
	return f'#{red}{green}{blue}'


# Приклад використання
array = [3, 7, 1, 4, 10, 2, 8]
heap_root = build_heap(array)

# Відображення дерева у глибину (DFS)
draw_tree(heap_root, "DFS")

# Відображення дерева у ширину (BFS)
draw_tree(heap_root, "BFS")