a, b, c = map(int,input().split())  # 주사위 3개 값을 받아 int로 바꿔주기

if a == b == c:                     # 같은 눈이 3개 일 때
    print(10000 + a * 1000)         # 10000 + 같은 눈 * 1000 
elif a == b or a == c:              # 같은 눈이 2개 일 때
    print(1000 + a * 100)           # 같은 눈이 a일 때
elif b == c:                        # 같은 눈이 b일 때
    print(1000 + b * 100)
else:                               # 모두 다른 눈
    max = [a, b, c]                 # 비교를 위해 max 리스트로 묶어줌
    max_number = max[0]             # max_number에 가장 큰 값 저장   // max_number의 주소는 바로 int값으로 감 (파이썬 튜터)
    for i in max:                   # 리스트의 옆의 값과 돌아가며 비교
        if max_number <= i:         # i가 max_number보다 클 때
            max_number = i          # max_number값에 i를 할당
    print(max_number * 100)

            
                                    # 코드가 너무 복잡한 것 같은 느낌?
