import sys # you must import "sys" to read from STDIN
#lines = sys.stdin.read().splitlines() # read in the input from STDIN
#DNA = lines[0]
#line2 = lines[1].split('')
#k = line2[0]
#L = line2[1]
#t = line2[2]

def PatternCount(Text, Pattern):
    count = 0
    TextSize = len(Text) - len(Pattern)
    for i in range(0,TextSize):
        if Text[i:len(Pattern)+i] == Pattern:
            count = count + 1
    return count

def PatternLoc(Text, Pattern):
    count = []
    TextSize = len(Text) - len(Pattern)
    for i in range(0,TextSize):
        if Text[i:len(Pattern)+i] == Pattern:
            count.append(i)
    return count

def FrequentWords(Text, k):
        FrequentPatterns = []
        count = []
        for i in range(0,len(Text)-k):
            Pattern = Text[i:k+i]
            count.append(PatternCount(Text, Pattern))
        maxCount = max(count)
        for i in range(0, len(Text) - k):
            if count[i] == maxCount:
                FrequentPatterns.append(Text[i:k+i])
        FrequentPatterns = set(FrequentPatterns)
        return FrequentPatterns

#print PatternLoc(DNA, k,L,t)