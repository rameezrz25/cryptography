
import hashlib
def Square_and_Multiply(a, x, n):
    b = bin(x)[2:]
    b = str(b)
    y = 1
    for i in range(len(b) - 1, -1, -1):
        if b[i] == '1':
            y = y * a % n
            #print('y=',y)
        a = a * a % n
        # print('a=',a)
    return y
def keygen(e1,d,p):
    e2=Square_and_Multiply(e1,d,p)
    return e2
def chkprm(e1,p):
    y=Square_and_Multiply(e1,p-1,p)
    if(y==1):
        for i in range(1,(p-1)):
            y=Square_and_Multiply(e1,i,p)
            if(y==1):
                print('not primitive root')
                exit()
    else:
        print('not primitive root')
        exit()

def siggen(e1,r,p,m,q,d):
    if(r>q):
        print('r is not in range')
        exit()
    s1=Square_and_Multiply(e1,r,p)
    s1=str(m)+str(s1)
    s1= int(hashlib.md5(s1.encode()).hexdigest()[2:],16)
    print('s1',s1)
    s2=r+((d*s1)%q)
    print('s2',s2)
    return s1,s2
def sigver(s1,s2,m):
    v1=Square_and_Multiply(e1,s2,p)
    exe2=ExEucMethod(p,e2)
    v2=Square_and_Multiply(exe2,s1,p)
    v = str(m)+str((v1*v2)%p)
    v=int(hashlib.md5(v.encode()).hexdigest()[2:],16)
    if(s1==v):
        print('signature is verified')
    else:
        print('signature is not verified')
def ExEucMethod(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while (r2 > 0):
        q = int(r1 / r2)
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t
    s = s1
    t = t1
    return t%a
p=int(input('enter the prime no p: '))
q=int(input('enter the prime no q'))
if((p-1)%q!=0):
	print('p-1!= 0 mod q')
	exit()


e0=int(input('enter the value of e0: '))
chkprm(e0,p)
z=(p-1)/q
e1=Square_and_Multiply(e0,int(z),p)
d=int(input('enter the value of d: '))
e2=Square_and_Multiply(e1,d,p)



mi=input('enter the Message: ')
m=''
for i in mi:
    m+=str(ord(i))
m=int(m)
print('public key',e1,e2,p,q)
print('private key',d)
r=int(input('enter the value of r: '))
s1,s2=siggen(e1,r,p,m,q,d)
sigver(s1,s2,m)
