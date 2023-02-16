A = [22, -11, 1, 4, 2, 10, 43]
N  = len(A)
for i in range(N):
    for j in range(i, N-1):
        if A[i] > A[j+1]:
            A[i], A[j+1] = A[j+1], A[i]
print(A)
