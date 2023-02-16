A = [22, -11, 1, 4, 2, 10, 43]
N = len(A)
for i in range(N):
    for j in range(0, N - 1 - i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
print(A)
