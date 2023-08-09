mr = []
for _ in range(10):
    mr.append(int(input()))

ate = 0
i = 0
ans = 0
while ate + mr[i] <= 100:     # 먹은 버섯의 양과 다음 버섯 하나의 합이 100보다 작거나 같다면
    ate += mr[i]              # 다음 버섯도 먹어줍니다
    i += 1                    # 그 다음 버섯으로 가기위한 i + 1
    if i == 9:                # 버섯을 다 먹었는데도 100 이하라면 (마지막 버섯 먹기 전)
        ans = ate + mr[i]     # 마지막 버섯까지 먹은 점수가 답
        break
if ate == 100:                          # 먹은 점수가 딱 100점이라면
    ans = ate                           # 바로 출력
elif ate + mr[i] > 100:                 # '이미 먹은거 + 다음 버섯' 이 100을 초과한다면
    if 100 - ate < ate + mr[i] - 100:   # 100을 넘기 전의 점수와 100을 넘긴후의 점수 중 뭐가 더 100에 가까운지 비교
        ans = ate
    elif 100 - ate >= ate + mr[i] - 100:  # 100까지의 거리가 같거나 100초과하는 것이 더 크다면
        ans = ate + mr[i]
print(ans)