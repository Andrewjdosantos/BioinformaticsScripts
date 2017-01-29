import itertools
import sys # you must import "sys" to read from STDIN
import random
from collections import Counter
import Overlap
import EulerianPath
# lines = sys.stdin.read().splitlines() # read in the input from STDIN

# k = int(lines[0])
# kmers = lines[1:len(lines)]

def StringReconstruction(k,kmers):
	adjacency = Overlap.Adjacency(kmers)
	EulerianP = EulerianPath.EulerianPath(adjacency.splitlines())
	EulerianPList = EulerianP[1]
	EulerianP = EulerianP[0]
	string = EulerianPList[0]
	for i in range(1,len(EulerianPList)):
		string = string + EulerianPList[i][k-1]
	return(string)


def Binary(k):
	lst = list(itertools.product([0, 1], repeat=k))
	binList = []
	for i in range(0,len(lst)):
		binList.append("".join(str(x) for x in lst[i]))
	eul = StringReconstruction(k,binList)
	return(eul)

print(Binary(4))