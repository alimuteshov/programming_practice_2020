text = input()
n = int(input())
print("Hello, ",end="")
for i in range(n-1):
    print(text, end=", ")
print(text)
