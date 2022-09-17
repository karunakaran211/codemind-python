n=int(input())
c=0
d=0
for i in str(n):
 if(int(i)%2==0):
     c+=1
 elif(int(i)%2==1):
     d+=1
if(len(str(n))==c):
    print('Even')
elif(len(str(n))==d):
    print('Odd')
else:
    print('Mixed')
