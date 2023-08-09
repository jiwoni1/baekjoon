x = int(input())
y = int(input())

# if x > 0 and y > 0:     # 직관적으로 풀기
#     print(1)
# if x < 0 and y > 0:
#     print(2)    
# if x < 0 and y < 0:
#     print(3)
# if x > 0 and y < 0:
#     print(4)

if x > 0:         # 중첩 if로 풀기
    if y > 0:
        print(1)
    else:
        print(4)
if x < 0:
    if y > 0:
        print(2)
    else:
        print(3)