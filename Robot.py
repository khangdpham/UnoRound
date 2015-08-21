from random import shuffle
from Hand import Hand

class Robot(object):
	WIN_POINT=4
	TIE_POINT=2
	NOT_WIN_POINT=1
	def __init__(self, n,l):
		self.points= 0
		self.name = n	
		self.house = False
		self.hand = []
		self.win  = 0
		self.tie  = 0
		self.lose = 0
		self.level = l
		self.lastGame= 0
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.__str__()
	def setHouse(self,h):
		self.house = h
	def tieGame(self):
		self.points+=Robot.TIE_POINT
	def notWin(self):
		self.points+=Robot.NOT_WIN_POINT
	def winGame(self):
		self.win += 1
		self.points+=Robot.WIN_POINT
	def loseGame(self):
		self.lose += 1
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
	def setLastGameWin(self,l):
		self.lastGame = l
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
		if Hand.getPowerHand(Hand,sorted(self.hand)) < 65:
			return True
	def Strategy_2(self):
		if self.lastGame == 0:
			self.lastGame = 75
		if Hand.getPowerHand(Hand,sorted(self.hand)) < self.lastGame+30:
			return True
	def Strategy_3(self):
		if self.lastGame == 0:
			self.lastGame = 75
		if Hand.getPowerHand(Hand,sorted(self.hand)) < self.lastGame+50:
			return True
	def Strategy_4(self):
		if self.lastGame == 0:
			self.lastGame = 75
		if Hand.getPowerHand(Hand,sorted(self.hand)) < self.lastGame+70:
			return True
	def Strategy_5(self):
		if self.lastGame == 0:
			self.lastGame = 75
		if Hand.getPowerHand(Hand,sorted(self.hand)) < self.lastGame:
			return True
			
