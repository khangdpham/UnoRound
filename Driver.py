from Robot import Robot
from random import randint
from Hand import Hand
from random import shuffle
import time
import datetime
from operator import itemgetter

ROUND = 1000
#ROUND = 1000
a1 = Robot("player1",1)
a2 = Robot("player2",2)
a3 = Robot("player3",3)
a4 = Robot("player4",4)
a5 = Robot("player5",5)
FLIPPER= None
POOL=[a1,a2,a3,a4,a5]
DECK=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
R_RESULT=[]
DEBUG_SHUFFLE= True
def dealCards():
	newDeck =list(DECK)
	if DEBUG_SHUFFLE : shuffle(newDeck)
	for i in range(5):
		#print(newDeck)
		if DEBUG_SHUFFLE : shuffle(newDeck)
		for c in POOL:
			card = newDeck.pop(0)
			print("#{} gets {}".format(c.getName(),card))
			c.dealCard(card)
		
def withdrawCards():
	card = None
	for x, y in zip(POOL,POOL[1:]):
		rand=randint(0,4)
		card= y.removeCard(rand)
		print("#{} loses {}".format(y.getName(),card))		
		x.insertCard(card)
		print("#{} gets {}".format(x.getName(),card))
	card = POOL[0].removeCard(rand)
	print("#{} loses {}".format(POOL[0].getName(),card))	
	POOL[len(POOL)-1].insertCard(card)
	print("#{} gets {}".format(POOL[len(POOL)-1].getName(),card))
def showAllHands():
	for b in POOL:
		print("#{} hand {} {}".format(b.getName(),b.getHand(),Hand.getPowerHand(Hand,b.getHand())))
		#print("{} : {} - {}".format(b.getName(),b.getHand(),Hand.getPowerHand(Hand,b.getHand())))
def newRound():
	del R_RESULT[:]
	for b in POOL:
		b.resetHand()
def printSummary():
	for b in POOL:
		print("{} wins: {} ties: {} loses:{} points:{}".format(b.getName(),b.win,b.tie,b.lose,b.points))

def calculateRound():
	#### TODO : Calculate Winning points and Tie
	###############################################################
	global R_RESULT,FLIPPER
	for b in POOL:
		R_RESULT.append({'bot':b,'hand':Hand.getPowerHand(Hand,b.getHand())})
	R_RESULT= sorted(R_RESULT,key=lambda k:k['hand'])
	#print(R_RESULT)
	for b in POOL:
		b.setLastGameWin(R_RESULT[0]['hand'])
	
	###### This happens when all players have [1,2,3,4,5] hand
	uHand = [1,2,3,4,5]
	count = 0
	for b in R_RESULT:
		if b['hand'] == uHand:
			count+=1
	if count == 5:
		for b in POOL:
			b.tieGame()
		return
	if count == 3:
		for i in range(2):
			R_RESULT[i]['bot'].winGame()
		if R_RESULT[3]['bot'] == FLIPPER:
			R_RESULT[3]['bot'].loseGame()
			R_RESULT[4]['bot'].notWin()
		if R_RESULT[4]['bot'] == FLIPPER:
			R_RESULT[3]['bot'].notWin()
			R_RESULT[4]['bot'].loseGame()
		return
	######################################################################
	f_idx = 99
	for x in R_RESULT:
		if x['bot'] == FLIPPER:
			f_idx = R_RESULT.index(x)

	if R_RESULT[0]['hand'] == R_RESULT[1]['hand']:
		if R_RESULT[0]['bot'] != FLIPPER and R_RESULT[1]['bot'] != FLIPPER:
			R_RESULT.append(R_RESULT.pop(f_idx))
		R_RESULT[0]['bot'].winGame()
		R_RESULT[1]['bot'].winGame()
		R_RESULT[2]['bot'].notWin()
		R_RESULT[3]['bot'].notWin()	
		R_RESULT[4]['bot'].loseGame()
	else:
		if R_RESULT[0]['bot'] != FLIPPER:
			R_RESULT.append(R_RESULT.pop(f_idx))
		R_RESULT[0]['bot'].winGame()
		R_RESULT[1]['bot'].notWin()
		R_RESULT[2]['bot'].notWin()
		R_RESULT[3]['bot'].notWin()	
		R_RESULT[4]['bot'].loseGame()		
	
def main():
	global FLIPPER
	round=1
	for x in range(ROUND):
		print("\n#Game Round {}".format(round))
		newRound()
		#showAllHands()
		##############################################################
		dealCards()
		#showAllHands()
		##############################################################
		print("\n#Game Flop".format(round))		
		randint(0,100)
		turn=0
		#############################################################
		##### FLOP COUNT ############################################
		flip= False

		#############################################################
		while True:
			print("\n#Game Turn {}".format(turn))				
			turn+=1
			withdrawCards()
			for b in POOL:
				if b.StrategyThinking() and turn > 5:
					flip = True
					FLIPPER = b
					print("#{} flips".format(b.getName()))
					break
			if flip : break
		#############################################################
		#############################################################
		'''
		a1.setNewHand([1,2,2,3,4])			
		a2.setNewHand([1,2,2,3,4])			
		a3.setNewHand([1,1,1,5,5])			
		a4.setNewHand([2,3,3,4,4])			
		a5.setNewHand([3,4,5,5,5])			
		'''
		'''
		a1.setNewHand([2,3,4,5,5])			
		a2.setNewHand([1,1,1,2,2])			
		a3.setNewHand([2,3,4,5,5])			
		a4.setNewHand([3,3,3,4,4])			
		a5.setNewHand([1,1,2,4,5])		
		'''
		'''
		a1.setNewHand([1,1,2,2,4])			
		a2.setNewHand([1,1,2,2,4])			
		a3.setNewHand([1,2,3,5,5])			
		a4.setNewHand([3,3,4,5,5])			
		a5.setNewHand([3,3,4,4,5])			
		
		'''
		#############################################################
		#############################################################
		showAllHands()
		print("")
		calculateRound()
		round+=1
		#time.sleep(2)
		
	printSummary()	
	
	
if __name__ == "__main__":
    main()


