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
			self.add(x)

	def add(self, data):
		a = Node(data)
		
		if self.head is None:
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

	def prepend(self, addon):
		a = Node(addon)

		if self.head is None:
			self.head = a
			self.tail = a
			return
		a.next = self.head
		self.head.previous = a
		self.head = a


	def remove(self, rem):
		current = self.head

		while current is not None:
			if current.data == rem:
				if current.previous is not None:
					current.previous.next = current.next
				else:
					self.head = current.next
				if current.next is not None:
					current.next.previous = current.previous
				else:
					self.tail = current.previous
				return True
			current = current.next


ist = LinkedList(1, 2, 3, 4, 5, 6, 7, 8)
print(ist.search(5))

ist.printlist()
ist.printreverselist()
ist.prepend(5)
ist.printlist()
ist.remove(1)
ist.printlist()