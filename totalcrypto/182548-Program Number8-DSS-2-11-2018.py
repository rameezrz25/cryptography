
def checkprime(n):
    flag = 0
    for i in range(2, n, 1):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        return 0

    return 1
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
        print('error')
        exit()
    s1=Square_and_Multiply(e1,r,p)
    s1=s1%q
    print('s1',s1)
    f.write('s1 ' + str(s1)  + '\n')

    rinv=ExEucMethod(q,r)
    s2=((m+d*s1)*rinv)%q
    print('s2',s2)
    f.write('s2 ' + str(s2)  + '\n')

    return s1,s2
def sigver(s1,s2,m):
    s2inv=ExEucMethod(q,s2)
    #print(s2inv)
    v1=Square_and_Multiply(e1,m*s2inv,p)
    v2=Square_and_Multiply(e2,s1*s2inv,p)
    v=((v1*v2)%p)%q
    if(s1==v):
        print('signature is verified')
        f.write('signature is verified'  + '\n')

    else:
        print('signature is not verified')
        f.write('signature is not verified'  + '\n')
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
if(checkprime(p)!=0):
    print('p is not prime')
    exit()
q=int(input('enter the prime no q: '))
if(checkprime(p)!=0):
    print('q is not prime')
    exit()
if((p-1)%q!=0):
	print('p-1!= 0 mod q')
	exit()


e0=int(input('enter the value of e0: '))
chkprm(e0,p)
z=(p-1)/q
e1=Square_and_Multiply(e0,int(z),p)
#print(e1)
d=int(input('enter the value of d: '))
e2=Square_and_Multiply(e1,d,p)
#print(e2)


m=int(input('enter the Message digest: '))

'''m=''
for i in mi:
    m+=str(ord(i))
m=int(m)'''
print('public key',e1,e2,p,q)
print('private key',d)
r=int(input('enter the value of r: '))
f = open("dss", "w")
f.write('enter the prime no p: ' + str(p) + '\n')
f.write('enter the prime no q: ' + str(q) + '\n')
f.write('enter the prime no e0: ' + str(e0) + '\n')
f.write('e1: ' + str(e1) + '\n')
f.write('e2: ' + str(e2) + '\n')
f.write('enter the prime no d: ' + str(d) + '\n')
f.write('enter the prime no r: ' + str(r) + '\n')
f.write('enter the Message digest: ' + str(m) + '\n')
f.write('public key ' + str(e1) + ',' +str(e2) + ',' +str(p) + ',' +str(q)  + '\n')
f.write('private key ' + str(d)  + '\n')

s1,s2=siggen(e1,r,p,m,q,d)
sigver(s1,s2,m)
f.close()