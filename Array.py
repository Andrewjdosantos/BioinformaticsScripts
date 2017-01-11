import itertools
import sys # you must import "sys" to read from STDIN
#lines = sys.stdin.read().splitlines() # read in the input from STDIN

#DNA = lines[0]
#line2 = lines[1].split()
#k = int(line2[0])
#L = int(line2[1])
#t = int(line2[2])

def SymbolToNumber(symbol):
	if symbol == 'A':
		return 0
	if symbol == 'C':
		return 1
	if symbol == 'G':
		return 2
	if symbol == 'T':
		return 3

def PatternToNumber(Pattern):
    if Pattern == '':
        return 0
    symbol = Pattern[len(Pattern)-1:len(Pattern)]
    Prefix = Pattern[0:len(Pattern)-1]
    return (4 * PatternToNumber(Prefix) + SymbolToNumber(symbol))

def NumberToSymbol(number):
	if number == 0:
		return 'A'
	if number == 1:
		return 'C'
	if number == 2:
		return 'G'
	if number == 3:
		return 'T'


def NumberToPattern(index, k):
        if k == 1:
            return NumberToSymbol(index)

        prefixIndex = index // 4
        r = index % 4
        symbol = NumberToSymbol(r)
        PrefixPattern = NumberToPattern(prefixIndex, k - 1)
        return (PrefixPattern + symbol)

def ComputingFrequencies(Text, k):
    exp = (4**(k))
    FrequencyArray = [0]*exp
    for i in range(0,len(Text)-(k-1)):
        Pattern = Text[i:k+i]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] = FrequencyArray[j] + 1
        return FrequencyArray

def FrequentWords(Text, k,t):
        FrequentPatterns = []
        FrequencyArray = ComputingFrequencies(Text,k)
        maxCount = max(FrequencyArray)
        for i in range(4**k):
        	if FrequencyArray[i] >= t:
        		Pattern = NumberToPattern(i,k)
        		FrequentPatterns.append(Pattern)
        return FrequentPatterns

def FrequentWordsBySorting(Text, k,t):
        FrequentPatterns = []
        Index = [0]*(len(Text)-k)
        Count = [0]*(len(Text)-k)
        for i in range(0,len(Text)-k):
            Pattern = Text[i:k+i]
            Index[i] = PatternToNumber(Pattern)
            Count[i] = 1
        SortedIndex = sorted(Index)
        for i in range(1,len(Text) -k):
            if SortedIndex[i] == SortedIndex[i - 1]:
                Count[i] = Count[i - 1] + 1
        for i in range(0,len(Text)-k):
            if Count[i] >= t:
                Pattern = NumberToPattern(SortedIndex[i], k)
                FrequentPatterns.append(Pattern)
        return FrequentPatterns


def ClumpFind(Genome,k,L,t):
	Clump = []
	Clumps = []
	for i in range(0,len(Genome)):
			Clumps.append(Genome[i:i+L])
	for i in range(0,len(Clumps)):
		FreqWords = FrequentWordsBySorting(Clumps[i],k,t)
		for j in range(0,len(FreqWords)):
			Clump.append(FreqWords[j])
	Clump = list(set(Clump))
	return Clump

#print ClumpFind(DNA,k,L,t)