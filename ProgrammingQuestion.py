'''
15. PROGRAMMING QUESTION: This should be a separate submission on Canvas. Please
submit the
link to your Github repo that solves this problem. First start by making a Github repo and clone
the
repo onto your computer. Then, create a python file that contains this starter code below:
class CardNode:
'''
class CardNode:
	def __init__(self, card):
		self.card = card
		self.next = None

class Deck:

	def __init__(self, a):
		self.head = None

		for card in a:
			self.add_card(card)


	def add_card(self, card):
		cards = CardNode(card)
		cards.next = self.head
		self.head = cards

	def draw_top_card(self):
		if self.head is None:
			return None

		card = self.head
		self.head = self.head.next
		return card.card

Cards = ["Ace", "Joker", "Jack", "King", "Queen", "Pawn", "Rook"]
a = Deck(Cards)
print(a.draw_top_card())

'''
You’re going to be making a card deck in a way that is similar to the linked list we’ve been
working
on up until now. The card attribute in the CardNode class can be a string such as “King of
Hearts.”
First implement the add_card(card) method in the Deck class. This should add a new card to
the
end of the deck. Then implement draw_top_card(). This should remove the first card from the
deck and return its value. If the deck is empty, None can be returned. Lastly, implement
'''