from time import time
import numpy as np
from wordEmbedding import WordEmbedding
from HashTableChaining import HashTableChainWord
from HashTableProbing import HashTableLP

#wordLimit, amount of words to build from glove.  -1 builds entire file
def buildHTChaining(algor = 1, wordLimit = -1):
	try:
		runTime = 0
		#total size of glove file is 400,000 words.  400,009 is the next largest prime number.
		HTC = HashTableChainWord(400009) 
		file = open("glove.6B.50d.txt", encoding="utf8")
		lineCount = 0
		for line in file:
			dataList = line.split(" ") #first element is word, the rest is the float array
			if dataList[0].isalpha():  #only insert if word starts with an alpha character
				if algor == 1:
					startTime = time()
					HTC.insert1(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 2:
					startTime = time()
					HTC.insert2(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime					
				if algor == 3:
					startTime = time()
					HTC.insert3(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 4:
					startTime = time()
					HTC.insert4(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 5:
					startTime = time()
					HTC.insert5(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 6:
					startTime = time()
					HTC.insert6(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime																				
			lineCount += 1
			if lineCount == wordLimit:
				return HTC, runTime
			print(lineCount,end = "\r")
		return HTC,runTime
	except Exception as e:
		print(e)
		HTC.print_table()
		raise e

#wordLimit, amount of words to build from glove.  -1 builds entire file
def buildHTProbing(algor = 1, wordLimit = -1):
	try:
		runTime = 0
		#total size of glove file is 400,000 words.  400,009 is the next largest prime number.
		HTP = HashTableLP(400009) 
		file = open("glove.6B.50d.txt", encoding="utf8")
		lineCount = 0
		for line in file:
			dataList = line.split(" ") #first element is word, the rest is the float array
			if dataList[0].isalpha():  #only insert if word starts with an alpha character
				if algor == 1:
					startTime = time()
					HTP.insert1(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 2:
					startTime = time()
					HTP.insert2(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime					
				if algor == 3:
					startTime = time()
					HTP.insert3(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 4:
					startTime = time()
					HTP.insert4(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 5:
					startTime = time()
					HTP.insert5(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime
				if algor == 6:
					startTime = time()
					HTP.insert6(WordEmbedding(dataList[0],dataList[1:]))
					runTime += time()-startTime																				
			lineCount += 1
			if lineCount == wordLimit:
				return HTP, runTime
			print(lineCount,end = "\r")
		return HTP,runTime

	except Exception as e:
		print(e)
		HTP.print_table()
		raise e




#Does vector calculation to determine how similar words are
def similarities(embed1, embed2):
	return np.dot(embed1.emb, embed2.emb)/(np.linalg.norm(embed1.emb) * np.linalg.norm(embed2.emb))

#reads words from a file and returns a 2-d list of wordEmbedding and
def getEmbeddingsFromFile(T,fileName, algor = 1):
	file = open(fileName)
	runtime = 0
	embeddingsList = []

	for line in file:
		#sliced to remove the newline character, then split by the comma
		if "\n" in line:
			line = line[:-1]
		seachWords = line.split(",")

		#determine algorithm to use
		if algor == 1:
			startTime = time()
			output1 = T.find1(seachWords[0])
			output2 = T.find1(seachWords[1])
			if output1 is None or output2 is None: #if word is not in tree, just appends the string words
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)
		if algor == 2:
			startTime = time()
			output1 = T.find2(seachWords[0])
			output2 = T.find2(seachWords[1])
			if output1 is None or output2 is None: #if word is not in tree, just appends the string words
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)	
		if algor == 3:
			startTime = time()
			output1 = T.find3(seachWords[0])
			output2 = T.find3(seachWords[1])
			if output1 is None or output2 is None: #if word is not in tree, just appends the string words
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)	
		if algor == 4:
			startTime = time()
			output1 = T.find4(seachWords[0])
			output2 = T.find4(seachWords[1])
			if output1 is None or output2 is None: #if word is not in tree, just appends the string words
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)		
		if algor == 5:
			startTime = time()
			output1 = T.find5(seachWords[0])
			output2 = T.find5(seachWords[1])
			if output1 is None or output2 is None: #if word is not in tree, just appends the string words
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)					
		if algor == 6:
			startTime = time()
			output1 = T.find6(seachWords[0])
			output2 = T.find6(seachWords[1])
			if output1 is None or output2 is None: #if word is not in tree, just appends the string words
				embeddingsList.append(seachWords)
			else:
				embeddingsList.append([output1, output2])
			runtime = runtime + (time() - startTime)	
	return embeddingsList, runtime


def main():

	htType = 0
	buildRunTime = 0
	while(int(htType) < 1 or int(htType) > 2):
		print("Choose table for implementation")
		print("\t1. Hash Table Chaining")
		print("\t2. Hash Table Probing")
		htType = input()
	algType = -1
	while(int(algType) < 1 or int(algType) > 6):
		print("Choose algorithm type")
		print("\t1. ")
		print("\t2. ")
		print("\t3. ")
		print("\t4. ")		
		print("\t5. ")		
		print("\t6. ")				
		algType = input()
	hashT = None
	if int(htType) == 1:
		hashT,buildRunTime = buildHTChaining(int(algType), 10000)
	else:
		hashT,buildRunTime = buildHTProbing(int(algType), 10000)

	#find similarities
	print("Reading word file to determine similarities")
	embeddingsList,runtime = getEmbeddingsFromFile(hashT,"wordSimilarities2.txt",int(algType))
	for embed in embeddingsList:
		#pass #used to supress output of similarities
		if any(isinstance(words,str) for words in embed):
			print("Did not find an embedding for {} or {}".format(embed[0], embed[1]))
		else:
			print("Similarity [{},{}] = {}".format(embed[0].word,embed[1].word,similarities(embed[0],embed[1])))

	print("runtime to build",buildRunTime)
	print("runtime to search is, ",runtime)

#used to convert words in glove to format for searching for word similarities.
def convertToCSV(fileName):
	inputFile = open(fileName, encoding="utf8")
	outputFile = open("wordSimilarities2.txt","w")
	word = 0
	lineCount = 0
	for line in inputFile:
		if "\n" in line:
			line = line[:-1]
		line = line.split(" ")[0]
		if line.isalpha():
			if(word == 1):
				outputFile.write(line + "\n")
				word = 0
			else:
				outputFile.write(line + ",")
				word = word + 1
			lineCount += 1
			if lineCount == 12000:
				inputFile.close()
				outputFile.close()
				return

#used to build csv for graph in report
def timeRunner():
	fp = open("htRuntime.csv","w")
	
	for i in range(1,7):
		hashT,buildRunTime = buildHTChaining(int(i), 10000)
		embeddingsList,runtime = getEmbeddingsFromFile(hashT,"wordSimilarities2.txt",int(i))

		fp.write("algorithm " + str(i) + "," + str(buildRunTime) + "," + str(runtime) + "\n")
	for i in range(1,7):
		hashT,buildRunTime = buildHTProbing(int(i), 10000)
		embeddingsList,runtime = getEmbeddingsFromFile(hashT,"wordSimilarities2.txt",int(i))

		fp.write("algorithm " + str(i) + "," + str(buildRunTime) + "," + str(runtime) + "\n")		
	fp.close()


def compareWithBST():
	import lab4
	#binary search tree
	bstBuildTime = 0
	start = time()
	BST = lab4.buildBinaryTree()
	bstBuildTime = time() - start

	bstEmbeddingsList,bstSearchTime = lab4.getEmbeddingsFromFile(BST,"wordSimilarities1.txt")

	#hash table with chaining
	HTC, htcBuildTime= buildHTChaining(5)
	htcEmbeddingsListHTC,htcSearchTime = getEmbeddingsFromFile(HTC,"wordSimilarities1.txt")

	print("runtimes (build and search) BST: ",bstBuildTime,bstSearchTime)
	print("runtimes (build and search) HTC: ",htcBuildTime,htcSearchTime)


if __name__ == '__main__':
	main()
	#convertToCSV("glove.6B.50d.txt")
	#timeRunner()
	#compareWithBST()
