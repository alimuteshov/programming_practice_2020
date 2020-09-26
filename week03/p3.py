a = [int(i) for i in input().split()]
t = 0
for i in range(len(a)):
    for j in range(len(a)):
        if ((a[i] == a[j]) & (i!=j)):
            t=t+1
print(t//2)
