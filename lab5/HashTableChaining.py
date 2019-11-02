from wordEmbedding import WordEmbedding

# Implementation of hash tables with chaining
# Programmed by Olac Fuentes
# Last modified October 9, 2019

class HashTableChainWord(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.bucket = [[] for i in range(size)]

    def h(self,k):
        return k%len(self.bucket)   

    def h5(self,S,n):
        if len(S) == 0:
            return 1
        else:
            return (ord(S[0]) + 255*self.h5(S[1:],n))%n

    def h6(self,S):
        runSum = 0
        while len(S) > 0:
            runSum += ord(S[0])<<8 | len(S)
            S = S[1:]
        return runSum % len(self.bucket) 

    def insert1(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h(len(k.word))
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end
    
    def find1(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(len(k))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None #i = -1
        #return self.bucket[b][i] #return b, i

    def insert2(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h(ord(k.word[0]))
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end

    def find2(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(ord(k[0]))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None #i = -1
        #return self.bucket[b][i] #return b, i

    def insert3(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h(ord(k.word[0]) * ord(k.word[-1]))
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end

    def find3(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(ord(k[0]) * ord(k[-1]))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None #i = -1
        #return self.bucket[b][i] #return b, i

    def insert4(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        runSum = 0
        for l in k.word:
            runSum += ord(l)
        b = self.h(runSum)
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end

    def find4(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        runSum = 0
        for l in k:
            runSum += ord(l)
        b = self.h(runSum)
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None #i = -1
        #return self.bucket[b][i] #return b, i

    def insert5(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h5(k.word,len(self.bucket))
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end

    def find5(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h5(k,len(self.bucket))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None #i = -1
        #return self.bucket[b][i] #return b, i
   
    def insert6(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h6(k.word)
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end

    def find6(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h6(k)
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None #i = -1

    def print_table(self):
        print('Table contents:')
        for b in self.bucket:
            print(b)


class HashTableChain(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.bucket = [[] for i in range(size)]
        
    def h(self,k):
        return k%len(self.bucket)    
            
            
    def insert(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h(k)
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end
            
    def find(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(k)
        try:
            i = self.bucket[b].index(k)
        except:
            i = -1
        return b, i
     
    def print_table(self):
        print('Table contents:')
        for b in self.bucket:
            print(b)
    
    def delete(self,k):
        # Returns k from appropriate list
        # Does nothing if k is not in the table
        # Returns 1 in case of a successful deletion, -1 otherwise
        b = self.h(k)
        try:
            self.bucket[b].remove(k)
            return 1
        except:
            return -1

    def load(self):
        totalValues = 0
        for b in self.bucket:
            totalValues = totalValues + len(b)
        return totalValues/len(self.bucket)

    def longestChain(self):
        maxlength = 0
        for b in self.bucket:
            if len(b) > maxlength:
                maxlength = len(b)
        return maxlength

    def verify(self):
        for i in range(len(self.bucket)):
            for d in self.bucket[i]:
                if self.h(d) != i:
                    return False
        return True

    def insertFront(self,k):
        # Inserts k in appropriate bucket (list) at the front of list
        # Does nothing if k is already in the table
        b = self.h(k)
        if not k in self.bucket[b]:
            self.bucket[b].insert(0,k)         #Insert new item at the front
    
    def findOptimized(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(k)
        try:
            i = self.bucket[b].index(k)
        except:
            i = -1
        return b, i

def main():
    h = HashTableChain(7)
    A = [12,3, 21, 14, 11, 8, 9, 7, 6, 1, 22, 19, 35]
    for a in A:
        h.insert(a)
    h.print_table()
    print(h.find(19))
    print(h.find(15))
    h.delete(14)
    h.delete(19)
    h.print_table()
    print("load",h.load())
    print("longest running time",h.longestChain())
    print("verify hash table",h.verify())
    h.insertFront(15)
    h.print_table()
    
if __name__ == "__main__":    
    main()
    
    
    
    