# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified October 2, 2019
import matplotlib.pyplot as plt
import numpy as np
from wordEmbedding import WordEmbedding

class BST(object):
    def __init__(self, word = None, embedding = None, left=None, right=None):  
        if word is not None and embedding is not None:
            self.data = WordEmbedding(word, embedding)
        else:
            self.data = None
        self.left = left 
        self.right = right      

def Insert(T, word, embedding):
    if T is None:
        T = BST(word, embedding)
    elif word <= T.data.word :
        T.left = Insert(T.left, word, embedding)
    else:
        T.right = Insert(T.right,word,embedding)
    return T

def Search(T, word):
    if T is None:
        return None    
    elif T.data.word == word:
        return T.data
    elif word < T.data.word:
        return Search(T.left, word)
    else:
        return Search(T.right, word)

def PrintInOrder(T):
    if T is not None:
        PrintInOrder(T.left)
        print(T.data.word, T.data.emb)
        PrintInOrder(T.right)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def Insert(T,newItem):
#     if T == None:
#         T =  BST(newItem)
#     elif T.data > newItem:
#         T.left = Insert(T.left,newItem)
#     else:
#         T.right = Insert(T.right,newItem)
#     return T

def DrawBST_(T, x0, x1, y, y_inc,ax):
    if T is not None:
        xm = (x0+x1)/2
        yn = y-y_inc
        if T.left is not None:
            p=np.array([[xm,y], [(x0+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.left,x0,xm,yn, y_inc,ax)
        if T.right is not None:
            p=np.array([[xm,y], [(x1+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.right,xm,x1,yn, y_inc,ax)
        ax.text(xm,y, str(T.data), size=10,ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))

def DrawBST(T): 
    fig, ax = plt.subplots()
    DrawBST_(T, 0, 200, 400, 20, ax)
    ax.set_aspect(1.0)
    ax.axis('off') 
    plt.show() 


    
# def printInOrder(T):
#     if T is not None:
#         printInOrder(T.left)
#         print(T.data)
#         printInOrder(T.right)


def Min(T):
    if T.left is not None:
        return Min(T.left)
    else:
        return T

def Max(T):
    if T.right is not None:
        return Max(T.right)
    else:
        return T

# def search(T,k):
#     if T is not None:
#         if T.data > k:
#             return search(T.left, k)
#         elif T.data < k:
#             return search(T.right, k)
#         else:
#             return T
#     else:
#         return None
def Size(T):
    if T is None:
        return 0
    else:
        return 1 + Size(T.left) + Size(T.right)

def Height(T):
    if T is None:
        return -1
    else:
        return 1 + max(Height(T.left), Height(T.right))

def DepthOfK(T,k):
    if T == None:
        return -1
    if T.data == k:
        return 0
    if k < T.data:
        d = DepthOfK(T.left, k) + 1
    else:
        d = DepthOfK(T.right, k) + 1
    if d == -1:
        return -1
    return d+1

def PrintByDepth(T):
 Q = [T]
 while len(Q) > 0:
    front = Q.pop(0)
    if front is not None:
        print(front.data)
        Q.append(front.left)
        Q.append(front.right)

def ListToTree(L):
    if len(L) == 0:
        return None
    mid = Len(L)//2
    #return BST(L[mid], ListToTree(L[:mid]) ListToTree(L[mid-1:]))

def TreeToList(T):
    if T == None:
        return []
    else:
        return TreeToList(T.left) + [T.data] + TreeToList(T.right)

if __name__ == "__main__":  
    plt.close('all')
    T = None
    A = [40, 70, 50, 60, 20, 80, 30, 10, 90]
    for a in A:
        T = Insert(T,a)

    printInOrder(T)
    print("min", Min(T).data)
    print("max", Max(T).data)
    print("finding 30 ", search(T,30).data)    
    print("size", size(T))
    print("height", height(T))
    print("80 is at depth, ", DepthOfK(T,80))
    PrintByDepth(T)
    DrawBST(T)
