#File boggle.py
#Esther Adu
#EAA15G
#CIS4930 - Assignment 1
#5/30/17

import random
import enchant

#Function displays board to user
def printBoard(board) :
	newBoard = []			#Declaring and initializing board

	#For loop checks for ranges
        for i in range(0, 16):
		l = (random.choice(board))	#Generating random index from list
		newBoard.append(random.choice(l)) #Generating random letter from index in list
		l.remove		#Remove the list to not appear again
                
	#New board stores list in a list for 2D list - I'm sure there's an easier way to do any of this
	mBoard = [[newBoard[0], newBoard[1], newBoard[2], newBoard[3]],
		  [newBoard[4], newBoard[5], newBoard[6], newBoard[7]],
		  [newBoard[8], newBoard[9], newBoard[10], newBoard[11]],
		  [newBoard[12], newBoard[13], newBoard[14], newBoard[15]]]

	#Display list to user
	print "[%s]  [%s]  [%s]  [%s]" %(mBoard[0][0], mBoard[0][1], mBoard[0][2], mBoard[0][3])
	print "[%s]  [%s]  [%s]  [%s]" %(mBoard[1][0], mBoard[1][1], mBoard[1][2], mBoard[1][3])
	print "[%s]  [%s]  [%s]  [%s]" %(mBoard[2][0], mBoard[2][1], mBoard[2][2], mBoard[2][3])
	print "[%s]  [%s]  [%s]  [%s]" %(mBoard[3][0], mBoard[3][1], mBoard[3][2], mBoard[3][3])
	return mBoard


#Function does calculation for board
def checkBoard(board) :
	userIn = ""  	#Declaring and initializing variables
	l = []
	final = []
	points = 0
	p = 0
	#Initializing dictionary
        myDict = enchant.Dict("en_US")

	#Prompting user for input
        print("Start typing your words! (Press enter after each word and enter 'X' when done):")

	#While loop checks for board input
        while (userIn != 'X' and userIn != 'x') :
		userIn = raw_input()
		userIn = userIn.upper()		#Turn all into uppercase
		if userIn != 'x'and userIn != 'X' :		
			l.append(userIn)			#Adding to list

	# For loop checks for correctness and adds points
        for i in l :
                if i in final :		
                        print "The word %s has already been used." %i
                elif len(i) < 3 :
                        print "The word %s is too short." %i
                elif myDict.check(i) == False :
                        print "The word %s ...is not an English word." %i
		elif not findIndex(i, board) :
			print "The word %s is not on the board." %i
                
                else :
                        if len(i) == 3 or len(i) == 4 :
                                print "The word %s is worth 1 point." %i
				p = 1
                        elif len(i) == 5 :
                                print "The word %s is worth 2 points!" %i
				p = 2
                        elif len(i) == 6 :
                                print "The word %s is worth 3 points!!" %i
				p = 3
                        elif len(i) == 7 :
                                print "The word %s is worth 5 points!!!" %i
				p = 5
                        elif len(i) > 7 :
                                print "The word %s is worth 11 points!!!!" %i
				p = 11
			points = points + p	#Finding total points
		final.append(i)		#Add to list to check if input was already added to previous list
		
	print "Your total score is ", points, " points!"


#Function finds the index of the letters in user input
def findIndex(v, b) :
	var = v[0]
	sIndex = 1	
	sameLetter = [ ]
	f = False

	#Checking to see if Qu exist on the board
	if var == "Q" :
		var = v[1]
		if var == "U" :
			sIndex = 2
			var == "Qu"
		
	for i in range(0, 4) :
		for j in  range(0, 4) :		
			if var == b[i][j] :
				f = checkIfInBoard(v, b, i, j, sIndex, sameLetter + [[i, j]])
			if f == True :
				return f

	return f

#Function checks if word actually exist in the board
def checkIfInBoard(v, b, i, j, s, sl) :
	isValid = False

	#If all word is found
	if s >= len(v) :
		return True
	else :
		var = v[s]

	#If statement checks all indexes to see if the next letter exist
	if (i+1 < 4 and j+1 < 4 and i-1 > -1 and j-1 > -1)  :	
		if (var == b[i+1][j] or var == b[i][j+1] or var == b[i-1][j]
			or var == b[i][j-1] or var == b[i-1][j-1] 
			or var == b[i+1][j+1] or var == b[i+1][j-1]
			or var == b[i-1][j+1]) :
			isValid = True

	elif (i+1 > 3 and j+1 < 4 and i-1 > -1 and j-1 > -1) :
		if (var == b[i][j+1] or var == b[i-1][j] or var == b[i][j-1]
			or var == b[i-1][j-1] or var == b[i-1][j+1]) :
			isValid = True

	elif (i+1 < 4 and j+1 > 3 and i-1 > -1 and j-1 > -1) :
		if(var == b[i+1][j] or var == b[i-1][j] or var == b[i][j-1]
			or var == b[i-1][j-1] or var == b[i+1][j-1]) :
			isValid = True

	elif (i+1 < 4 and j+1 < 4 and i-1 < 0 and j-1 > -1) :
		if(var == b[i+1][j] or var == b[i][j+1] or var == b[i][j-1]
			or var == b[i+1][j-1] or var == b[i+1][j+1]) :
			isValid = True
	
	elif (i+1 < 4 and j+1 < 4 and i-1 > -1 and j-1 < 0) :
		if (var == b[i+1][j] or var == b[i][j+1] or var == b[i+1][j+1]
			or var == b[i-1][j] or var == b[i-1][j+1]) :
			isValid = True

	elif (i+1 < 4 and j+1 < 4 and i-1 < 0 and j-1 < 0) :
		if (var == b[i+1][j] or var == b[i][j+1] or var == b[i+1][j+1]) :
			isValid = True

	elif (i+1 > 3 and j+1 > 3 and i-1 > -1 and j-1 > -1) :
		if (var == b[i-1][j] or var == b[i][j-1] or var == b[i-1][j-1]) :
			isValid =  True

	elif (i+1 > 3 and j+1 < 3 and i-1 > -1 and j-1 < 0) :
		if (var == b[i][j+1] or var == b[i-1][j] or var == b[i-1][j-1]) :
			isValid = True

	elif (i+1 < 4 and j+1 > 3 and i-1 < 0 and j-1 > -1) :
		if (var == b[i-1][j] or var == b[i+1][j] or var == b[i+1][j-1]) : 
			isValid = True

	else:
		return False

	#If isValid is true, then next letter exist. Find where that index is and recursively
	#call it to find next index
	if isValid == True :
		if ((j-1 > -1) and (var == b[i][j-1]) and (([i, j-1]) not in sl)) :
              		if checkIfInBoard(v, b, i, j-1, s+1, sl + [[i, j-1]]) :
				return True

		if ((i-1 > -1) and (var == b[i-1][j])  and (([i-1, j]) not in sl)) :
			if checkIfInBoard(v, b, i-1, j, s+1, sl + [[i-1, j]]) :
				return True

		if ((j+1 < 4) and (var == b[i][j+1]) and (([i, j+1]) not in sl)) :
			if checkIfInBoard(v, b, i, j+1, s+1, sl + [[i, j+1]]) :
				return True

		if ((i+1 < 4) and (var == b[i+1][j]) and (([i+1, j]) not in sl)) :
			if checkIfInBoard(v, b, i+1, j, s+1, sl + [[i+1, j]]) :
				return True

		if ((i-1 > -1) and (j-1 > -1) and (var == b[i-1][j-1]) and (([i-1, j-1]) not in sl)) :
			if checkIfInBoard(v, b, i-1, j-1, s+1, sl + [[i-1, j-1]]) :
				return True

		if ((i+1 < 4) and (j + 1 < 4) and (var == b[i+1][j+1]) and (([i+1, j+1]) not in sl)) :
			if checkIfInBoard(v, b, i+1, j+1, s+1, sl + [[i+1, j+1]]) :
				return True

		if ((i+1 < 4) and (j-1 > -1) and (var == b[i+1][j-1]) and (([i+1, j-1]) not in sl)) :
			if checkIfInBoard(v, b, i+1, j-1, s+1, sl + [[i+1, j-1]]) :
				return True

		if ((i-1 > -1) and (j+1 < 4) and (var == b[i-1][j+1]) and (([i-1, j+1]) not in sl)) :
			if checkIfInBoard(v, b, i-1, j+1, s+1, sl + [[i-1, j+1]]) :
				return True



# Main function
if __name__ == "__main__":

	boggleBoard = [['A', 'E', 'A', 'N', 'E', 'G'],	#Stores the board information
			['A', 'H', 'S', 'P', 'C', 'O'],
			['A', 'S', 'P', 'F', 'F', 'K'],
			['O', 'B', 'J', 'O', 'A', 'B'],
			['I', 'O', 'T', 'M', 'U', 'C'],
			['R', 'Y', 'V', 'D', 'E', 'L'],
			['L', 'R', 'E', 'I', 'X', 'D'],
			['E', 'I', 'U', 'N', 'E', 'S'],
			['W', 'N', 'G', 'E', 'E', 'H'],
			['L', 'N', 'H', 'N', 'R', 'Z'],
			['T', 'S', 'T', 'I', 'Y', 'D'],
			['O', 'W', 'T', 'O', 'A', 'T'],
			['E', 'R', 'T', 'T', 'Y', 'L'],
			['T', 'O', 'E', 'S', 'S', 'I'],
			['T', 'E', 'R', 'W', 'H', 'V'],
			['N', 'U', 'I', 'H', 'M', 'Qu']]

	#Calling functions
	nboard = printBoard(boggleBoard)
	checkBoard(nboard)

