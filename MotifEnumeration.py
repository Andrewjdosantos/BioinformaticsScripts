import itertools
import sys # you must import "sys" to read from STDIN
import ImmediateNeighbors as N
lines = sys.stdin.read().splitlines() # read in the input from STDIN
liner = lines[0].split(" ")
k = int(liner[0])
d = int(liner[1])
DNA = []

for line in range(1,len(lines)):
	DNA.append(lines[line])

def Hamming(p,q):
	Hamming =0
	for i in range(len(p)):
		if p[i] != q[i]:
			Hamming = Hamming +1
	return(Hamming)

def Neighbors(Pattern, d):
    neucs = ["A","C","G","T"]
    Patterner = []
    if int(d) == 0:
        Patterner.append(Pattern)
        return(Patterner)
    if len(str(Pattern)) == 1 :
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

def MotifEnumeration(Dna, k, d):
	Pattern = []
	DNS = Dna[0]
	print(len(DNS))
	for kmer in range(0,len(DNS)-k+1):
		print(kmer)
		PatterNeigh =Neighbors(DNS[kmer:kmer+k],d)
		for Patterns in range(0,len(PatterNeigh)):
			counter = 0
			for s in range(0,len(Dna)):
				control = 0
				if s != 0:
					for kmer2 in range(0,len(Dna[s])-k+1):
							if Hamming(PatterNeigh[Patterns],Dna[s][kmer2:kmer2+k])<=d:
								if control == 0:
									counter = counter + 1
									control = control +1
								if counter == len(Dna) -1 :
									Pattern.append(PatterNeigh[Patterns])
	return(set(Pattern))

print(MotifEnumeration(DNA,k,d))
