import math
from random import randint



class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 


class SortedList(object):   
    # Constructor
	def __init__(self,head = None,tail = None):    
		self.head = head
		self.tail = tail

	def Print(self):
		iterNode = self.head
		while iterNode is not None:
			print(iterNode.data)
			iterNode = iterNode.next

	def Insert(self, i):
		#if empty, assign both head and tail to the new node
		if self.head is None:
			self.head = Node(i)
			self.tail = self.head
		else:
			#If value is the least element, assign it as the new head.
			if self.head.data > i:
				newNode = Node(i)
				newNode.next = self.head
				self.head = newNode
			#if value is the greater than any other element, insert at end.
			elif self.tail.data < i:
				newNode = Node(i)
				self.tail.next = newNode
				self.tail = newNode 
			else:
				iterNode = self.head
				#stop when end is reached or when a value greater than i is reached.
				#statement is short circuited to prevent None error
				while iterNode.next is not None and iterNode.next.data < i:
					iterNode = iterNode.next
				else:
					newNode = Node(i)
					newNode.next = iterNode.next
					iterNode.next = newNode

	def Delete(self, i):
		#if list is empty, do nothing
		if self.head is None:
			return
		#if value is larger than the tail or head is greater than i, do nothing, value is not in list.
		elif self.tail.data < i or self.head.data > i:
			return

		#if element to remove is head
		if self.head.data == i:
			#if head is the only data, set both pointers to None
			if self.head is self.tail:
				self.head, self.tail = None, None
			else:
				self.head = self.head.next
		else:
			iterNode = self.head
			while iterNode.next is not self.tail and iterNode.next.data != i:
				iterNode = iterNode.next
			#reached end, could either be because value wasn't found
			#or tail is the value.
			if iterNode.next is self.tail:
				#if tail is value, remove tail, otherwise do nothing 
				if self.tail.data == i:
					self.tail = iterNode
			#next node is node to remove, relink by skipping victim node.
			else:
				iterNode.next = iterNode.next.next

	def Merge(self, M):
		m = M.head
		while m is not None:
			self.Insert(m.data)
			m = m.next

	def IndexOf(self, i):
		#empty list
		if self.head is None:
			return -1
		#if tail is less than i or head is greater than i, it's guaranteed
		#the value isn't in list.
		if self.tail.data < i or self.head.data > i:
			return -1			
		#assumes index starting at 0
		index = 0
		iterNode = self.head

		while iterNode is not None:
			if iterNode.data == i:
				return index
			index += 1
			iterNode = iterNode.next
		return -1 #should never be reached

	def Clear(self):
		self.head, self.tail = None, None

	def Min(self):
		if self.head is None:
			return math.inf
		else:
			return self.head.data

	def Max(self):
		if self.tail is None:
			return -math.inf
		else:
			return self.tail.data

	def HasDuplicates(self):
		if self.head is None:
			return
		iterNode = self.head
		while iterNode.next is not None:
			if iterNode.data == iterNode.next.data:
				return True
			iterNode = iterNode.next
		#ends at iterNode at tail, in that case, there is no duplicates
		return False

	def Select(self, k):
		i = 0
		iterNode = self.head
		while iterNode is not None and i < k:
			iterNode = iterNode.next
			i += 1
		if iterNode is not None:
			return iterNode.data
		else:
			return math.inf







def main():
	L = SortedList()
	print("testing on an empty list")
	print("printing: ")
	L.Print()
	print("Deleting: ")
	L.Delete(2)
	print("index of 3: ", L.IndexOf(3))
	print("min", L.Min())
	print("max", L.Max())
	print("hasDuplicate: ", L.HasDuplicates())
	print("select 0", L.Select(0))
	print()

	print("Inserting 10-0 to list.")
	for i in range(10,0,-1):
		L.Insert(i)
	L.Print()
	print("Inserting a second 5")
	L.Insert(5)
	print("has duplicate: ", L.HasDuplicates())
	print("deleting the 5")
	L.Delete(5)
	print("has duplicate: ", L.HasDuplicates())
	print("Deleting 4 and 12 (12 not in list)")
	L.Delete(4)
	L.Delete(12)
	L.Print()
	print("min", L.Min())
	print("max", L.Max())
	print("kth smallest element, k=3:",L.Select(3))
	print("index of 5 (should be same as k value above)",L.IndexOf(5))
	print()

	M = SortedList()
	for i in range(5):
		M.Insert(randint(0,10))
	print("merging with this randomized sortedList: ")
	M.Print()
	L.Merge(M)
	print("\nmerged list:")
	L.Print()
	print()

	print("clearing list")
	L.Clear()
	L.Print()
	print("min", L.Min())
	print("max", L.Max())

def writeRuntimeCsv(r=100):
	from time import time
	import winsound #so I don't have to stare at code for test to finish

	n = 0  #the size of the list.
	file = open("Runtime.csv","w")
	file.write("n,Insert,Print,Delete,Merge,IndexOf,Clear,Min,Max,HasDuplicates,Select\n")

	for i in range(r):
		n += 1
		
		insertTime = 0
		printTime = 0
		deleteTime = 0
		mergeTime = 0
		indexOfTime = 0
		clearTime = 0
		minTime = 0
		maxTime = 0
		hasDuplicateTime = 0
		selectTime = 0

		#average over 100 times
		for j in range(100):
			SL = SortedList()
			TL = SortedList()
			UL = SortedList()

			for i in range(n+1):
				SL.Insert(randint(0,1000))
				TL.Insert(randint(0,1000))
				UL.Insert(randint(0,1000))
			
			#insert random value
			randVal = randint(0,1000)
			startTime = time()
			SL.Insert(randVal)
			insertTime =+ (time()-startTime)
			SL.Delete(randVal) #remove random value to maintain n size for rest of tests
			
			startTime = time()
			SL.Print()
			printTime =+ (time()-startTime)
			
			startTime = time()
			UL.Delete(randint(0,n))
			deleteTime =+ (time()-startTime)

			startTime = time()
			TL.Merge(SL)
			mergeTime =+ (time()-startTime)

			startTime = time()
			SL.IndexOf(randint(0,n))
			indexOfTime =+ (time()-startTime)

			startTime = time()
			SL.Clear()
			clearTime =+ (time()-startTime)

			startTime = time()
			SL.Min()
			minTime =+ (time()-startTime)	

			startTime = time()
			SL.Max()
			maxTime =+ (time()-startTime)

			startTime = time()
			SL.HasDuplicates()
			hasDuplicateTime =+ (time()-startTime)	

			startTime = time()
			SL.Select(randint(0,n))
			selectTime =+ (time()-startTime)	

		file.write(str(n) + "," + str(insertTime/100) + "," + str(printTime/100) + "," + str(deleteTime/100) + "," + str(mergeTime/100) + "," + str(indexOfTime/100) + "," + str(clearTime/100) + ", " + str(minTime/100) + "," + str(maxTime/100) + "," + str(hasDuplicateTime/100) + "," + str(selectTime/100) + "\n")					
	file.close()
	winsound.Beep(400, 2000)



if __name__ == '__main__':
	main()
	#writeRuntimeCsv(100)