A,B = map(int,input().split())
C = int(input())

total = A*60 + B + C
hour = (total // 60) % 24
minute = total % 60
print(hour, minute)


