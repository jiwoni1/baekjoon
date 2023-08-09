h, m = map(int, input().split())    # 입력값을 int로 바꿔 h와 m으로 분배

time = h * 60 + m                   # 시간을 분으로 단위 통일 시켜줌
time -= 45                          # x min - 45 min

if time < 0:                        # 0시 경우에는 time값이 음수가 나와 계산 불가
    time += 60 * 24                 # 계산을 위해 0시 -> 24시로 바꿔줌

h = time // 60                      # h 는 time의 몫
m = time % 60                       # min은 time의 나머지

print(h, m)

