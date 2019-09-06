from time import time

def getWords1(fileName):
	try:
		fp = open(fileName)
		wordSet = set()
		for word in fp:
			#remove newline character from word
			word = word.replace('\n', '')
			wordSet.add(word)
		return wordSet
	except IOError as e:
		print(e)
		return set() #return empty set on IO error

def getWords2(fileName):
	try:
		fp = open(fileName)
		wordSet = set()
		strSet = set()
		for word in fp:
			word = word.replace('\n', '')
			#for each word, add a running prefix to a different set.
			for i in range(len(word)):
				strSet.add(word[:i])
			wordSet.add(word)
		return wordSet, strSet
	except IOError as e:
		print(e)
		return set()


#These recusive methods are based off and adapted from zybooks section 2.6
def scramble1(r_letters, wordSet, returnSet, s_letters = ""):
	#base case
	if len(r_letters) == 0:
		if(s_letters in wordSet):
			returnSet.add(s_letters)
	#recursive case
	else:
		#for each letter in the string, add it to a different string, remove it from the previous string,
		#then recusively repeat the process
		for i in range(len(r_letters)):
			scramble_letter = r_letters[i]
			remaining_letters = r_letters[:i] + r_letters[i+1:]
			scramble1(remaining_letters, wordSet, returnSet, s_letters+scramble_letter)

def scramble2(r_letters, wordSet, prefixSet, returnSet, s_letters = ""):
	#base case
	if len(r_letters) == 0:
		if(s_letters in wordSet):
			returnSet.add(s_letters)
	#recusive case
	else:
		#for each letter in the string, add it to a different string, remove it from the previous string,
		#then recusively repeat the process		
		usedLetters = set()
		for i in range(len(r_letters)):
			scramble_letter = r_letters[i]
			remaining_letters = r_letters[:i] + r_letters[i+1:]
			#If this is not the end of the string and the prefix is found in the set of word prefixes, then recusively continue.
			#otherwise finish this iteration of the for loop here without continueing recursion
			if((len(remaining_letters) != 0) and not ((s_letters+scramble_letter) in prefixSet)):
				continue
			#if the letter chosen to be appended has already been used, stop this iteration for the for loop without recursion
			#else add letter to the set and continue forth.
			if(scramble_letter in usedLetters):
				continue
			usedLetters.add(scramble_letter)
			scramble2(remaining_letters, wordSet, prefixSet, returnSet, s_letters+scramble_letter)

def printAnagram1(word, wordSet):
	#will be used to calculate runtime.
	startTime = time()
	#an empty set to store anagrams found from the recursive function
	anagramSet = set()
	scramble1(word, wordSet, anagramSet)
	endTime = time()
	if(len(anagramSet) == 0):
		print("The word, " + word + "  has no anagrams.")
	else:
		#convert to list for sorting
		anagramList = list(anagramSet)
		#if the inputted word is found in the anagram list, remove it.
		if word in anagramList:
			anagramList.remove(word)
		#sorts anagram list alphabetically
		anagramList.sort()
		print("The word " + word + " has " + str(len(anagramList)) + " anagrams:")
		for anagram in anagramList:
			print("\t" + anagram)
	print("It took, " + str(endTime - startTime) + " seconds to find all the anagrams.")

def printAnagram2(word, wordSet, prefixSet):
	#will be used to calculate runtime.
	startTime = time()
	wordList = list(word)
	#an empty set to store anagrams found from the recursive function	
	anagramSet = set()
	scramble2(word, wordSet, prefixSet, anagramSet)
	endTime = time()
	if(len(anagramSet) == 0):
		print("The word, " + word + "  has no anagrams.")
	else:
		#convert to list for sorting
		anagramList = list(anagramSet)
		#if the inputted word is found in the anagram list, remove it.		
		if word in anagramList:
			anagramList.remove(word)
		#sorts anagram list alphabetically		
		anagramList.sort()
		print("The word " + word + " has " + str(len(anagramList)) + " anagrams:")
		for anagram in anagramList:
			print("\t" + anagram)
	print("It took, " + str(endTime - startTime) + " seconds to find all the anagrams.")


def main1():
	wordSet = getWords1("words_alpha.txt")
	userInput = None
	while userInput != "":
		print("Enter a word or empty string to finish: ", end = "")
		userInput = input()
		if(userInput != ""):
			printAnagram1(userInput, wordSet)
	print("exiting program, thanks for using this program!")

def main2():
	wordSet, prefixSet = getWords2("words_alpha.txt")
	userInput = None
	while userInput != "":
		print("Enter a word or empty string to finish: ", end = "")
		userInput = input()
		if(userInput != ""):
			printAnagram2(userInput, wordSet, prefixSet)
	print("exiting program, thanks for using this program!")


if __name__ == '__main__':
	main1()
	#main2()