total_pri = int(input())
total_num = int(input())

ans = 0
for i in range(total_num):
    price, num = map(int, input().split())
    ans += price * num

if ans == total_pri:
    print('Yes')
else:
    print('No')