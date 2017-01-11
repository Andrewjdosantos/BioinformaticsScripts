import sys # you must import "sys" to read from STDIN
#lines = sys.stdin.read().splitlines() # read in the input from STDIN

#NucAcid = lines[0]
def Compliment(NucAcid):
	p = ''
	for i in range(0,len(NucAcid)):
		if NucAcid[i] == 'A':
			p = p+'T'
		if NucAcid[i] == 'T':
			p = p+'A'
		if NucAcid[i] == 'G':
			p = p+'C'
		if NucAcid[i] == 'C':
			p = p+'G'
	pstar = p[::-1]
	return pstar

#print Compliment(NucAcid)

