n=int(input())
s=1
h=0
while n>0:
    r=n%10
    s*=r
    h+=r
    e=s-h
    n=n//10
print(e)
    