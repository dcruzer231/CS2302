import graph_AL as ALG
import graph_AM as AMG
import graph_EL as ELG

def buildGraphs():
	vertices = 16
	weighted = False
	directed = False
	AL = ALG.Graph(vertices, weighted, directed)
	AL.insert_edge(0,5)
	AL.insert_edge(2,11)
	AL.insert_edge(2,7)
	AL.insert_edge(4,5)
	AL.insert_edge(4,7)
	AL.insert_edge(4,13)
	AL.insert_edge(8,11)
	AL.insert_edge(8,13)
	AL.insert_edge(10,11)
	AL.insert_edge(10,15)

	EL = AL.as_EL()
	AM = AL.as_AM()

	return AL, AM, EL

def drawGraphs():
	AL, AM, EL = buildGraphs()
	AL.draw()
	AM.draw()
	EL.draw()

def main():
	AL, AM, EL = buildGraphs()
	#AL
	
	#print(AL.buildPath(0))
	print("AL: breadth First Search")
	print(AL.breadthFirstSearch(0,15))
	AL.printBreadthPath(0,15)
	print("AL: Depth First Search")
	print(AL.depthFirstSearch(0,15))
	AL.printDepthPath(0,15)
	print()
	
	#AM
	#print(AM.buildPath(0))
	print("AM: breadth First Search")
	print(AM.breadthFirstSearch(0,15))
	AM.printBreadthPath(0,15)
	print("AM: Depth First Search")
	print(AM.depthFirstSearch(0,15))	
	AM.printDepthPath(0,15)
	print()

	#EL
	#print(EL.buildPath(0))
	print("EL: breadth First Search")
	print(EL.breadthFirstSearch(0,15))
	EL.printBreadthPath(0,15)
	print("EL: Depth First Search")
	print(EL.depthFirstSearch(0,15))	
	EL.printDepthPath(0,15)	
	print()

if __name__ == '__main__':
	main()
	#drawGraphs()