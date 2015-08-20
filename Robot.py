from random import shuffle
from Hand import Hand

class Robot(object):
	def __init__(self, n,l):
		self.name = n	
		self.hand = []
		self.win  = 0
		self.tie  = 0
		self.level = l
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
	def StrategyThinking(self):
		if self.level == 1:
			if self.Strategy_1():
				return  True
		if self.level == 2:
			if self.Strategy_2():
				return  True
		
		if self.level == 3:
			if self.Strategy_3():
				return  True
		if self.level == 4:
			if self.Strategy_4():
				return  True
		
		if self.level == 5:
			if self.Strategy_5():
				return  True
		return False
	def Strategy_1(self):
		if Hand.getPowerHand(Hand,sorted(self.hand)) < 75:
			return True
	def Strategy_2(self):
		if Hand.getPowerHand(Hand,sorted(self.hand)) < 65:
			return True
	def Strategy_3(self):
		if Hand.getPowerHand(Hand,sorted(self.hand)) < 55:
			return True
	def Strategy_4(self):
		if Hand.getPowerHand(Hand,sorted(self.hand)) < 45:
			return True
	def Strategy_5(self):
		if Hand.getPowerHand(Hand,sorted(self.hand)) < 40:
			return True
			
