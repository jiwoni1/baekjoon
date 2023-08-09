N = int(input())
scores = [int(input()) for _ in range(N)]

i = 0                  # 현재 인덱스
cnt = 0                # 몇 번 감소시켰는지
d = 0                  # 감소시켜야하는 양
for i in range(N):                               # 현재 원소와 그 뒤에 있는 원소들을 순차적으로 다 비교
    for j in range(i+1, N):
        d = (j - i) - (scores[j] - scores[i])    # (뒤에 있는 원소의 위치 - 내 위치) - (내 점수 - 뒤에있는 점수) 를 하면 최소 몇 번 감소해야하는지 나옴
        if d > 0:                # 감소해야하는 양이 있을 경우에 (양수)
            scores[i] -= d       # 현재 값을 그만큼 빼줌
            cnt += d             # 빼준만큼 카운트
print(cnt)
