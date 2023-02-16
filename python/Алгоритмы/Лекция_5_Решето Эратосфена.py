N = 200
A = [True]*N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False
for c in range(N):
    if A[c]:
        print (c, end = " ")

