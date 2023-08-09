N, M = map(int, input().split())

arr1 = [_ for _ in range(N)]
arr2 = [_ for _ in range(N)]

for i in range(N):
    arr1[i] = list(map(int, input().split()))

for i in range(N):
    arr2[i] = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        arr1[i][j] = arr1[i][j] + arr2[i][j]

for number in range(N):
    print(*arr1[number])