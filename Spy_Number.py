a=int(input())
a1=0
a2=1
while a>0:
    b=a%10
    a1+=b
    a2*=b
    a=a//10
if a1==a2:
    print('Spy Number')
else:
    print('Not Spy Number')
