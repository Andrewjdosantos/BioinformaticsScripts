import itertools
import sys # you must import "sys" to read from STDIN
import random
from collections import Counter
import Overlap
import EulerianPath
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k = int(lines[0])
kmers = lines[1:len(lines)]

def StringReconstruction(k,kmers):
	adjacency = Overlap.Adjacency(kmers)
	EulerianP = EulerianPath.EulerianPath(adjacency.splitlines())
	EulerianPList = EulerianP[1]
	EulerianP = EulerianP[0]
	string = EulerianPList[0]
	for i in range(1,len(EulerianPList)):
		string = string + EulerianPList[i][k-1]
	return(string)

print(StringReconstruction(k,kmers))
