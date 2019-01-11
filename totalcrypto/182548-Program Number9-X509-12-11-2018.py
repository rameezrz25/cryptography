import hashlib
import math
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
            # print('y=',y)
        a = a * a % n
        # print('a=',a)
    return y
def sigver(s,e,n):
    v=Square_and_Multiply(s,e,n)
    print('V',v)
    if(s==v):
        print('SIGNATURE VERIFIED')
    else:
        print('SIGNATURE NOT VERIFIED')
def siggen(m,d,n):
    s=Square_and_Multiply(m,d,n)
    print('S',s)
    return s

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
    return t
def genkey(p, q):
    if p == q:
        print('p cannot be equal to q')
        return 0
    if (checkprime(p) or checkprime(q)):
        print('p or q is not prime')
        exit() 

    n = p * q
    if n < 127:
        print('n value is less than 127')
    phi = (p - 1) * (q - 1)
    '''e = random.randrange(2, phi)
    hcf = gcd(e, phi)
    while hcf != 1:
        e = random.randrange(2, phi)
        hcf = gcd(e, phi)'''
    e=int(input('enter value of e '))
    d = ExEucMethod(phi, e)

    if d < 0:
        d = d % phi
    return e, d, n
f = open("input.txt", "r")
d=f.read()
f1 = open("op.txt", "w")
f1.write(str(d))
f1.write("\n")
m1=hashlib.sha256(str(d).encode()).hexdigest()
print(m1)
M_digest=int(m1,16)
print(M_digest)
p = int(input('enter the value of p '))
q = int(input('enter the value of q '))
e, d, n = genkey(p, q)
print('public key ', e, n)
#f.write('public key ' + str(e) + ',' + str(n) + '\n')
print('private key ', d, n)
#f.write('private key ' + str(d) + ',' + str(n) + '\n')
s=siggen(M_digest,d,n)
sigver(s,e,n)