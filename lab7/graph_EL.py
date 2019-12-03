# Edge list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, source, dest, weight=1):
        self.source = source
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self,  vertices, weighted=False, directed = False):
        self.vertices = vertices
        self.el = []
        self.weighted = weighted
        self.directed = directed
        self.representation = 'EL'
        
    def insert_edge(self,source,dest,weight=1):
        self.el.append(Edge(source, dest, weight))
    
    def delete_edge(self,source,dest):
        for edge in self.el:
            if source == edge.source:
                if dest == edge.dest:
                    self.el.remove(edge)       
                
    def display(self):
        print("[",end = "")
        for e in self.el:
            print("[" + str(e.source), str(e.dest), str(e.weight) + "]", end = " ")
        print("\b]") #backspace one to delete unneeded ending space
     
    def draw(self):
        self.as_AL().draw()
            
    def as_EL(self):
        return self
    
    def as_AM(self):
        from graph_AM import Graph
        AM = Graph(self.vertices, self.weighted, self.directed)
        for edge in self.el:
            AM.insert_edge(edge.source, edge.dest, edge.weight)
        return AM

    
    def as_AL(self):
        from graph_AL import Graph
        AL = Graph(self.vertices, self.weighted, self.directed)
        for edge in self.el:
            AL.insert_edge(edge.source, edge.dest, edge.weight)
        return AL

    def depthFirstSearch(self,start,end):
        fronteirStack = [start]
        discoveredSet = [start]
        path = [-1]*16
        while fronteirStack:
            vertex = fronteirStack.pop()
            for edge in self.el:
                if edge.source == vertex and edge.dest not in discoveredSet:
                    fronteirStack.append(edge.dest)
                    discoveredSet.append(edge.dest)
                    path[edge.dest] = edge.source 
        return path 

    def breadthFirstSearch(self, start, end):
        frontierQ = [start]
        discoveredSet = [start]
        path = [-1]*16
        while frontierQ:
            vertex = frontierQ.pop(0)
            for edge in self.el:
                if edge.source == vertex and edge.dest not in discoveredSet:
                    frontierQ.append(edge.dest)
                    discoveredSet.append(edge.dest)
                    path[edge.dest] = edge.source 
        return path

    def printPath(self, path, dest):
        if path[dest] != -1:
            self.printPath(path, path[dest])
            print(dest, end = " ")
        else:
            print(dest, end = " ")
            return -1


    def printBreadthPath(self, start, end):
        path = self.breadthFirstSearch(start, end)
        self.printPath(path, end)
        print()

    def printDepthPath(self, start, end):
        path = self.depthFirstSearch(start, end)
        self.printPath(path, end)
        print()        