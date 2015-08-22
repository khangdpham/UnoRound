from random import shuffle
from Hand import Hand
from random import randint
import numbers

class Player(object):
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
		self.points+=Player.TIE_POINT
	def notWin(self):
		self.points+=Player.NOT_WIN_POINT
	def winGame(self):
		self.win += 1
		self.points+=Player.WIN_POINT
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
	def processInput(self,str,turn):
		var_i = raw_input(str)
		if str == "#Game Drawcard":
			if (int(var_i) <=5 or int(var_i) >= 1):
				c = int(var_i)-1
			else:
				c = randint(0,4)
			return int(c)
		if str == "#Game Action":
			return int(var_i)


