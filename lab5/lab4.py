from time import time
from wordEmbedding import WordEmbedding
import numpy as np
import binarySearchTree as BST
import btree


def buildBinaryTree():
	try:
		file = open("glove.6B.50d.txt", encoding="utf8")
		BT = None

		for line in file:
			dataList = line.split(" ") #first element is word, the rest is the float array
			if dataList[0].isalpha():  #if word starts with an alpha character
				BT = BST.Insert(BT, dataList[0], dataList[1:])

		return BT
	except Exception as e:
		print(e)
		print(line)
		raise e

#inputs the max number of elements allowed in a node
def buildBTree(maxValue):
	try:
		file = open("glove.6B.50d.txt", encoding="utf8")
		B_T = btree.BTree([],max_data=maxValue) 

		for line in file:
			dataList = line.split(" ")
			if dataList[0].isalpha():
				btree.Insert(B_T, WordEmbedding(dataList[0], dataList[1:]))

		return B_T
	except Exception as e:
		print(e)
		raise e


#reads words from a file and returns a 2-d list of wordEmbedding and
def getEmbeddingsFromFile(T,fileName):
	file = open(fileName)
	runtime = 0
	embeddingsList = []

	for line in file:
		#sliced to remove the newline character, then split by the comma
		if "\n" in line:
			line = line[:-1]
		seachWords = line.split(",")

		#determine type of tree is inputted
		if type(T) == BST.BST:
			startTime = time()
			output1 = BST.Search(T, seachWords[0])
			output2 = BST.Search(T, seachWords[1])
			if output1 is None or output2 is None: #if word is not in tree, just appends the string words
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)
		elif type(T) == btree.BTree:
			startTime = time()
			output1 = btree.Search(T, seachWords[0])
			output2 = btree.Search(T, seachWords[1])
			if output1 is None or output2 is None:
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)

	return embeddingsList, runtime


#Does vector calculation to determine how similar words are
def similarities(embed1, embed2):
	return np.dot(embed1.emb, embed2.emb)/(np.linalg.norm(embed1.emb) * np.linalg.norm(embed2.emb))



def main():
	fileName = ""
	inp = 0
	while(int(inp) < 1 or int(inp) > 2):
		print("Choose table for implementation")
		print("\t1. binary search")
		print("\t2. B-Tree")
		inp = input()

	#Build binary search tree
	if int(inp) == 1:
		print("\nBuilding binary tree")
		startTime = time()
		table = buildBinaryTree()
		endTime = time()

		print("Number of nodes:",BST.Size(table))
		print("Height of tree",BST.Height(table))
		print("Time to build binary tree:",str(endTime-startTime))
		print()

		embeddingsList = getEmbeddingsFromFile(table,"wordSimilarities.txt")

	#Build b-tree
	if int(inp) == 2:
		maxValue = 0
		while maxValue < 3 or maxValue%2 == 0:
			print("Enter the maximum number of values in a node (value must be odd and greater or equal to 3): ", end = " ")
			maxValue = int(input())
		print("\nBuilding b-tree")
		startTime = time()
		table = buildBTree(maxValue)
		endTime = time()
		
		print("Number of nodes:",btree.Size(table))
		print("Height of tree",btree.Height(table))
		print("Time to build binary tree (with maxvalue of", maxValue, "):",str(endTime-startTime))

	#find similarities
	print("Reading word file to determine similarities")
	embeddingsList,runtime = getEmbeddingsFromFile(table,"wordSimilarities1.txt")
	for embed in embeddingsList:
		#pass #used to supress output of similarities
		if any(isinstance(words,str) for words in embed):
			print("Did not find an embedding for {} or {}".format(embed[0], embed[1]))
		else:
			print("Similarity [{},{}] = {}".format(embed[0].word,embed[1].word,similarities(embed[0],embed[1])))

	print("runtime is, ",runtime)


#used to convert a file with words on each line to a file of two words on each line.  This is the format for searching two words.
def convertToCSV(fileName):
	inputFile = open(fileName)
	outputFile = open("wordSimilarities1.txt","w")
	word = 0
	for line in inputFile:
		if "\n" in line:
			line = line[:-1]
		if(word == 1):
			outputFile.write(line + "\n")
			word = 0
		else:
			outputFile.write(line + ",")
			word = word + 1

#used to build csv for graph in report
def buildRunner():
	fp = open("btBuild.csv","w")
	for maxnum in range(3,21,2):
		startTime = time()
		table = buildBTree(maxnum)
		endTime = time()
		fp.write(str(maxnum) + "," + str(endTime - startTime) + "\n")
	fp.close()

#used to build csv for graph in report
def searchRunner():
	fp = open("btSearch.csv","w")
	for maxnum in range(3,21,2):
		table = buildBTree(maxnum)
		embeddingsList,runtime = getEmbeddingsFromFile(table,"wordSimilarities1.txt")
		fp.write(str(maxnum) + "," + str(runtime) + "\n")
	fp.close()	

if __name__ == '__main__':
	#convertToCSV("google-10000-english-no-swears.txt")
	main()
	#bulidRunner()
	#searchRunner()