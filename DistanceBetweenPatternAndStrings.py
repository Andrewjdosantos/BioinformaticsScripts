import itertools
import sys # you must import "sys" to read from STDIN
import ImmediateNeighbors as N
import math
import Array as A
lines = sys.stdin.read().splitlines() # read in the input from STDIN
k = int(lines[0])
DNA = []

for line in range(1,len(lines)):
	DNA.append(lines[line])

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in range(0,len(Dna)):
        texter = Dna[Text]
        HammingDistance = len(texter)
        for kmer in range(0,len(texter)-k):
            if HammingDistance > N.Hamming(Pattern, texter[kmer:kmer+k]):
                HammingDistance = N.Hamming(Pattern, texter[kmer:kmer+k])
        distance = distance + HammingDistance
    return distance


def MedianString(Dna, k):
    distance = float('Inf')
    Median = ''
    for i in range(0,(4**k)-1):
        Pattern = A.NumberToPattern(i, k)
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
            print(Pattern)
    return Median

print(MedianString(DNA,k))