from random import shuffle


class Robot(object):
	def __init__(self, n):
		self.name = n	
		self.hand = []
		self.win  = 0
		self.tie  = 0
	def winGame(self):
		self.win += 1
	def tieGame(self):
		self.tie += 1
	def dealCard(self,c):
		self.hand.append(c)
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
	def resetHand(self):
		self.hand=[]


		