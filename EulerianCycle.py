import itertools
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN
import random
edge = {}

for i in range(0,len(lines)):
	start = int(lines[i].split("->")[0].strip())
	end = lines[i].split("->")[1].split(',')
	ender = []
	for node in range(0,len(end)):
		ender.append(int(end[node].strip()))
	edge[start] = ender

def CycleCreate(StartNode,edges):
	WController = 0
	cycle = []
	cycle.append(StartNode)
	while WController == 0:
		try:
			NextNode = random.choice(edge[StartNode])
		except(KeyError):
			WController = 1
			return(cycle,edges)
		cycle.append(NextNode)
		edges[StartNode].remove(NextNode)
		StartNode = NextNode
		keys = edge.keys()
		for key in keys:
			if len(edge[key]) == 0:
				del edges[key]

def replace(l, X, Y):
  for i,v in enumerate(l):
     if v == X:
        l.pop(i)
        l.insert(i, Y)

def EularianCycle(edges):
	cycle = []
	StartNode = random.choice(edges.keys())
	cycler = CycleCreate(StartNode,edges)
	cycle = cycler[0]
	edges = cycler[1]
	while len(edges.keys()) > 0:
		intersect = list(set(edges.keys()).intersection(cycle))
		StartNode = random.choice(intersect)
		cycler = CycleCreate(StartNode,edges)
		edges = cycler[1]
		indexed = cycle.index(StartNode)
		cycle.remove(StartNode)
		for i in range(0,len(cycler[0])):
			cycle.insert(indexed+i,cycler[0][i])
	return(cycle)
Euler = EularianCycle(edge)
eul = str(Euler)
output = eul.replace(',','->').replace('[','').replace(' ','').replace(']','')
print(output)

# select start node
# add start node to cycle
# select next node
# if no next node return the cycle
# while controller off
# else:
# add next node to cycle
# remove next node from start nodes dictionary key list
# cull all keys from dict where edge list =0



# for i in range(0,len(lines)):
# 	start = lines[i].split("->")[0]
# 	end = lines[i].split("->")[1].split(',')
# 	for node in range(0,len(end)):
# 		edge.append(str(start.strip())+','+str(end[node].strip()))
# print(edge)
# def randomEdge(Edges):
# 	randomedge = random.choice(Edges)
# 	return(randomedge)

# def CycleCreate(start,edge):
# 	edges = list(edge)
# 	startNode = start.split(',')[0]
# 	nextNode = start.split(',')[1]
# 	counter = 0
# 	edges.remove(start)
# 	counter = counter + 1
# 	startswith = []
# 	cycle = []
# 	cycle.append(startNode)
# 	cycle.append(nextNode)
# 	for i in range(0,len(edges)):
# 		if edges[i].startswith(nextNode):
# 			startswith.append(edges[i])
# 	while len(startswith) > 0:
# 		randomlychosen = randomEdge(startswith)
# 		cycle.append(randomlychosen.split(',')[1])
# 		nextNode = randomlychosen.split(',')[1]
# 		edges.remove(randomlychosen)
# 		counter = counter + 1
# 		startswith = []
# 		for i in range(0,len(edges)):
# 			if edges[i].startswith(nextNode):
# 				startswith.append(edges[i])
# 	return(cycle,counter)


# def EulerianCycle(edge):
# 	start = randomEdge(edge)
# 	cyclecount = CycleCreate(start,edge)
# 	cycle = cyclecount[0]
# 	count = cyclecount[1]
# 	while count != len(edge):
# 		start = randomEdge(edge)
# 		cyclecount = CycleCreate(start,edge)
# 		cycle = cyclecount[0]
# 		count = cyclecount[1]
# 	return(cycle)

# print(EulerianCycle(edge))