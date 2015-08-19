from Robot import Robot
from random import randint
from Hand import Hand
from random import shuffle
import time
import datetime

a1 = Robot("player1")
a2 = Robot("player2")
a3 = Robot("player3")
a4 = Robot("player4")
a5 = Robot("player5")
POOL=[a1,a2,a3,a4,a5]
DECK=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
result=[]
def dealCards():
	newDeck =list(DECK)
	shuffle(newDeck)
	for i in range(5):
		shuffle(newDeck)
		for c in POOL:
			c.dealCard((newDeck.pop(0)))
		
def withdrawCards():
	for x, y in zip(POOL,POOL[1:]):
		rand=randint(0,4)
		x.insertCard(y.removeCard(rand))
	POOL[len(POOL)-1].insertCard(POOL[0].removeCard(rand))
def showAllHands():
	for b in POOL:
		print("{} : {} - {}".format(b.getName(),b.getHand(),Hand.getPowerHand(Hand,b.getHand())))
def newRound():
	for b in POOL:
		b.resetHand()
def printSummary():
	for b in POOL:
		print("{} wins: {}".format(b.getName(),b.win))

def calculateRound():
	for b in POOL:
		result.append(Hand.getPowerHand(Hand,b.getHand()))
	for b in POOL:
		if Hand.getPowerHand(Hand,b.getHand()) == min(result):
			print("{} wins with hand {}".format(b.getName(),min(result)))
			b.winGame()
	
def main():
	round=1
	for x in range(5):
		print("\nRound {} {}\n".format(round,datetime.datetime.now()))
		newRound()
		del result[:]
		dealCards()
		randint(0,100)
		for x in range(5):
			#time.sleep(5)
			withdrawCards()
		showAllHands()
		calculateRound()
		round+=1
		time.sleep(2)
	printSummary()	
	
	
if __name__ == "__main__":
    main()


