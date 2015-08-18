from Robot import Robot
from random import randint
from random import shuffle
a1 = Robot("player1")
a2 = Robot("player2")
a3 = Robot("player3")
a4 = Robot("player4")
a5 = Robot("player5")
POOL=[a1,a2,a3,a4,a5]
MYLIST=[]
text_file = open("Output.txt", "w")
for a1 in range(5):
	for a2 in range(5):
		for a3 in range(5):
			for a4 in range(5):
				for a5 in range(5):
					#print("{},{},{},{},{}".format(a1+1,a2+1,a3+1,a4+1,a5+1))
					#text_file.write("{},{},{},{},{}\n".format(a1+1,a2+1,a3+1,a4+1,a5+1))
					MYLIST.append([a1+1,a2+1,a3+1,a4+1,a5+1])
for c in MYLIST:
	c = sorted(c)
	text_file.write("{},{},{},{},{}\n".format(c[0],c[1],c[2,c[3],c[4]))
		
text_file.close()