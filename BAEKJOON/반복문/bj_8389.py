num = int(input())

ans = 0                   # 합을 넣을 변수, 초기값이므로 0
for i in range(1, num+1): # 1부터 num까지 반복
    ans += i              # 순차적으로 더해줍니다
print(ans)                # print가 for안에 있으면 1, 3, 6다 나오므로 최종값만 얻고 싶기 때문에 빼줌