a=int(input())
b=1
for i in range (2,a):
    if a%i==0:
        b=b+i
if b==a:
    print(True)
else:
    print(False)