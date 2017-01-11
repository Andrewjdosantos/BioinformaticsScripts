import itertools
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN
import random
edge = []
for i in range(0,len(lines)):
	start = lines[i].split("->")[0]
	end = lines[i].split("->")[1].split(',')
	for node in range(0,len(end)):
		edge.append(str(start.strip())+','+str(end[node].strip()))
print(edge)
def randomEdge(Edges):
	randomedge = random.choice(Edges)
	return(randomedge)

def CycleCreate(start,edge):
	edges = list(edge)
	startNode = start.split(',')[0]
	nextNode = start.split(',')[1]
	counter = 0
	edges.remove(start)
	counter = counter + 1
	startswith = []
	cycle = []
	cycle.append(startNode)
	cycle.append(nextNode)
	for i in range(0,len(edges)):
		if edges[i].startswith(nextNode):
			startswith.append(edges[i])
	while len(startswith) > 0:
		randomlychosen = randomEdge(startswith)
		cycle.append(randomlychosen.split(',')[1])
		nextNode = randomlychosen.split(',')[1]
		edges.remove(randomlychosen)
		counter = counter + 1
		startswith = []
		for i in range(0,len(edges)):
			if edges[i].startswith(nextNode):
				startswith.append(edges[i])
	return(cycle,counter)


def EulerianCycle(edge):
	start = randomEdge(edge)
	cyclecount = CycleCreate(start,edge)
	cycle = cyclecount[0]
	count = cyclecount[1]
	while count != len(edge):
		start = randomEdge(edge)
		cyclecount = CycleCreate(start,edge)
		cycle = cyclecount[0]
		count = cyclecount[1]
	return(cycle)

print(EulerianCycle(edge))