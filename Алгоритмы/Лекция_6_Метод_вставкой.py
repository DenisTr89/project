A = [22, -11, 1, 4, 2, 10, 43]
N  = len(A)
for i in range(1, N):
    for j in range(i, 0, -1):
        if A[j] < A[j-1]:
            A[j], A[j-1] = A[j-1],  A[j]
        
print(A)
