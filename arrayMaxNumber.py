def findMax():
	array = [5,3,8,9]
	largest = array[0]
	i = 1
	maxI = 0
	numElements = len(array)
	while i < numElements:
		if array[i] > largest:
			largest = array[i]
			maxI = i
		i += 1
	print(f"The largest number is {largest} in position {maxI}")
	
	
def findMax2():
	array = [5,3,8,9]
	largest = ""
	maxI = -1
	i = 0
	
	for element in array:
		if element > largest:
			largest = element
			maxI = i
		i += 1
	print(f"The largest number is {largest} in position {maxI}")

def findMax3():
	array = [5,3,8,9]
	largest = ""
	maxI = -1
	numElements = len(array)
	for i in range(numElements):
		if array[i] > largest:
			largest = array[i]
			maxI = i
	print(f"The largest number is {largest} in position {maxI}")
	
def findMin():
	array = [5,3,8,9]
	smallest = array[0]
	i = 1
	minI = 0
	numElements = len(array)
	while i < numElements:
		if array[i] < smallest:
			smallest = array[i]
			minI = i
		i += 1
	print(f"The smallest number is {smallest} in position {minI}")
	
findMax()
findMin()
input()