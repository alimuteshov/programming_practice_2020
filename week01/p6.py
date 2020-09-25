max=int(input())
submax=int(input())
t=0
if max<submax:
   t=max
   max=submax
   submax=t
n=int(input())
while n!=0:
    if (n>submax):
        submax=n
    if (n>max):
        submax=max
        max=n
    n=int(input())
print(submax)