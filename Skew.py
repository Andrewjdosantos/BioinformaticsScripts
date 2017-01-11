import itertools
import sys # you must import "sys" to read from STDIN
#lines = sys.stdin.read().splitlines() # read in the input from STDIN

#
def Skew(text):
	index = [0]*(len(text)+1)
	Skew = 0
	for i in range(1,len(text)+1):
		if text[i-1] == "G":
			Skew = Skew +1
			index[i] = Skew
		if text[i-1] == "C":
			Skew = Skew-1
			index[i] = Skew
		if text[i-1] == "A" or text[i-1] == "T":
			index[i] = Skew
	minIndex = min(index)
	minPos = []
	for i in range(1,len(index)):
		if index[i] == minIndex:
			minPos.append(i)
	return (minPos)

print(Skew("GATACACTTCCCGAGTAGGTACTG"))