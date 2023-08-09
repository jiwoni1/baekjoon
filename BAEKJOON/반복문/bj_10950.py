T = int(input())

for i in range(T):                   # T줄이 있으니까 T번만큼 반복
    A, B = map(int, input().split()) # 한 줄당 나눠줌
    print(A+B)                       # 근데 한번에 입력을 받고 출력을 한번에 세로로 못하나?