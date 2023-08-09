h, m = map(int, input().split())       # 입력값을 int로 바꿔서 h, m에 넣기
run_time = int(input())                # 소요시간 받기 ***? 근데 한 줄로 받아야 더 좋은건지, 따로 input으로 받아도 괜찮은 건지 의문

end_time = h * 60 + m + run_time       # h -> m으로 단위 변경 + 소요시간까지 더해서 끝나는 시간(분) 구하기

h = end_time // 60                     # 시간 = 60으로 나눈 몫
m = end_time % 60                      # 분 = 60으로 나눈 나머지

if h >= 24:                            # h이 24 이상으로 표시되면 안됨 
    h -= 24                            # h가 24이상이라면 24를 빼줌

print(h , m)