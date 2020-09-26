s = input()
a = s.split()
t=0
max=0
min=0

for i in range(1,len(a)):
    if int(a[i])>int(a[max]):
        max=i
    if int(a[i])<int(a[min]):
        min=i

t = a[max]
a[max]=a[min]
a[min]=t

for i in range(len(a)):
    print(a[i],end=" ")