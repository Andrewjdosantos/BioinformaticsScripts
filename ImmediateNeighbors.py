#import Hamming
import itertools
import sys # you must import "sys" to read from STDIN
#lines = sys.stdin.read().splitlines() # read in the input from STDIN
#keeper = ""
def Hamming(p,q):
	Hamming =0
	for i in range(len(p)):
		if p[i] != q[i]:
			Hamming = Hamming +1
	return(Hamming)

#def ImmediateNeighbors(Pattern):
#    Neighborhood = []
#    Neighborhood.append(Pattern)
#    neucs = ["A","C","G","T"]
#    for i in range(1,len(Pattern)):
#        symbol = Pattern[i]
#       for X in range(0, len(neucs)):
#            if symbol != neucs[X]:
#                Neighbor = Pattern[0:i-1] + neucs[X] + Pattern[i:len(Pattern)]
#                Neighborhood.append(Neighbor)
#    return Neighborhood


def Neighbors(Pattern, d):
    neucs = ["A","C","G","T"]
    if int(d) == 0:
        return(list(Pattern))
    if len(Pattern) == 1 :
        return("A","C","G","T")
    Neighborhood = []
    SuffixPattern = Pattern[1:len(Pattern)]
    SuffixNeighbors = Neighbors(SuffixPattern, int(d))
    for i in range(0,len(SuffixNeighbors)):
        if Hamming(SuffixNeighbors[i], SuffixPattern) < int(d):
            for x in range(0,len(neucs)):
                Neighborhood.append(neucs[x] + SuffixNeighbors[i])
        else:
            Neighborhood.append(Pattern[0] + SuffixNeighbors[i])

    return Neighborhood

#Neigh = Neighbors(lines[0],lines[1])

#Neigh = list(set(ImmediateNeighbors("ACGT")))
#print(Neigh)
#for i in range(0,len(Neigh)-1):
#	print(Hamming(Neigh[i],"ACGT"))

#for i in range(0,len(Neigh)):
#   	keeper = keeper + Neigh[i] + "\n"
#print(keeper)
