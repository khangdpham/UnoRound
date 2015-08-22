from Robot import Robot
from Player import Player
from random import randint
from Hand import Hand
from random import shuffle
import time
import datetime
from operator import itemgetter


class UboRound(object):

	ROUND = 1
	a1 = Robot("player1",1)
	a2 = Robot("player2",2)
	a3 = Robot("player3",3)
	a4 = Robot("player4",4)
	a5 = Player("Khang",5)
	FLIPPER= None
	FLIPPED=False
	POOL=[a1,a2,a3,a4,a5]
	DECK=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
	R_RESULT=[]
	DEBUG_SHUFFLE= True
	def dealCards(self):
		newDeck =list(self.DECK)
		if self.DEBUG_SHUFFLE : shuffle(newDeck)
		for i in range(5):
			#print(newDeck)
			if self.DEBUG_SHUFFLE : shuffle(newDeck)
			for c in self.POOL:
				card = newDeck.pop(0)
				print("#{} gets {}".format(c.getName(),card))
				c.dealCard(card)
	def withdrawCards(self,t):
		card = None
		rand = 99
		for x, y in zip(self.POOL,self.POOL[1:]):
			if isinstance(x,Player):
				print("#{} hand {}".format(a5.getName(),a5.getHand()))
				rand=x.processInput("#Game Drawcard",t)	
			else:
				rand=randint(0,4)
			card= y.removeCard(rand)
			print("#{} loses {}".format(y.getName(),card))		
			x.insertCard(card)
			print("#{} gets {}".format(x.getName(),card))
		if isinstance(self.POOL[len(self.POOL)-1],Player):
			p=self.POOL[len(self.POOL)-1]
			print("#{} hand {}".format(p.getName(),p.getHand()))
			rand=self.POOL[len(self.POOL)-1].processInput("#Game Drawcard")
		else:
			rand=randint(0,4)
		card = self.POOL[0].removeCard(rand)
		print("#{} loses {}".format(self.POOL[0].getName(),card))	
		self.POOL[len(self.POOL)-1].insertCard(card)
		print("#{} gets {}".format(self.POOL[len(self.POOL)-1].getName(),card))

	def flipGame(self,p):
		if isinstance(p,Player):
			action=p.processInput("#Game Action")
			if action == 1:
				self.FLIPPED = True
				self.FLIPPER = p
				print("#{} flips".format(p.getName()))
				return True
		else:
			if p.StrategyThinking():
				self.FLIPPED= True
				self.FLIPPER = p
				print("#{} flips".format(p.getName()))
				return True

		return False

	def showAllHands(self):
		for b in self.POOL:
			print("#{} hand {} {}".format(b.getName(),b.getHand(),Hand.getPowerHand(Hand,b.getHand())))
			#print("{} : {} - {}".format(b.getName(),b.getHand(),Hand.getPowerHand(Hand,b.getHand())))
	def newRound(self):
		del self.R_RESULT[:]
		for b in self.POOL:
			b.resetHand()
	def printSummary(self):
		for b in self.POOL:
			print("{} wins: {} ties: {} loses:{} points:{}".format(b.getName(),b.win,b.tie,b.lose,b.points))

	def calculateRound(self):
		#### TODO : Calculate Winning points and Tie
		###############################################################
		for b in self.POOL:
			self.R_RESULT.append({'bot':b,'hand':Hand.getPowerHand(Hand,b.getHand())})
		self.R_RESULT= sorted(self.R_RESULT,key=lambda k:k['hand'])
		#print(self.R_RESULT)
		for b in self.POOL:
			if isinstance(b,Player):continue
			b.setLastGameWin(self.R_RESULT[0]['hand'])
		
		###### This happens when all players have [1,2,3,4,5] hand
		uHand = [1,2,3,4,5]
		count = 0
		for b in self.R_RESULT:
			if b['hand'] == uHand:
				count+=1
		if count == 5:
			for b in self.POOL:
				b.tieGame()
			return
		if count == 3:
			for i in range(2):
				self.R_RESULT[i]['bot'].winGame()
			if self.R_RESULT[3]['bot'] == self.FLIPPER:
				self.R_RESULT[3]['bot'].loseGame()
				self.R_RESULT[4]['bot'].notWin()
			if self.R_RESULT[4]['bot'] == self.FLIPPER:
				self.R_RESULT[3]['bot'].notWin()
				self.R_RESULT[4]['bot'].loseGame()
			return
		######################################################################
		f_idx = 99
		for x in self.R_RESULT:
			if x['bot'] == self.FLIPPER:
				f_idx = self.R_RESULT.index(x)

		if self.R_RESULT[0]['hand'] == self.R_RESULT[1]['hand']:
			if self.R_RESULT[0]['bot'] != self.FLIPPER and self.R_RESULT[1]['bot'] != self.FLIPPER:
				self.R_RESULT.append(self.R_RESULT.pop(f_idx))
			self.R_RESULT[0]['bot'].winGame()
			self.R_RESULT[1]['bot'].winGame()
			self.R_RESULT[2]['bot'].notWin()
			self.R_RESULT[3]['bot'].notWin()	
			self.R_RESULT[4]['bot'].loseGame()
		else:
			if self.R_RESULT[0]['bot'] != self.FLIPPER:
				self.R_RESULT.append(self.R_RESULT.pop(f_idx))
			self.R_RESULT[0]['bot'].winGame()
			self.R_RESULT[1]['bot'].notWin()
			self.R_RESULT[2]['bot'].notWin()
			self.R_RESULT[3]['bot'].notWin()	
			self.R_RESULT[4]['bot'].loseGame()		
	@staticmethod	
	def startGame(self):

		
		self.ROUND=1
		for x in range(self.ROUND):
			print("\n#Game self.ROUND {}".format(self.ROUND))
			self.newRound()
			#showAllHands()
			##############################################################
			self.dealCards()
			self.showAllHands()
			raw_input()
			##############################################################
			print("\n#Game Flop".format(self.ROUND))		
			randint(0,100)
			turn=1
			#############################################################
			##### FLOP COUNT ############################################
			self.FLIPPED= False

			#############################################################
			while True:
				print("\n#Game Turn {}".format(turn))				
				turn+=1
				self.withdrawCards(turn)
				self.showAllHands()
				raw_input()
				for b in self.POOL:
					if self.flipGame(b) : break
				if self.FLIPPED: break

			
			#############################################################
			self.showAllHands()
			raw_input()
			self.calculateRound()
			self.ROUND+=1
			#time.sleep(2)
			
		self.printSummary()	
		
		
	if __name__ == "__main__":
	    main()


