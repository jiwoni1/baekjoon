cook = [list(map(int, input().split())) for _ in range(5)]  # 5명의 참가자의 점수 리스트 생성 (2차원 배열)

r = 0                    # 행
c = 0                    # 열
score = 0                # 점수 합계
com = []
while c < 4 and r < 5:   # 열이 4 미만, 행이 5미만으로 제한
    score += cook[r][c]  # 행 순회 -> 각 행마다 다 더해줌
    c += 1               # 행 순회
    if c == 4:           # 행 다 돌면
        com.append(score)  # 총 점수를 com 리스트에 넣어주고 초기화
        score = 0
        c = 0
        r += 1           # 다음 행

ans = 0                  # com 리스트에서 가장 큰 값 찾기 (가장 점수가 높은 요리사)
for j in range(5):
    if ans < com[j]:
        ans = com[j]
idx = 0                 # 최고점 요리사가 누구인지 인덱스 찾기
for f in com:
    idx += 1
    if f == ans:
        break

print(idx, ans)
