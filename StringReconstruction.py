import itertools
import sys # you must import "sys" to read from STDIN
import random
from collections import Counter
import Overlap
import EulerianPath
lines = sys.stdin.read().splitlines() # read in the input from STDIN

k = int(lines[0].split(' ')[0])
d = int(lines[0].split(' ')[1])
kmers = lines[1:len(lines)]
print(kmers)
def SplitPairs(pairs):
	Preffix = []
	Suffix = []
	for i in range(0,len(pairs)):
		Preffix.append(pairs[i].split('|')[0].rstrip())
		Suffix.append(pairs[i].split('|')[1].rstrip())
	return(Preffix,Suffix)

def StringReconstruction(k,kmers):
	adjacency = Overlap.Adjacency(kmers)
	Counters = Counter(kmers)
	print(adjacency)
	EulerianP = EulerianPath.EulerianPath(adjacency.splitlines(),Counters,kmers)
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

def PairedString(k,d,pairs):
	Preffix = SplitPairs(pairs)[0]
	print(len(Preffix))
	Suffix = SplitPairs(pairs)[1]
	print(len(Suffix))
	counter = 10
	for j in range(0,counter):
		counter_two = 1
		PrefixString = StringReconstruction(k,Preffix)
		SuffixString = StringReconstruction(k,Suffix)
		for i in range((k + d + 1),len(PrefixString)):
			if PrefixString[i] != SuffixString[i-k-d-1]:
				print('No Gapped Pattern')
				counter_two = 0
		if counter_two == 1:
			return(PrefixString[0:k+d]+SuffixString)
	# PrefixString = StringReconstruction(k,Preffix)
	# SuffixString = StringReconstruction(k,Suffix)
	print(PrefixString)
	print(SuffixString)
	try:
		for i in range((k + d + 1),len(PrefixString)-1):
			if PrefixString[i] != SuffixString[i-k-d-1]:
				return('No Gapped Pattern')
	except(IndexError):
		print(PrefixString)
		print(SuffixString)
	return(PrefixString[0:k+d]+SuffixString)

# lst = list(itertools.product([0, 1], repeat=k))
# binList = []
# for i in range(0,len(lst)):
# 	binList.append("".join(str(x) for x in lst[i]))

print(PairedString(k,d,kmers))