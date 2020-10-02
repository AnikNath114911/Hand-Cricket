from random import *
from HandCricket import BattingFirst
from HandCricket import BowlingFirst

if __name__ == '__main__':
	print("Always enter 1 for heads or 2 for tails.")
	print("Always enter 1 for batting or 2 for bowling.")
	print("That's toss")
	a = int(input("Enter your choose:"))
	if a > 2 or a < 1:
		exit(1)
		pass
	else:
		b = randrange(1, 3)
		if a == b:
			print('Now you won the toss')
			print('Now its choosing')
			c = int(input('Enter your choose:'))
			if c > 2 or c < 1:
				exit(2)
				pass
			elif c == 1:
				myBat = BattingFirst.Batting()
				pass
			else:
				myBall = BowlingFirst.Bowling()
				pass
			pass
		else:
			print('Oops you lose the toss.')
			c = randrange(1, 3)
			if c == 1:
				print('Computer chooses batting.')
				BowlingFirst.Bowling()
				BattingFirst.Batting()
				pass
			else:
				print('Computer chooses bowling.')
				BattingFirst.Batting()
				BowlingFirst.Bowling()
				pass
			pass
		pass
	pass
