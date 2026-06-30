class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None
		self.previous = None

class LinkedList:

	def __init__(self, *CoolList):
		self.head = None
		self.tail = None

		for x in CoolList:
			self.add(x) #calls the function "add" for each value in the tuple

	def add(self, data):
		a = Node(data) #calls node for each thing in the tuple
		
		if self.head is None: #finds the leading value
			self.head = a
			self.tail = a
			return
		self.tail.next = a 
		a.previous = self.tail
		self.tail = a

	def search(self, b):
		current = self.head

		while current is not None:
			if current.data == b:
				return True
			current = current.next
		return False

	def printlist(self):
		current = self.head
		print("----print----")
		while current is not None:
			print(current.data)
			current = current.next

	def printreverselist(self):
		current = self.tail
		print("----reverse----")
		while current is not None:
			print(current.data)
			current = current.previous

ist = LinkedList(1, 2, 3, 4, 5, 6, 7, 8)
print(ist.search(5))

ist.printlist()
ist.printreverselist()