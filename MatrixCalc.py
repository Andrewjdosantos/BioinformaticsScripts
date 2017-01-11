
profile = {

    'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
    'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
    'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
    'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}
prob = 1
for i in range(0,len(profile['A'])):
	A = profile['A']
	C = profile['C']
	G = profile['G']
	T = profile['T']
	print(A[0])
	lister = []
	lister = lister.append(A[i])
	lister = lister.append(C[i])
	lister = lister.append(G[i])
	lister = lister.append(T[i])
	maxNum = max(lister)
	prob = prob*maxNum