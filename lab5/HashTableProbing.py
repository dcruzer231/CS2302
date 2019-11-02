# Implementation of hash tables with linear probing
# Programmed by Olac Fuentes
# Last modified October 10, 2019

import numpy as np
from wordEmbedding import WordEmbedding

class HashTableLP(object):
    # Builds a hash table of size 'size', initilizes items to -1 (which means empty)
    # Constructor
    def __init__(self,size):  
        self.item = np.zeros(size,dtype=WordEmbedding)-1
        
    def insert(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h(k+i)
            if self.item[pos] < 0:
                self.item[pos] = k
                return pos
        return -1

    def insert1(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h(len(k.word)+i)
            if self.item[pos] < 0:
                self.item[pos] = k
                return pos
        return -1        
    
    def find1(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h(len(k)+i)
            if self.item[pos] == k:
                return self.item[pos]
            if self.item[pos] == -1:
                return None
        return None

    def insert2(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h(ord(k.word[0])+i)
            if self.item[pos] < 0:
                self.item[pos] = k
                return pos
        return -1  

    def find2(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h(ord(k[0])+i)
            if self.item[pos] == k:
                self.item[pos]
            if self.item[pos] == -1:
                return None
        return None

    def insert3(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h((ord(k.word[0]) * ord(k.word[-1]))+i)
            if self.item[pos] < 0:
                self.item[pos] = k
                return pos
        return -1 

    def find3(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h((ord(k[0]) * ord(k[-1]))+i)
            if self.item[pos] == k:
                return self.item[pos]
            if self.item[pos] == -1:
                return None
        return None

    def insert4(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        runSum = 0
        for l in k.word:
            runSum += ord(l)

        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h(runSum+i)
            if self.item[pos] < 0:
                self.item[pos] = k
                return pos
        return -1 

    def find4(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        runSum = 0
        for l in k:
            runSum += ord(l)

        for i in range(len(self.item)):
            pos = self.h(runSum+i)
            if self.item[pos] == k:
                return self.item[pos]
            if self.item[pos] == -1:
                return None
        return None

    def insert5(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h5(k.word,len(self.item)) + i
            if self.item[pos] < 0:
                self.item[pos] = k
                return pos
        return -1 


    def find5(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h5(k,len(self.item)) + i
            if self.item[pos] == k:
                return self.item[pos]
            if self.item[pos] == -1:
                return None
        return None

    def insert6(self,k):
        # Inserts k in table unless table is full
        # Returns the position of k in self, or -1 if k could not be inserted
        for i in range(len(self.item)): #Despite for loop, running time should be constant for table with low load factor
            pos = self.h6(k.word) + i
            if self.item[pos] < 0:
                self.item[pos] = k
                return pos
        return -1 

    def find6(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h6(k) + i
            if self.item[pos] == k:
                return self.item[pos]
            if self.item[pos] == -1:
                return None
        return None

    def find(self,k):
        # Returns the position of k in table, or -1 if k is not in the table
        for i in range(len(self.item)):
            pos = self.h(k+i)
            if self.item[pos] == k:
                return pos
            if self.item[pos] == -1:
                return -1
        return -1
     
    def delete(self,k):
        # Deletes k from table. It returns the position where k was, or -1 if k was not in the table
        # Sets table item where k was to -2 (which means deleted)
        f = self.find(k)
        if f >=0:
            self.item[f] = -2
        return f
    
    def h(self,k):
        return k%len(self.item)  
            
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
        return runSum % len(self.item)                

    def print_table(self):
        print('Table contents:')
        print(self.item)

    def load(self):
        return (self.item > -1).sum() / len(self.item)

    def collisions(self):
        collisionCount = 0
        for i in range(len(self.item)):
            if self.h(self.item[i]) != i:
                collisionCount += 1
        return collisionCount

    def findOptimized(self):
        # Returns the position of k in table, or -1 if k is not in the table
        firstDeletion = -1
        for i in range(len(self.item)):
            pos = self.h(k+i)
            if self.item[pos] == k:
                if firstDeletion != -1:
                    self.item[pos] = -2
                    self.item[firstDeletion] = k
                    return firstDeletion
            else:
                return pos
            if self.item[pos] == -1:
                return -1
            if self.item[pos] == -2 and firstDeletion == -1:
                firstDeletion = pos
        return -1        
            
def main():
    h = HashTableLP(11)
    A = [23,5,7,9,12,32,45,22]
   
    for a in A:
        h.insert(a)
        print('Insert',a)
    h.print_table()
        
    h.delete(22)
    h.print_table()
    print(h.load())
    print(h.collisions())
    
if __name__ == "__main__":    
    main()
    