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
DEBUG_SHUFFLE=False
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
			print("#{} wins {}".format(b.getName(),min(result)))
			b.winGame()
	
def main():
	round=1
	for x in range(2):
		print("\n#Game Round {}".format(round))
		newRound()
		#showAllHands()
		del result[:]
		##############################################################
		dealCards()
		#showAllHands()
		##############################################################
		print("\n#Game Flop".format(round))		
		randint(0,100)
		turn=0
		for x in range(5):
			turn+=1
			print("\n#Game Turn {}".format(turn))					
			#time.sleep(5)
			withdrawCards()
		showAllHands()
		calculateRound()
		round+=1
		#time.sleep(2)
		
	printSummary()	
	
	
if __name__ == "__main__":
    main()


