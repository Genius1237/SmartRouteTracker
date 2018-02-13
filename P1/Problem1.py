import sys
import string
import random
import copy

"""
* Data structure to store data regarding current state.
"""
class State:
	def __init__(self):
		self.position = None # Tekls the number of missionaries and cannibals in west bank
		self.flag = 0 # Tells whether the journey is forward or backward


"""
* Represents an Abstraction for stack used in Depth First Backtracking
"""
class TrackStack:
	def __init__(self):
		self.size = 0
		self.trackStack=[]

	def push(self,state):
		self.trackStack.append(state)
		self.size=self.size+1

	def pop(self):
		if(self.size<=0):
			return
		else:
			self.trackStack.pop()
			self.size = self.size - 1

	def empty(self):
		if(self.size<=0):
			return True
		return False

	def top(self):
		return self.trackStack[-1]

class MissionRescue:

	"""
	* Constructor: To Set the initial Problem states
	* Params: variables a and b to store the number of Missionaries
	* and number of Cannibals respectively
	"""
	def __init__(self,a,b):
		self.numMissionaries = a
		self.numCannibals = b
		self.visited = []
		self.boatCap = 2
		for i in range( a+1 ):
			temp = []
			for j in range( b+1 ):
				temp2 = []
				for k in range(2):
					temp2.append(0)
				temp.append(temp2)
			self.visited.append(temp)

		self.state = (a,b)
		self.getOnBoat = []
		self.path=[]


	"""
	* Given the current number of missionaries and cannibals
	* in the western bank,returns all possible next states, 
	* irrespective of whether it was visited it in the past
	"""
	def possiblePaths(self,ano,bno,flag):
		possibleNextStates = []
		if ( flag == 0 ):
			if ( ano > 0 and bno > 0 ):
				possibleNextStates.append((ano-1,bno-1))
			if ( ano > 0 ):
				if ( ano > 1 ):
					possibleNextStates.append((ano-2,bno))
				possibleNextStates.append((ano-1,bno))

			if ( bno > 0 ):
				if ( bno > 1):
					possibleNextStates.append((ano,bno-2))
				possibleNextStates.append((ano,bno-1))



		else:
			if ( ano < self.numMissionaries ):
				possibleNextStates.append((ano+1,bno))

			if ( bno < self.numCannibals ):
				possibleNextStates.append((ano,bno+1))

			if ( ano < self.numMissionaries-1 ):
					possibleNextStates.append((ano+2,bno))

			if ( bno < self.numCannibals-1 ):
					possibleNextStates.append((ano,bno+2))

			if ( ano < self.numMissionaries and bno < self.numCannibals ):
				possibleNextStates.append((ano+1,bno+1))


		return possibleNextStates


	"""
	Function that start searching from state: self.state till state 0,0 
	via Depth First Backtracking, and returns the path 
	(may not be the shortest path) from start state to 0,0.
	"""
	def searchSolution(self):
		flag = 0
		pathStack = TrackStack()
		currState = State()
		currState.position = copy.deepcopy(self.state)
		currState.flag = copy.deepcopy(flag)
		#print((currPosition[0],currPosition[1],flag))
		pathStack.push(currState)
		self.visited[currState.position[0]][currState.position[1]][flag]=1
		while pathStack.empty()==False:
			top = pathStack.top().position
			flag = pathStack.top().flag

			if ( (top[0] < top[1] and top[0]!=0 and flag==1 ) or ( ( self.numMissionaries-top[0] < self.numCannibals-top[1]) and top[0]!=self.numMissionaries ) and flag==0 ):
				print(top,flag,end="  ")
				print("Cannibals")
				pathStack.pop()
				continue


			print(top,flag,end="  ")
			neighbours = self.possiblePaths(top[0],top[1],flag)
			random.shuffle(neighbours)
			print(neighbours)
			atleastOnePath = False
			if ( top[0]==0 and top[1]==0 ):
				print("Solution found.. have a look at it")
				print(top[0],top[1])
				pathStack.pop()
				while not pathStack.empty():
					print(pathStack.top().position[0],pathStack.top().position[1])
					pathStack.pop()
				return

			for path in neighbours:
				if ( self.visited[path[0]][path[1]][flag] == 0 ):
					atleastOnePath = True
					self.visited[path[0]][path[1]][flag]=1
					nextState = State()
					nextState.position = copy.deepcopy(path)
					nextState.flag = copy.deepcopy(flag^1)
					pathStack.push(nextState)
					break

			if ( atleastOnePath == False ):
				pathStack.pop()



obj = MissionRescue(3,3)
obj.searchSolution()