a=int(input())
def num(d):
    t=0
    s=0
    while (d):
        t=d%10
        s+=t
        d=d//10
    return s
while a>9:
    a=num(a)
print(a)