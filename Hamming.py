import itertools
import sys # you must import "sys" to read from STDIN
#lines = sys.stdin.read().splitlines() # read in the input from STDIN

def Hamming(p,q):
	Hamming =0
	for i in range(len(p)):
		if p[i] != q[i]:
			Hamming = Hamming +1
	return(Hamming)


def ApproximatePatternCount(Pattern,Genome,HammingDist):
	Count = 0
	for i in range(0,len(Genome)-len(Pattern)+1):
		if Hamming(Pattern,Genome[i:(i+len(Pattern))]) <= HammingDist:
			Count = Count +1
	return Count

print(ApproximatePatternCount("TGT","CGTGACAGTGTATGGGCATCTTT",1))
#Approx = str(ApproxPatMatch(lines[0],lines[1],int(lines[2])))
#Approx = Approx.replace(",","")
#Approx = Approx.replace("[","")
#Approx = Approx.replace("]","")
#print(Approx)