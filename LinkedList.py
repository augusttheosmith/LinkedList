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

	def __len__(self):
			count = 0
			current = self.head
			while current is not None:
				count += 1
				current = current.next
			return count

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

	def get(self, index):
		x = self.head
		count = 1
		while x is not None:
			if count == index + 1:
				print("______________")
				return x.data
			x = x.next
			count += 1
		return None


	def indexOf(self, value):
		count = 0
		x = self.head

		while x is not None:
			if x.data == value:
				return count
			x = x.next
			count += 1
		print("______________")
		return None

	def clear(self):
		self.head = None
		self.tail = None
		return

	def removes(self, index):
		current = self.head
		count = 1 

		while current is not None:
			if count == index + 1:
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
			count += 1
		return False

	def replace(self, index, value):
		current = self.head
		count = 1

		while current is not None:
			if count == index + 1:
				current.data = value
				return True
			current = current.next
			count += 1
		return False

	def insert(self, index, value):

		if index == 0:
			self.prepend(value)
			return

		a = Node(value)
		current = self.head
		count = 1


		while current is not None:
			if count == index + 1:
				a.previous = current.previous
				a.next = current

				if current.previous is not None:
					current.previous.next = a 
				current.previous = a
				return
			current = current.next
			count += 1
		self.add(value)




ist = LinkedList(1, 2, 3, 4, 5, 6, 7, 8)

ist.printlist()
ist.insert(1, 20)
ist.printlist()
'''
print(ist.get(5)) *
print(ist.indexOf(1))
ist.replace(3, 4) *
ist.printlist()
ist.removes(1) *
ist.printlist()
ist.insert(2, 9) *
ist.printlist()
print("_____")
print(len(ist))
'''