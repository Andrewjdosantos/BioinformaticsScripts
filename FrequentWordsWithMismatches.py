import Hamming
import Array
import Skew
import itertools
import sys
import ImmediateNeighbors
import compliment

lines = sys.stdin.read().splitlines() # read in the input from STDIN
line2 = lines[1].split(' ')
k = int(line2[0])
d = int(line2[1])
print(lines)

def FrequentWordsWithMismatches(Text, k, d):
    FrequentPatterns = []
    Close = [0] * (4**k)*2
    FrequencyArray = [0] * (4**k)*2
    for i in range(0,len(Close) - 1):
        Close[i] = 0
        FrequencyArray[i] = 0
    for i in range(0,(len(Text) - k)):
        Neighborhood = ImmediateNeighbors.Neighbors(Text[i:i+k], d)
        for i in range(0,len(Neighborhood)):
            index = Array.PatternToNumber(Neighborhood[i])
            Close[index] = 1
    for i in range(0,(len(Text) - k)):
        reverse = compliment.Compliment(Text[i:i+k])
        print(reverse)
        Neighborhood = ImmediateNeighbors.Neighbors(reverse, d)
        for i in range(0,len(Neighborhood)):
            index = Array.PatternToNumber(Neighborhood[i])
            Close[index] = 1
    for i in range(0,len(Close) - 1):
        if Close[i] == 1:
            Pattern = Array.NumberToPattern(i, k)
            FrequencyArray[i] = Hamming.ApproximatePatternCount(Pattern, Text, d)
    maxCount =max(FrequencyArray)
    for i in range(0,len(Close) - 1):
        if FrequencyArray[i] == maxCount:
            Pattern = Array.NumberToPattern(i, k)
            print(Pattern)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns
print(FrequentWordsWithMismatches(lines[0],k,d))