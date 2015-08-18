from Robot import Robot
from random import randint
from Hand import Hand
from random import shuffle
a1 = Robot("player1")
a2 = Robot("player2")
a3 = Robot("player3")
a4 = Robot("player4")
a5 = Robot("player5")
POOL=[a1,a2,a3,a4,a5]

def withdrawCards():
	for x, y in zip(POOL,POOL[1:]):
		rand=randint(0,4)
		x.insertCard(y.removeCard(rand))
	POOL[len(POOL)-1].insertCard(POOL[0].removeCard(rand))
def showAllHands():

	for b in POOL:
		print("{} : {} - {}".format(b.getName(),b.getHand(),Hand.getPowerHand(b.getHand())))


def main():
	for x in range(100):
		withdrawCards()
	showAllHands()

if __name__ == "__main__":
    main()


