import random
import time
import sys
import os
import math

sys.setrecursionlimit(1000000)

# rules
# https://www.youtube.com/watch?v=-A-djjimCcM

# https://www.youtube.com/watch?v=l-hh51ncgDI

# free turn
# https://stackoverflow.com/questions/16656976/how-to-adapt-my-minimax-search-tree-to-deal-with-no-term-based-game


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# 5x5
#BOARD
# 
#       11   10  9   8   7   6
# AI	x || x | x | x | x | x ||
# P1  	  || x | x | x | x | x || x
# 		     0   1   2   3   4    5
# 
# LARGEST SCORE --> beads*slots = 3*10 = 30

sungka = [3,3,3,3,3,0,3,3,3,3,3,0]

each_slot = 5
total_slots = 11
beads = 3

P1_last_slot = 4
P1_score_slot = 5

# 7x7
#BOARD
# 
#       15  14  13  12  11  10   9   8
# AI	x || x | x | x | x | x | x | x ||
# P1  	  || x | x | x | x | x | x | x || x
# 		     0   1   2   3   4   5   6    7
# 
# LARGEST SCORE --> beads*slots = 4*12 = 48

# sungka = [4,4,4,4,4,4,4,0,4,4,4,4,4,4,4,0]

# each_slot = 7
# total_slots = 15
# beads = 4

# P1_last_slot = 6
# P1_score_slot = 7

AI_start_slot = P1_score_slot + 1 
AI_last_slot = P1_score_slot * 2
AI_score_slot = AI_last_slot + 1


def printBoard():
	# 5x5
	print "\t\t   [10] [9] [8] [7] [6]"
	print "\tAI\t", sungka[11], "||", sungka[10], "|", sungka[9], "|", sungka[8], "|", sungka[7], "|", sungka[6], "||"
	print "\t\t  ||", sungka[0], "|" ,sungka[1], "|", sungka[2], "|", sungka[3], "|", sungka[4], "||", sungka[5], "\tP1"
	print "\t\t    [1] [2] [3] [4] [5]"

	# 7x7
	# print "\t\t    [14][13][12][11][10][9] [8]"
	# print "\tAI\t", sungka[15], "||", sungka[14], "|", sungka[13], "|", sungka[12], "|", sungka[11], "|", sungka[10], "|", sungka[9], "|", sungka[8], "||"
	# print "\t\t  ||", sungka[0], "|" ,sungka[1], "|", sungka[2], "|", sungka[3], "|", sungka[4], "|", sungka[5], "|", sungka[6], "||", sungka[7], "\tP1"
	# print "\t\t    [1] [2] [3] [4] [5] [6] [7]"


def intro():
	x = "SUNGKA"

	print "\n"
	for y in x:
	    time.sleep(0.5)
	    sys.stdout.write("\t" + y)
	    sys.stdout.flush()

	print "\n\n"


def choose():
	time.sleep(1)

	s = '.'
	sys.stdout.write( '\tDisplaying board' )
	for i in range(5):
	    sys.stdout.write( s )
	    sys.stdout.flush()
	    time.sleep(0.5)

	print "\n"
	printBoard()

	time.sleep(1)
	player1 = random.randint(1, 10)

	s = '.'
	sys.stdout.write( '\n\n\tWho will go first' )
	for i in range(5):
	    sys.stdout.write( s )
	    sys.stdout.flush()
	    time.sleep(0.5)

	if player1%2:
		print "\n\t\tYOU'RE FIRST"
		time.sleep(1)
		p1Turn()
	else:
		print "\n\t\tAI FIRST"
		time.sleep(1)
		aiThink()


def checkAIPossibleMoves(board):
	counter = AI_start_slot;
	posMoves = []

	while (counter <= AI_last_slot):
		if (counter == P1_score_slot):
			counter = counter + 1

		if (board[counter] != 0):
			posMoves.append(counter)
		counter = counter + 1

	return posMoves

def checkP1PossibleMoves(board):
	counter = 0;
	posMoves = []

	while (counter <= P1_last_slot):
		if (counter == P1_score_slot):
			counter = counter + 1

		if (board[counter] != 0):
			posMoves.append(counter)
		counter = counter + 1

	return posMoves

def trialMove(tempBoard, move):
	tempBoard = list(tempBoard)

	ai_value = tempBoard[move]
	tempBoard[move] = 0

	lastSlot = 1
	lastBeads = 0

	counter = 1
	newC = "false"
	newCounter = 0
	
	while (counter <= ai_value):
		slot = move+counter

		if slot > AI_score_slot:
			slot = 0
			newC = "true"

		if slot == P1_score_slot:
			slot = slot + 1

		if newC == "false":
			tempBoard[slot] = tempBoard[slot] + 1
			lastSlot = slot
			lastBeads = tempBoard[slot]
		else:
			tempBoard[newCounter] = tempBoard[newCounter] + 1
			newCounter = newCounter + 1
			lastSlot = newCounter
			lastBeads = tempBoard[newCounter]

		counter = counter + 1

	# print "tempBoard", tempBoard
	return tempBoard

def freeTurn(move):
	tempBoard = list(sungka)

	ai_value = tempBoard[move]
	tempBoard[move] = 0

	lastSlot = 1
	lastBeads = 0

	counter = 1
	newC = "false"
	newCounter = 0
	
	while (counter <= ai_value):
		slot = move+counter
		# print slot

		if slot > 15:
			slot = 0
			newC = "true"

		if slot == 7:
			slot = slot + 1

		if newC == "false":
			tempBoard[slot] = tempBoard[slot] + 1
			lastSlot = slot
			lastBeads = tempBoard[slot]
		else:
			tempBoard[newCounter] = tempBoard[newCounter] + 1
			newCounter = newCounter + 1
			lastSlot = newCounter
			lastBeads = tempBoard[newCounter]

		# board()
		counter = counter + 1

	if lastSlot == 15:
		return True 
	else:
		return False

def minimax(board, depth, alpha, beta, maximazingPlayer):
	checkAIMoves = checkAIPossibleMoves(board)
	checkP1Moves = checkP1PossibleMoves(board)
	# print(checkAIMoves)
	# print(checkP1Moves)

	tempBoard = list(board)
	number = 0
	if maximazingPlayer:
		bestValue = float("-inf")
		for number in checkAIMoves:
			tempBoard = trialMove(tempBoard, number)

			# print "maxvalue is", bestValue
			# print "max alpha is", alpha
			# print "max beta is", beta
			# print "max number is", number

			value = minimax(tempBoard, depth-1, alpha, beta, "false")
			# value = minimax(tempBoard, depth-1, alpha, beta, False)
			bestValue = max(bestValue, value)
			alpha = max(alpha, value)

			if (beta <= alpha):
				break

		# print "fin maxvalue is", bestValue
		# print "fin max alpha is", alpha
		# print "fin max beta is", beta
		# print "fin max number is", number
		return number
	else:
		bestValue = float("inf")
		for number in checkP1Moves:
			tempBoard = trialMove(tempBoard, number)

			# print "minvalue is", bestValue
			# print "min alpha is", alpha
			# print "min beta is", beta
			# print "min number is", number

			value = minimax(tempBoard, depth-1, alpha, beta, "true")
			# value = minimax(tempBoard, depth-1, alpha, beta, True)
			bestValue = min(bestValue, value)
			beta = min(beta, value)

			if (beta <= alpha):
				break

		# print "fin minvalue is", bestValue
		# print "fin min alpha is", alpha
		# print "fin min beta is", beta
		# print "fin min number is", number
		return number


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 															AI 																#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def aiThink():
	animation = "|/-\\!"

	c = random.randrange(5, 20, 5)

	print "\n"
	for i in range(c):
	    time.sleep(0.1)
	    sys.stdout.write("\r\tAI is Thinking" + animation[i % len(animation)])
	    sys.stdout.flush()
	    #do something
	print("\n\tDone!")

	aiTurn()


def aiTurn():
	aimove = minimax(sungka, 0, float("-inf"), float("inf"), "false")
	# aimove = minimax(sungka, 0, float("-inf"), float("inf"), True)


	print "\n\tAI moves", aimove

	aiMove(aimove)


def aiMove(move):
	ai_value = sungka[move]
	sungka[move] = 0

	lastSlot = 1
	lastBeads = 0

	counter = 1
	newC = "false"
	newCounter = 0
	
	while (counter <= ai_value):
		slot = move+counter
		# print slot

		if slot > AI_score_slot:
			slot = 0
			newC = "true"

		if slot == P1_score_slot:
			slot = slot + 1

		if newC == "false":
			sungka[slot] = sungka[slot] + 1
			lastSlot = slot
			lastBeads = sungka[slot]
		else:
			sungka[newCounter] = sungka[newCounter] + 1
			newCounter = newCounter + 1
			lastSlot = newCounter
			lastBeads = sungka[newCounter]

		counter = counter + 1

	printBoard()
	checkEnd()

	if lastSlot == AI_score_slot:
		print "\n\tAI Free Turn!!"
		aiThink()

	checkEnd()
	p1Think()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 														Player 1															#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def p1Think():
	print "\n\n\tYour Turn"
	p1Turn()


def p1Turn():
	p1_choice = 0
	pick_status = "true"

	while (p1_choice < 1 or p1_choice > P1_score_slot or pick_status == "false"):
		try:
			p1_choice = int(input("\n\tPick your move: "))

			if p1_choice < 1 or p1_choice > P1_score_slot:
				raise Exception


			# check if the "slot" is zero

			# if p1_choice <= 7:
			# 	p1_choice = p1_choice-1

			p1_choice = p1_choice-1
			p1_value = sungka[p1_choice]
			# print p1_value

			if (p1_value == 0):
				pick_status = "false"
				print "\tSlot is empty. Pick again."
			else:
				pick_status = "true"
				break
		except:
			print "\tIncorrect move. Pick again (1-5)."

	p1Move(p1_choice)


def p1Move(move):
	p1_value = sungka[move]
	sungka[move] = 0

	lastSlot = 1
	lastBeads = 0

	counter = 1
	newC = "false"
	newCounter = 0
	
	while (counter <= p1_value):
		slot = move+counter
		# print slot

		if slot > AI_last_slot:
			slot = 0
			newC = "true"

		if newC == "false":
			sungka[slot] = sungka[slot] + 1
			lastSlot = slot
			lastBeads = sungka[slot]
		else:
			sungka[newCounter] = sungka[newCounter] + 1
			newCounter = newCounter + 1
			lastSlot = newCounter
			lastBeads = sungka[newCounter]

		counter = counter + 1

	printBoard()
	checkEnd()
	if lastSlot == P1_score_slot:
		print "\n\tFree Turn!!"
		p1Turn()

	checkEnd()
	aiThink()

def checkEnd():
	p1remain = 0
	airemain = 0

	counter1 = 0
	while (counter1 <= P1_last_slot):
		p1remain = p1remain + sungka[counter1]
		counter1 = counter1 + 1

	counter2 = AI_start_slot
	while (counter2 <= AI_last_slot):
		airemain = airemain + sungka[counter2]
		counter2 = counter2 + 1

	p1_score = sungka[P1_score_slot]
	ai_score = sungka[AI_score_slot]

	if p1remain == 0:
		if (p1_score == ai_score):
			print "DRAW"
			print "\tYour Score:\t", p1_score
			print "\tAI Score:\t", ai_score
			exit()

		if (p1_score > ai_score):
			print "\n\tYOU WIN!"
			print "\tYour Score:\t", p1_score
			print "\tAI Score:\t", ai_score
			exit()
		else:
			print "\n\tAI WIN!"
			print "\tAI Score:\t", ai_score
			print "\tYour Score:\t", p1_score
			exit()

	if airemain == 0:
		if (p1_score == ai_score):
			print "DRAW"
			print "\tYour Score:\t", p1_score
			print "\tAI Score:\t", ai_score

		if (ai_score > p1_score):
			print "\n\tAI WIN!"
			print "\tAI Score:\t", ai_score
			print "\tYour Score:\t", p1_score
			exit()
		else:
			print "\n\tYOU WIN!"
			print "\tYour Score:\t", ai_score
			print "\tAI Score:\t", p1_score
			exit()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 														START GAME															#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
intro()
choose()

# p1Turn()
