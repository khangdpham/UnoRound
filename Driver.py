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
POOL=[a1,a2,a3,a4,a5]
DECK=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
result=[]
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
		print("#{} hand {}".format(b.getName(),b.getHand()))
		#print("{} : {} - {}".format(b.getName(),b.getHand(),Hand.getPowerHand(Hand,b.getHand())))
def newRound():
	del result[:]
	for b in POOL:
		b.resetHand()
def printSummary():
	for b in POOL:
		print("{} wins: {} ties: {} points:{}".format(b.getName(),b.win,b.tie,b.points))

def calculateRound():
	#### TODO : Calculate Winning points and Tie
	###############################################################
	global result
	for b in POOL:
		result.append({'bot':b,'hand':Hand.getPowerHand(Hand,b.getHand())})
	result= sorted(result,key=lambda k:k['hand'])
	for b in POOL:
		b.setLastGameWin(result[0]['hand'])
	points=4
	i = 0
	skip = False
	for i in range(len(result)-1):
		if skip:
			skip = False
			continue
		if i == 0:
			if result[i]['hand'] == result[i+1]['hand']:	
				result[i]['bot'].winGame()
				result[i+1]['bot'].winGame()
				result[i]['bot'].tieGame()
				result[i+1]['bot'].tieGame()
				result[i]['bot'].addPoint(points)
				result[i+1]['bot'].addPoint(points)
				skip =True
			else:
				result[i]['bot'].winGame()
				result[i]['bot'].addPoint(points)
		else:
			if result[i]['hand'] == result[i+1]['hand']:	
				result[i]['bot'].tieGame()
				result[i+1]['bot'].tieGame()
				result[i]['bot'].addPoint(points)
				result[i+1]['bot'].addPoint(points)
				skip =True
			else:
				result[i]['bot'].addPoint(points)
		points-=1
		
			


	return

	for b in POOL:
		if Hand.getPowerHand(Hand,b.getHand()) == min(result):
			print("#{} wins {}".format(b.getName(),min(result)))
			b.winGame()
def main():
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
		flop= False

		#############################################################
		while True:
			print("\n#Game Turn {}".format(turn))				
			turn+=1
			withdrawCards()
			for b in POOL:
				if b.StrategyThinking() and turn > 5:
					print("#{} flips".format(b.getName()))
					flop = True
			if flop : break
		#############################################################
		#############################################################
		#a1.setNewHand([1,2,2,3,4])			
		#a2.setNewHand([1,2,2,3,4])			
		#a3.setNewHand([1,1,1,5,5])			
		#a4.setNewHand([2,3,3,4,4])			
		#a5.setNewHand([3,4,5,5,5])			

		
		#a1.setNewHand([1,1,2,2,4])			
		#a2.setNewHand([1,1,2,2,4])			
		#a3.setNewHand([1,2,3,5,5])			
		#a4.setNewHand([3,3,4,5,5])			
		#a5.setNewHand([3,3,4,4,5])			


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


