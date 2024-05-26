import random

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def reverse(self):
		prev = None
		current = self.head
		while current is not None:
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def sorted_insert(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		if self.head.data >= data:
			new_node.next = self.head
			self.head = new_node
			return
		current = self.head
		while current.next is not None and current.next.data < data:
			current = current.next
		new_node.next = current.next
		current.next = new_node


	def print_list(self):
		current = self.head
		while current is not None:
			print(current.data, end = " ")
			current = current.next
		print()

# Сортування однозв'язного списку вставкою
def sorted_insert(head, data):
	new_node = Node(data)
	if head is None:
		head = new_node
		return head
	if head.data >= data:
		new_node.next = head
		head = new_node
		return head
	current = head
	while current.next is not None and current.next.data < data:
		current = current.next
	new_node.next = current.next
	current.next = new_node
	return head

def insertion_sort(head):
	sorted = None
	current = head
	while current is not None:
		next = current.next
		sorted = sorted_insert(sorted, current.data)
		current = next
	return sorted

# Об'єднання двох відсортованих однозв'язних списків
def merge_lists(list1, list2):
	dummy = Node(0)
	tail = dummy
	while True:
		if list1 is None:
			tail.next = list2
			break
		if list2 is None:
			tail.next = list1
			break
		if list1.data <= list2.data:
			tail.next = list1
			list1 = list1.next
		else:
			tail.next = list2
			list2 = list2.next
		tail = tail.next
	return dummy.next


if __name__ == '__main__':
	llist = LinkedList()

	for i in range(10):
		llist.push(random.randint(1, 10))

	print(f"Original Linked List:")
	llist.print_list()

	llist.reverse()
	print(f"Reversed Linked List:")
	llist.print_list()

	llist.head = insertion_sort(llist.head)
	print(f"Sorted Linked List:")
	llist.print_list()

	# Створення другого списку
	llist2 = LinkedList()
	for i in range(10):
		llist2.push(random.randint(1, 10))

	# Сортування другого списку
	llist2.head = insertion_sort(llist2.head)

	# Об'єднання двох списків
	llist.head = merge_lists(llist.head, llist2.head)
	print(f"Merged Linked List:")
	llist.print_list()

