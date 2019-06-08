x=input()
n=int(input())
s=""
s+=x
v=""
def anagram(x1,x2):
    if(len(x1)==len(x2)):
        x1=sorted(x1)
        x2=sorted(x2)
        if(x1==x2):
            return 0;
        else:
            return 1;
for i in range(n):
    a,b=input().split()
    if a=="L":
        s=s[int(b):]+s[0:int(b)]
    elif a=="R":
        s=s[len(s)-int(b):]+s[0:len(s)-int(b)]
    s=s.replace(" ","")
    v+=s[0]
for i in range(len(x)-len(v)):
    x1=x[i:i+len(v)]
    f=anagram(x1,v)
    if(f==0):
        v=1
        break
if v==1:
    print("YES")
else:
    print("NO")

        
    
