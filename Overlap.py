import itertools
import sys # you must import "sys" to read from STDIN
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# k = int(lines[0])
# Pattern = lines[1]

def Overlap(Kmer):
	final = []
	for i in range(0,len(Kmer)):
		if  i == 0:
			final.append(Kmer[i])
		else:
			neuc = Kmer[i][len(Kmer[i])-1]
			final.append(neuc)
	s = ""
	final = s.join(final)
	return(final)

def Prefix(Kmer):
	k = len(Kmer)
	Pref = Kmer[0:k-1]
	return(Pref)

def Suffix(Kmer):
	k = len(Kmer)
	Suff = Kmer[1:k]
	return(Suff)

def Adjacency(Kmers):
	adjacency = []
	for i in range(0, len(Kmers)):
		for k in range(0,len(Kmers)):
			if Prefix(Kmers[i]) == Suffix(Kmers[k]) and k != i:
				app = Kmers[k]+" -> "+Kmers[i]
				adjacency.append(app)
	s = "\n"
	adjacency=list(adjacency)
	adjacency = s.join(adjacency)
	return(adjacency)

# def search(dictionary,searcher):
# 	for i in range(0,len(dictionary)):
# 		for k in range(0,len(dictionary[i]):
# 			if searcher in dictionary[i][k]:
# 				return(True)

def DeBruijn(k,Pattern):
    kmers = []
    for i in range(0,len(Pattern)-k+1):
        kmer = Pattern[i:i+k]
        kmers.append(kmer)
    short_kmers = []
    for i in range(0,len(kmers)):
    	short_kmers.append(kmers[i][0:k-1])
    # print(short_kmers)
    # kmers=short_kmers
    short_kmers = sorted(list(set(short_kmers)))
    adjacency = {}
    for i in range(0,len(short_kmers)):
    	adjacency[short_kmers[i]] = []
    kmers2 =kmers
    for i in range(0,len(short_kmers)):
    	for ks in range(0,len(kmers)):
    		if short_kmers[i] == Prefix(kmers[ks]):
    			adjacency[short_kmers[i]].append(Suffix(kmers[ks]))

    printable = []
    for i in range(0,len(adjacency)):
        printable.append(short_kmers[i] + " -> " + ",".join(sorted(adjacency[short_kmers[i]])))
    adjacency = "\n".join(printable)
    return(adjacency)

# print(DeBruijn(k,Pattern))