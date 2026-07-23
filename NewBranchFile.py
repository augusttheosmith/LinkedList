import LinkedList
'''
Hi = LinkedList.LinkedList(1, 2, 3 , 4, 5, 6, 7, 8)

Hi.printlist()
Hi = LinkedList(1, 2, 3, 4, 5, 6, 7, 8)
Hi.printlist()
'''
class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item) 

	def pop(self):
		return self.items.pop()

	def peek(self):
		if self.items == None:
			return
		return self.items[-1]
Stacks = Stack()

Stacks.push(1)
Stacks.push(2)
Stacks.push(3)
Stacks.push(4)

print(Stacks.items)
print("__________")
Stacks.pop()
print(Stacks.items)
print("__________")
print(Stacks.peek())
