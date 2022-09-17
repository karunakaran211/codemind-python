n=int(input())
s=0
h=1
while n>0:
    r=n%10
    s+=r
    h*=r
    n=n//10
if s==h:
    print('Spy Number')
else:
    print('Not Spy Number')
