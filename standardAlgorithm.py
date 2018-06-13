
def loadArray():
	i = 0
	Element = []
	dataValue = input('Enter data value, XXX to finish')
	while dataValue.upper() != "XXX":
		Element.append(dataValue)
		i += 1
		dataValue = input('Enter data value, XXX to finish')
	numElements = i
	print(f"There are {numElements} items loaded into array")
	return Element, numElements
	input()
	
def loadArray2():
	i = 0
	Element = []
	while True:
		dataValue = input('Enter data value, XXX to finish')
		if dataValue.upper() == "XXX":
			break
		Element.append(dataValue)
		i += 1
	numElements = i
	print(f"There are {numElements} items loaded into array")
	return Element, numElements
	input()

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
	input()
	
Element, numElements = loadArray2()
printArray(Element, numElements)
sumArrayContents(Element, numElements)