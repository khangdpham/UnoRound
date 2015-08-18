from random import shuffle


class Robot(object):
	MAX_HAND = 5
	def __init__(self, n):
		self.name = n	
		self.hand = [1,2,3,4,5]
	def getName(self):
		return self.name
	def getHand(self):
		return sorted(self.hand)
	def setNewHand(self,new_hand):
		self.hand = new_hand
	def removeCard(self,idx):
		return self.hand.pop(idx)
	def insertCard(self,card):
		self.hand.append(card)
		shuffle(self.hand)		
	def shuffleHand(self):
		shuffle(self.hand)			


		