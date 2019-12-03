import graph_AL as graph
import numpy as np
from connected_components import connected_components

#finds in-degrees of vertex v
def in_degree(G, v):
	sumDeg = 0
	for i in range(len(G.al)):
		for e in G.al[i]:
			if e.dest == v:
				sumDeg += 1
	return sumDeg

#hamiltonian cycle using randomization
def randomizedHamiltonian(G, trials = 1000):
	gEL = G.as_EL()
	for q in range(trials):
		gh = graph.Graph(len(G.al), weighted=G.weighted, directed=G.directed)
		gh = gh.as_EL()
		edges = gEL.el[:]
		#randomly choose edges
		for r in range(gh.vertices):
			gh.el.append(edges.pop(np.random.randint(len(edges))))
		#convert to adjacency list to check connected components
		gh = gh.as_AL()
		components,s = connected_components(gh)
		if components == 1:
			has2Deg = True
			#check if each vertex has in_degree 2.
			for i in range(len(gh.al)):
				indeg = in_degree(gh,i)
				if indeg != 2:
					has2Deg = False #give up, not a hamiltonian cycle	
			if has2Deg:
				return gh
	#could not find hamiltonian cycle.
	return None		




#takes in list and edge list.
def backtracker(g,gh):
	#end recursion if out of edges
	if len(gh.el) == gh.vertices:
		ghAL = gh.as_AL()
		components,s = connected_components(ghAL)
		if components == 1:
			#check in-degrees
			for i in range(len(ghAL.al)):
				if in_degree(ghAL, i) != 2:
					return None
			return ghAL
		return None
	if len(g) == 0:
		return None	
	else:
		nextEdge = g[0]
		gh.el = gh.el + [nextEdge]     
		response = backtracker(g[1:], gh)
		if response is not None:
			return response
		gh.el.remove(nextEdge) # get rid of inserted edge and backtrack
		response = backtracker(g[1:], gh)
		return response


def backtrackHamiltonian(G):
	# #check if every vertex in V has in-degree 2.
	gEL = G.as_EL()
	for e in gEL.el:
		print(e.source, e.dest, e.weight)
	gBuild = graph.Graph(len(G.al), weighted=G.weighted, directed=G.directed)
	return backtracker(gEL.el,gBuild.as_EL())


def editDistance(word1, word2):
	vowels = ['a','e','i','o','u']
	consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
	matrix = np.zeros((len(word1)+1,len(word2)+1),dtype=int)
	for i in range(len(matrix)):
		matrix[i][0] = i
	for i in range(len(matrix[0])):	
		matrix[0][i] = i
	for i in range(1,len(matrix)):
		for j in range(1,len(matrix[i])):
			#if characters are the same
			if word1[i-1] == word2[j-1]:
				matrix[i][j] = 	matrix[i-1][j-1]
			else:
				#if both characters are vowels or consonants, find the minimum and add 1
				if (word1[i-1] in vowels and word2[j-1] in vowels) or (word1[i-1] in consonants and word2[j-1] in consonants):
					matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])+1
				
				else:
					#if both characters not vowel or consonant, then replacements (upper left) are not possible.
					matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1])+1
	print(matrix)




def testHamiltonianCycle():
	# g = graph.Graph(3, weighted=False, directed=False)
	# g.insert_edge(0,1)
	# g.insert_edge(1,2)
	# g.insert_edge(2,0)
	g = graph.Graph(5, weighted=False, directed=False)
	g.insert_edge(0,1)
	g.insert_edge(1,2)
	g.insert_edge(2,4)
	g.insert_edge(1,4)
	g.insert_edge(1,3)
	g.insert_edge(0,3)
	g.insert_edge(3,4) #comment this edge to get rid of hamiltonian cycle

	g.draw()
	#hamilCyc = randomizedHamiltonian(g)
	hamilCyc = backtrackHamiltonian(g)
	if hamilCyc is not None:
		print('Found hamiltonian cycle')
		hamilCyc.draw()
	else:
		print("could not find hamiltonian cycle")

if __name__ == '__main__':
	testHamiltonianCycle()
	#editDistance("money", "miners")
	#print("aei", "iou")
	#editDistance("aei", "iou")
	#print("aei","bcd")
	#editDistance("aei", "bcd")