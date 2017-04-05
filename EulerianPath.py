import itertools
import sys # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
import random
from collections import Counter

def DataMassage(lines):
	print('Entering DataMassage')
	edge = {}
	nodes = []
	for i in range(0,len(lines)):
		start = lines[i].split("->")[0].strip()
		end = lines[i].split("->")[1].split(',')
		ender = []
		for node in range(0,len(end)):
			ender.append(str(end[node].strip()))
			nodes.append(str(end[node].strip()))
		try:
			edge[start].append(ender[0])
		except(KeyError):
			edge[start] = ender
	return(edge,nodes)

def CalcStartEnd(nodes,edges):
	print('Entering CalcStartEnd')
	counts = Counter(nodes)
	print(counts)
	print(edges)
	start = 0
	end = 0
	EndNone = 0
	StartNone = 0
	counter = 0
	for key in edges:
		if key not in counts.keys():
			StartNone = str(key)
			counter = counter +1
			start = str(key)
			print('found start')
			print(key)
			print(len(list(edges[key])))
			print(counts[key])
	for key in counts:
		try:	
			if len(list(edges[key])) < counts[key]:
				end = str(key)
				print('found end')
				print(key)
				print(len(list(edges[key])))
				print(counts[key])
			if len(list(edges[key])) > counts[key]:
				start = str(key)
				print('found start')
				print(key)
				print(len(list(edges[key])))
				print(counts[key])
		except(KeyError):
			print('found key errors')
			EndNone = str(key)
			print(key)
	# edgelst = []
	# for i in edges.keys():
	# 	edgelst.append(i)
	# if counter == 0:
	# 	print('not found')
	# 	randomSelect = random.choice(edgelst)
	# 	while randomSelect == end:
	# 		randomSelect = random.choice(edgelst)
	# 	start = randomSelect
	keys = []
	for key in edges.keys():
		keys.append(key)
	if EndNone != 0:
		end = str(EndNone)
	if end == 0:
			end = random.choice(keys)
	if StartNone != 0:
		start = str(StartNone)
	if start == 0:
		start = random.choice(keys)
	print('Start,End')
	print(str(start))
	print(str(end))
	return(start,end)

def CycleCreate(StartNode,edges,nodesRem):
	print('Entering CycleCreate')
	WController = 0
	cycle_1 = []
	cycle_1.append(StartNode)
	NodesR = nodesRem[:]
	try:
		NodesR.remove(StartNode)
	except(ValueError):
		print("Not in nodes rem")
	# print(StartNode)
	# print(NodesR)
	while WController == 0:
		try:
			NextNode = random.choice(edges[StartNode])
		except(KeyError):
			WController = 1
			return(cycle_1,edges,NodesR)
		edges[StartNode].remove(NextNode)
		if NextNode in NodesR:
			StartNode = NextNode
			NodesR.remove(NextNode)
			cycle_1.append(NextNode)
		keys= []
		for key in edges.keys():
			keys.append(key)
		# keys = edges.keys()
		for key in keys:
			if len(edges[key]) == 0:
				del edges[key]
	# return(cycle,edges,NodesR)

def replace(l, X, Y):
  for i,v in enumerate(l):
     if v == X:
        l.pop(i)
        l.insert(i, Y)

def EulerianPath(lines,Counter,noder):
	print('nodes')
	print(noder)
	data = DataMassage(lines)
	edges = data[0]
	nodes = data[1]
	cycle = []
	nodes_2 = noder
	StartNode = CalcStartEnd(nodes,edges)[0]
	# print(StartNode)
	cycler = CycleCreate(StartNode,edges,noder)
	print('cycler')
	print(cycler[0])
	cycle = cycler[0]
	# print(cycle)
	edges = cycler[1]
	nodes_2 = cycler[2][:]
	print('nodes_rem')
	print(nodes_2)
	print('cycle')
	print(cycle)
	# print(edges)
	while len(nodes_2) >0:
		intersect = list(set(edges.keys()).intersection(cycle))
		print(intersect)
		StartNode = random.choice(intersect)
		cycler = CycleCreate(StartNode,edges,nodes_2)
		print('cycler')
		print(cycler[0])
		nodes_2 = cycler[2][:]
		print('nodes_rem')
		print(nodes_2)
		edges = cycler[1]
		indexed = cycle.index(StartNode)
		if len(cycler[0])>1:
			cycle.remove(StartNode)
			for i in range(0,len(cycler[0])):
				cycle.insert(indexed+i,cycler[0][i])
		print('cycle')
		print(cycle)
		print(len(cycle))
		print(len(noder))
	cycleList = cycle
	cycle = str(cycle).rstrip()
	cycle = cycle.replace(',','->').replace('[','').replace(' ','').replace(']','').replace('','')
	return(cycle,cycleList)

# Euler = EularianPath(lines)
# eul = str(Euler)
# output = eul.replace(',','->').replace('[','').replace(' ','').replace(']','')
# print(output)

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