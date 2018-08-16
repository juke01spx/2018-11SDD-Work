
def loadArray():
	i = 0
	Element = []
	dataValue = input('Enter data value, XXX to finish ')
	while dataValue.upper() != "XXX":
		Element.append(dataValue)
		i += 1
		dataValue = input('Enter data value, XXX to finish ')
	numElements = i
	print(f"There are {numElements} items loaded into array")
	return Element, numElements
	
def loadArray2():
	i = 0
	Element = []
	while True:
		dataValue = input('Enter data value, XXX to finish ')
		if dataValue.upper() == "XXX":
			break
		Element.append(dataValue)
		i += 1
	numElements = i
	print(f"There are {numElements} items loaded into array")
	return Element, numElements

def printArray(Element, numElements):
	i = 0
	while True:
		print(f"Element({i}) = {Element[i]}")
		i += 1
		if i >= numElements:
			break

def sumArrayContents(Element, numElements):
	i = 0
	total = 0
	while True:
		total += int(Element[i])
		i += 1
		if i >= numElements:
			break
	print(f"The sum of all elements in the Array is {total}")

def getChars(dateString,start, len):
	day = ""
	for i in range(start,start+len,1):
		day += dateString[i]
	return day
	
def extractDataFromString():
	
	dateString = input("Date dd/mm/yy: ")
	print(dateString)
	
	day = getChars(dateString,0,2)
	month = getChars(dateString,3,2)
	
	print(f"The month is {month}, and the day of the month is {day}.")

def insertString(first, second):
	newWord = ""
	initialString = input("Initial String? ")
	newWord = input("Word to insert? ")
	for ch in first:
		if ch != ";":
			newWord += ch
		else:
			newWord += second
	return newWord

def InsertNewWordIntoString():
	#Get InitialSring and newWord
	initialString = input("Initial String? ")
	newWord = input("Word to insert? ")
	
	# L = len of initial string
	L = len(initialString)
	
	found = False
	i = 0
	
	while TRUE:
		checkLetter = initialString[i]
		if checkLetter == ";":
			firstPart = ""
			for x in range(0,i):
				firstPart += initialString[x]
			secondPart = ""
			for x in range(i+1,L):
				secondPart += initialString[x]
			newString = firstPart + newWord + secondPart
			found = true
		i+=1
	
		if i >= L or found:
			break
		

def DeleteWordFromString():
	#Get InitialString, StringToGo 
	initialString = input("Initial String: ")
	StringToGo = input("String To Go: ")
	'''
	Let LString = Length of InitialString
	Let Lword = Length of StringToGo
	Let found = 0
	Let i = 0
	'''
	LString = len(initialString)
	Lword = len(StringToGo)
	found = False
	i = 0
	while True:	#REPEAT
		#extract from the ith character (for Lword letters) from InitialString into CheckforWord
		CheckforWord = ""
		for x in range(i,i+Lword):
			CheckforWord += initialString[x]
		print(CheckforWord)
		if CheckforWord == StringToGo:
			#extract from the 1st character (for i – 1 characters) from InitialString into firstPart
			firstPart = ""
			for x in range(0,i):
				firstPart += initialString[x]
			secondPart = ""
			for x in range(i+Lword,LString - Lword + 2):
				secondPart += initialString[x]
			
			newString = firstPart + secondPart
			found = True
		else:
			i += 1
		#Until i>LinitialString or found = True
		if i >=	LString or found == True:
			print(newString)
			break

import random
def printSixUniqueLottoNumbers():
	flag = []
	for i in range(99):
		flag.append(0)
		
	for i in range(6):
		while True:
			r = random.randint(1,99)
			if flag[r] == 0:
				break
		flag[r] = 1
		print(f"Your next number is {r}")
			
def createAFile():
	fn = "friendsData.txt"
	
	f = open(fn,"w")
	for i in range(2):
		fname = input("First Name: ")
		sname = input("Surname: ")
		emailaddr = input("Email: ")
		mobile = input("Mobile Number: ")
		f.write(fname+", "+sname+", "+emailaddr+", "+mobile+"\n")
	f.writelines("xxx,xxx")
	f.close()
	
	
		
#Element, numElements = loadArray2()
#printArray(Element, numElements)
#sumArrayContents(Element, numElements)

#extractDataFromString()

#insertString("first;word","second")
#DeleteWordFromString()
#printSixUniqueLottoNumbers()
createAFile()
input()
