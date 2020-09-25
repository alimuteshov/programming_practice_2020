n = int(input())
t = 1
sum = 0
for i in range(1,n+1):
    t=i*t
    sum = t + sum
print(sum)