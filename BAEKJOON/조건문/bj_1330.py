A, B = map(int, input().split())     # A, B에 입력

if A > B:
    print('>')
elif A < B:
    print('<')
elif A == B:
    print('==')