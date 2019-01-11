
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

def siggen(e1,r,p,m):
    s1=Square_and_Multiply(e1,r,p)
    print('s1',s1)
    f.write('s1 ' + str(s1)  + '\n')
    rin=ExEucMethod(p-1,r)
    print('rin',rin)
    f.write('rin ' + str(rin)  + '\n')
    s2=((m-(d*s1))*rin)%(p-1)
    print('s2',s2)
    f.write('s2 ' + str(s2)  + '\n')
    return s1,s2
def sigver(s1,s2,m):
    v1=Square_and_Multiply(e1,m,p)
    v2=(Square_and_Multiply(e2,s1,p)*Square_and_Multiply(s1,s2,p))%p
    print('v1: ',v1)
    f.write('v1 ' + str(v1)  + '\n')
    print('v2: ',v2)
    f.write('v2 ' + str(v2)  + '\n')
    if(v1==v2):
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
e1=int(input('enter the value of e1: '))
chkprm(e1,p)
r=int(input('enter the value of r: '))
d=int(input('enter the value of d: '))
mi=input('enter the Message: ')
m=''
for i in mi:
    m+=str(ord(i))
m=int(m)
e2=int(input('enter e2: '))
print('public key',e1,e2,p)
print('private key',d)
f = open("Elgamal", "w+")
f.write('enter the prime no p: ' + str(p) + '\n')
f.write('enter the prime no e1: ' + str(e1) + '\n')
f.write('enter the prime no e2: ' + str(e2) + '\n')
f.write('enter the prime no d: ' + str(d) + '\n')
f.write('enter the prime no r: ' + str(r) + '\n')
s1,s2=siggen(e1,r,p,m)
sigver(s1,s2,m)
f.close()
