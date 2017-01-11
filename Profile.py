import itertools
import sys # you must import "sys" to read from STDIN
lines = sys.stdin.read().splitlines() # read in the input from STDIN
k = int(lines[0].split(" ")[0])
t = int(lines[0].split(" ")[1])
import random
import math
import re
DNA = []

for line in range(1,len(lines)):
	DNA.append(lines[line])
#DNA = lines[0]
#profile = {'A':lines[2].split(" "),'C':lines[3].split(" "),'G':lines[4].split(" "),'T':lines[5].split(" ")}
#print(profile)

def ProProf(Pattern,Profile):
	prob= 1
	for i in range(0,len(Pattern)):
		neuc = Pattern[i]
		prob = prob * float(Profile[neuc][i])
	return(prob)	

def PatternMostProb(DNA,Profile):
	k = len(Profile['A'])
	prob = []
	for i in range(0,len(DNA)- k+1):
		prob.append(ProProf(DNA[i:i+k],Profile))
	maxProb = max(prob)
#	print(maxProb)
	control = 0
	for i in range(0,len(prob)):
		if control == 0:
			if prob[i] == maxProb:
				consensus = DNA[i:(i+k)]
				control = 1
	return(consensus)

def CreateProf(StringsDNA):
	a=[]
	c=[]
	g=[]
	t=[]
	for i in range(0,len(StringsDNA[0])):

		A=0
		C=0
		G=0
		T=0
		for strand in range(0,len(StringsDNA)):
					if StringsDNA[strand][i] == 'A':
						A=A+1
					if StringsDNA[strand][i] == 'C':
						C=C+1
					if StringsDNA[strand][i] == 'G':
						G=G+1
					if StringsDNA[strand][i] == 'T':
						T=T+1
		a.append((A/len(StringsDNA))+1)
		c.append((C/len(StringsDNA))+1)
		g.append((G/len(StringsDNA))+1)
		t.append((T/len(StringsDNA))+1)
	Profile = {'A':a,'C':c,'G':g,'T':t}
	return(Profile)

def CreateProfEnt(StringsDNA):
	a=[]
	c=[]
	g=[]
	t=[]
	for i in range(0,len(StringsDNA[0])):

		A=0
		C=0
		G=0
		T=0
		for strand in range(0,len(StringsDNA)):
					if StringsDNA[strand][i] == 'A':
						A=A+1
					if StringsDNA[strand][i] == 'C':
						C=C+1
					if StringsDNA[strand][i] == 'G':
						G=G+1
					if StringsDNA[strand][i] == 'T':
						T=T+1
		
		a.append(round(A/len(StringsDNA),4))
		c.append(round(C/len(StringsDNA),4))
		g.append(round(G/len(StringsDNA),4))
		t.append(round(T/len(StringsDNA),4))
	Profile = {'A':a,'C':c,'G':g,'T':t}
	return(Profile)

def Score(DNA):
	Scorer = 0
	for i in range(0,len(DNA[0])):
		A=0
		C=0
		G=0
		T=0
		for strand in range(0,len(DNA)):
			if DNA[strand][i] == 'A':
				A=A+1
			if DNA[strand][i] == 'C':
				C=C+1
			if DNA[strand][i] == 'G':
				G=G+1
			if DNA[strand][i] == 'T':
				T=T+1
		maxNeuc = max(A,C,G,T)
		Scorer = Scorer + (len(DNA)-maxNeuc)
	return(Scorer)

def ScoreEnt(DNA):
	profile = CreateProfEnt(DNA)
	Entropy = 0
	for i in range(0, len(profile['A'])):
		if profile['A'][i] <= 0:
			EntA = 0
		else:
			EntA = profile['A'][i]*math.log(profile['A'][i],2)
		if profile['C'][i] <= 0:
			EntC = 0
		else:
			EntC = profile['C'][i]*math.log(profile['C'][i],2)
		if profile['G'][i] <= 0:
			EntG = 0
		else:
			EntG = profile['G'][i]*math.log(profile['G'][i],2)
		if profile['T'][i] <= 0:
			EntT = 0
		else:
			EntT = profile['T'][i]*math.log(profile['T'][i],2)
		Entropy = Entropy + (-1*(EntA+EntG+EntC+EntT))
	return(round(Entropy,4))


def GreedyMotifSearch(DNA, k, t):
	best_motifs = []
	for i in range(0,len(DNA)):
		best_motifs.append(DNA[i][0:0+k])
	for i in range(0,len(DNA[0])-k+1):
		motif = []
		motif.append(DNA[0][i:i+k])
		for strands in range(1,t):
			profile = CreateProf(motif)
			motif.append(Profile(DNA[strands],profile))
		if Score(motif) < Score(best_motifs):
			best_motifs = motif
	return(best_motifs)

def RandomizedMotifSearch(Dna, k, t):
    BestMotifs = []
    for i in range(0,len(Dna)):
        length = len(Dna[i])-k
        motifPos = random.randrange(0, length)
        BestMotifs.append(Dna[i][motifPos:motifPos+k])
    Motifs = BestMotifs
    go = 1
    count = 0
    while go == 1 :
        Profile = CreateProf(Motifs)
        Motifs = []
        for i in range(0,len(Dna)):
        	Motifs.append(PatternMostProb(Dna[i],Profile))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        else:
            return(BestMotifs)

counter = 0
best2 = []
while counter != 1000:
	counter = counter +1
	best = RandomizedMotifSearch(DNA,k,t)
	if best2 == []:
		best2 = best
	if Score(best) < Score(best2):
		best2 = best

for i in range(0,len(best2)):
	print(re.sub(r'\W+', '', best2[i]))
