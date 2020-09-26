s = input()
a = s.split()
t=0
for i in range(1,len(a)-1):
   if ((a[i]>a[i-1]) & (a[i]>a[i+1])):
       t=t+1
print(t)