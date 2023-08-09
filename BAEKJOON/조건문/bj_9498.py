test_score = int(input())       # 점수 값을 input으로 받고 int로 형 변환

if 90 <= test_score <= 100:       # 점수대에 따라 print값을 나눔
    print('A')
elif 80 <= test_score <= 89:
    print('B')
elif 70 <= test_score <= 79:
    print('C')
elif 60 <= test_score <= 69:
    print('D')
else:
    print('F')