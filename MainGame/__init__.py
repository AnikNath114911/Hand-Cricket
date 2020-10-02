from random import *


def battingFirst():
	pr = cr = out = target = 0
	while out == 0:
		i = int(input("Enter the runs:"))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print("Computer chooses " + str(j))
			if i == j:
				print("You are OUT..")
				target = pr + 1
				print("Your target is " + str(target))
				out += 1
				pass
			else:
				if i == 0:
					pr = pr + j
					pass
				else:
					pr = pr + i
					pass
				print("Your runs is " + str(pr))
				pass
			pass
		pass
	while target > cr:
		i = int(input('Enter your ball:'))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print('Computer chooses ' + str(j))
			if i == j:
				print("Computer is OUT..")
				if pr > cr:
					print("You won.")
					pass
				else:
					print("Match draws.")
					pass
				exit(0)
				pass
			else:
				if j == 0:
					cr = cr + i
					pass
				else:
					cr = cr + j
					pass
				print("Computer runs " + str(cr))
				pass
			pass
		pass
	print("Computer won.")
	exit(0)
	pass


def bowlingFirst():
	pr = cr = out = target = 0
	while out == 0:
		i = int(input("Enter your ball: "))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print("Computer chooses " + str(j))
			if i == j:
				print("Computer is OUT..")
				target = cr + 1
				print('Your target is ' + str(target))
				out += 1
				pass
			else:
				if j == 0:
					cr = cr + i
					pass
				else:
					cr = cr + j
					pass
				pass
				print("Computer runs is " + str(cr))
				pass
			pass
		pass
	while pr < target:
		i = int(input("Enter your run: "))
		if i < 0 or i > 6:
			exit(3)
			pass
		else:
			j = randrange(0, 7)
			print("Computer chooses " + str(j))
			if i == j:
				print("You are OUT..")
				if pr < cr:
					print("Computer won.")
					pass
				else:
					print("Match draws.")
					pass
				exit(0)
				pass
			else:
				if i == 0:
					pr = pr + j
					pass
				else:
					pr = pr + i
					pass
				print("Your run is " + str(pr))
				pass
			pass
		pass
	print("You won.")
	exit(0)
	pass


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
				battingFirst()
				pass
			else:
				bowlingFirst()
				pass
			pass
		else:
			print('Oops you lose the toss.')
			c = randrange(1, 3)
			if c == 1:
				print('Computer chooses batting.')
				bowlingFirst()
				pass
			else:
				print('Computer chooses bowling.')
				battingFirst()
				pass
			pass
		pass
	pass
