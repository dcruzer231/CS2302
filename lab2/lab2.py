from random import randint
from collections import deque


"""			BUBBLE 			"""
#counts comparisons.
bubbleCount = 0
def select_bubble(L,k):
	global bubbleCount
	if len(L) == 0 or k > (len(L) - 1):
		return None
	sorted = False
	while(not sorted):
		#set to true, will be set to false if a nonsorted section is found.
		sorted = True
		for i in range(len(L)-1):
			bubbleCount += 1
			if(L[i] > L[i+1]):
				L[i], L[i+1] = L[i+1], L[i]
				sorted = False;
	return L[k]

"""			SELECT_QUICK 			"""
quickCount = 0
def select_quick(L,k):
	global quickCount
	if len(L) == 0 or k > (len(L) - 1):
		return None
	recurs_quick(L, 0, len(L)-1)
	return L[k]

#recusion function
def recurs_quick(L,low,high):
	global quickCount
	#list of 1 is already sorted
	if high <= low:
		return
	else:
		lInd = low+1 #left index, low itself is reserved for the pivot
		rInd = high #right index
		while(lInd <= rInd):
			#decrement down the list until value less than pivot is found.
			quickCount += 1
			while rInd > low and L[rInd] >= L[low]:
				quickCount += 1
				rInd -= 1			
			#increment left until value is found greater than pivot
			quickCount += 1
			while lInd < high+1 and L[lInd] < L[low]:
				quickCount += 1
				lInd += 1
			#as long as indexes dont cross, swap the values
			if lInd < rInd:
				L[lInd], L[rInd] = L[rInd], L[lInd]
				rInd -= 1
				lInd += 1
		L[rInd], L[low] = L[low], L[rInd] #place pivot in the middle
		mid = rInd
		recurs_quick(L, low, mid)
		recurs_quick(L, mid+1, high)


"""			SELECT_MODIFIED_QUICK			"""
modifiedQuickCount = 0
def select_modified_quick(L,k):
	global modifiedQuickCount

	modifiedQuickCount += 1
	if len(L) == 0 or k > (len(L) - 1):
		return None
	rec_modified_quick(L, 0, len(L)-1, k)
	return L[k]


def rec_modified_quick(L,low,high, k):
	global modifiedQuickCount
	
	#list of 1 is already sorted
	if high <= low:
		return
	else:
		lInd = low+1 #left index, low itself is reserved for the pivot
		rInd = high #right index
		while(lInd <= rInd):
			
			#decrement down the list until value less than pivot is found.
			modifiedQuickCount += 1
			while rInd > low and L[rInd] >= L[low]:
				modifiedQuickCount += 1
				rInd -= 1			
			
			#increment left until value is found greater than pivot
			modifiedQuickCount += 1
			while lInd < high+1 and L[lInd] < L[low]:
				modifiedQuickCount += 1
				lInd += 1
			
			#as long as indexes dont cross, swap the values
			if lInd < rInd:
				L[lInd], L[rInd] = L[rInd], L[lInd]
				rInd -= 1
				lInd += 1
		L[rInd], L[low] = L[low], L[rInd] #place pivot in the middle
		mid = rInd

		modifiedQuickCount += 1 #one comparison for first if
		if k < mid:
			rec_modified_quick(L, low, mid, k)
		elif k > mid:
			modifiedQuickCount += 1 #second comparison for elif
			rec_modified_quick(L, mid+1, high, k)
		else:
			modifiedQuickCount += 1 #second comparison for elif
			return mid

"""			SELECT_QUICK W/ STACK 			"""
quickStackCount = 0
#Implementing a stack for quicksort
def select_quickStack(L,k):
	global quickStackCount
	if len(L) == 0 or k > (len(L) - 1):
		return None	
	stack = deque()
	low = 0
	high = len(L)-1
	#flag values to indicated end of stack
	stack.append(0)	#low
	stack.append(-1)#high
	#checks if there are elements in the stack
	while stack:
		
		while low < high:

			lInd = low+1 #left index, low itself is reserved for the pivot
			rInd = high #right index
			
			while(lInd <= rInd):

				#decrement down the list until value less than pivot is found.
				quickStackCount += 1
				while rInd > low and L[rInd] >= L[low]:
					quickStackCount += 1
					rInd -= 1			
				#increment left until value is found greater than pivot
				quickStackCount += 1
				while lInd < high+1 and L[lInd] < L[low]:
					quickStackCount += 1
					lInd += 1
				#as long as indexes dont cross, swap the values
				if lInd < rInd:
					L[lInd], L[rInd] = L[rInd], L[lInd]
					rInd -= 1
					lInd += 1
			L[rInd], L[low] = L[low], L[rInd] #place pivot in the middle
			mid = rInd
			#save these values for later to sort this section of the list.  (second recusion call)
			stack.append(mid+1) #low
			stack.append(high)	#high
			#begin low to mid partitions for sorting (first recusion call)
			high = mid
		high = stack.pop()
		low = stack.pop()
	return L[k]



"""			SELECT_MODIFIED_QUICK W/ WHILE 			"""
whileQuickCount = 0
#select_modified_quick with just a while loop
def while_modified_quick(L,k):
	global whileQuickCount

#	whileQuickCount += 1
	if len(L) == 0 or k > (len(L) - 1):
		return None
	low = 0
	high = len(L)-1

	#function will eventually leave while loop through return statement
	while True:
		lInd = low+1 #left index, low itself is reserved for the pivot
		rInd = high #right index

		while(lInd <= rInd):			
			#decrement down the list until value less than pivot is found.
			whileQuickCount += 1
			while rInd > low and L[rInd] >= L[low]:
				whileQuickCount += 1
				rInd -= 1			
			
			#increment left until value is found greater than pivot
			whileQuickCount += 1
			while lInd < high+1 and L[lInd] < L[low]:
				whileQuickCount += 1
				lInd += 1

			#as long as indexes dont cross, swap the values
			if lInd < rInd:
				L[lInd], L[rInd] = L[rInd], L[lInd]
				rInd -= 1
				lInd += 1
		L[rInd], L[low] = L[low], L[rInd] #place pivot in the middle
		mid = rInd

		whileQuickCount += 1
		if k < mid:
			high = mid
		elif k > mid:
			whileQuickCount += 1
			low = mid+1
		else:
			whileQuickCount += 1
			return L[mid]



"""			FUNCTIONS FOR TESTING ALL FUNCTIONS 			"""
def randomList(n = randint(0,10)):
	L = [None] * n
	return [randint(-1000,1000) for element in L]

def randomListDebug():
	for p in range(1000):
		R = randomList()
		for i in range(len(R)):
			quick = select_quick(R.copy(),i)
			modQuick = select_modified_quick(R.copy(), i)
			bubble = select_bubble(R.copy(), i)
			stackQuick = select_quickStack(R.copy(), i)
			whileQuick = while_modified_quick(R.copy(), i)
			sortedList = R.copy().sort()
			if(quick != modQuick and quick != bubble and modQuick != bubble and quick != stackQuick and quick != whileQuick and quick != sortedList[i]):
				print("error, values do not match up or incorrect: ", quick, modQuick, bubble, sortedList[i])

def printOutput():
	L = randomList()
	k = 3
	print("List: " + str(L))
	print("bubble sort: value in position",k,"is ",select_bubble(L.copy(),k))
	print("quicksort: value in position",k,"is ",select_quick(L.copy(),k))
	print("modified quicksort, value in position",k,"is ",select_modified_quick(L.copy(),k))
	print("stack quicksort, value in position",k,"is ",select_quickStack(L.copy(),k))
	print("modified quicksort with while: value in position",k,"is ",while_modified_quick(L.copy(),k))

	L.sort()
	print("sorted List " + str(L))

"""			FUNCTIONS FOR TESTING NUMBER OF COMPARISONS				"""
def resetComparisons():
	global bubbleCount
	global quickCount
	global modifiedQuickCount
	global quickStackCount
	global whileQuickCount

	bubbleCount = 0
	quickCount = 0
	modifiedQuickCount = 0
	quickStackCount = 0
	whileQuickCount = 0

def checkComparisons(n=1):
	global bubbleCount
	global quickCount
	global modifiedQuickCount
	global quickStackCount
	global whileQuickCount
	quick = 0
	modQuick = 0
	bubble = 0
	stackQuick = 0
	whileQuick = 0

	for i in range(n):
		resetComparisons()
		R = randomList()
		select_quick(R.copy(),0)
		quick += quickCount
		select_modified_quick(R.copy(), 0)
		modQuick += modifiedQuickCount
		select_bubble(R.copy(), 0)
		bubble += bubbleCount
		select_quickStack(R.copy(), 0)
		stackQuick += quickStackCount
		while_modified_quick(R.copy(), 0)
		whileQuick += whileQuickCount
	
	print("'Bubble Sort'", "'Quick Sort'", "'Modified Quick Sort'", "'Stack Quick Sort'", "'Modified Quick Sort with while'")
	print(bubble//n, "            ", quick//n, "                 ", modQuick//n, "            ", stackQuick//n, "                  ", whileQuick//n)


#print to file the number of comparisons based on incrementing list size.
def iterateSize(n = 1):
	global bubbleCount
	global quickCount
	global modifiedQuickCount
	global quickStackCount
	global whileQuickCount
	quick = 0
	modQuick = 0
	bubble = 0
	stackQuick = 0
	whileQuick = 0

	fp = open("comparisons.csv",'w')
	
	fp.write("'Bubble Sort', 'Quick Sort', 'Modified Quick Sort', 'Stack Quick Sort', 'Modified Quick Sort with while'\n")
	for i in range(n):
		resetComparisons()
		R = randomList(i)
		select_quick(R.copy(),0)
		quick += quickCount
		select_modified_quick(R.copy(), 0)
		modQuick += modifiedQuickCount
		select_bubble(R.copy(), 0)
		bubble += bubbleCount
		select_quickStack(R.copy(), 0)
		stackQuick += quickStackCount
		while_modified_quick(R.copy(), 0)
		whileQuick += whileQuickCount
		fp.write(str(bubbleCount) + ", " + str(quickCount) + ", " + str(modifiedQuickCount) + ", " + str(quickStackCount) + ", " + str(whileQuickCount) + "\n")



if __name__ == '__main__':
	printOutput()
	#randomListDebug()
	#checkComparisons(10000)
	#iterateSize(30)