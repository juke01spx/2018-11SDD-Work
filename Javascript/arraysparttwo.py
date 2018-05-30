def addUp(array):
	sum = 0
	for n in array:
		sum += int(n)
	return sum
	
def aver(array):
	sum = addUp(array)
	num = len(array)
	av = sum / num
	return av
	
def biggest(array):
	big = array[0]
	x = 0
	for i in range(1,len(array)):
		n = array[i]
		if int(n)> big:
			big = n
			x=i
	return x, big
	
	
def smallest(array):
	small = array[0]
	x = 0
	for i in range(1,len(array)):
		n = array[i]
		if int(n)< small:
			small = n
			x=i
	return x, small
	
###############################################

array = [10,2,1,4,5,6,7,8,9,3]

sum addUp(array)
av = aver(array)
b, big = biggest(array)
s, small = smallest(array)

print(f"Array {array}, Sum={sum}, Average={av}")
print(f"Largest number in array is {big} in {b} index location")
print(f"Smallest number in array is {small} in {s} index location")