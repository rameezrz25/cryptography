
def DB(ciphr, d, n):
    pt = Square_and_Multiply(ciphr, d, n)
    return pt
def checkprime(n):
    flag = 0
    for i in range(2, n, 1):
        if n % i == 0:
            flag = 1
            break
    if flag == 0:
        return 0

    return 1


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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


def size(pt, n):
    st = ''
    st1 = ''
    count = 0
    if ord(pt[0]) < n:
        st += str(ord(pt[0]))

    for i in range(1, len(pt)):

        if int(st) < n:
            st += str(ord(pt[i]))
            st1 += str(ord(pt[i - 1]))
            count += 1

    if len(pt) == 1:
        st1 += str(ord(pt[0]))
        print("blocktextvalue :-", st1)
        f.write('blocktextvalue' + '\n' + str(st1) + '\n')
        pt1 = ''
    elif int(st) < n:
        st1 = st
        pt1 = ''
    else:

        pt1 = pt[count:]
        print("blocktextvalue :-", st1)
        f.write('blocktextvalue' + '\n' + str(st1) + '\n')
    return int(st1), pt1


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
def BE(pt, e, n):
    block_ciphr = Square_and_Multiply(pt, e, n)
    return block_ciphr


def E(d, n, plaintext):
    cipher = [Square_and_Multiply(ord(char), d, n) for char in plaintext]
    return (cipher)


def D(e, n, ciphertext):
    plain = [chr(Square_and_Multiply(char, e, n)) for char in ciphertext]
    return ''.join(plain)


f = open("rsa", "w")
p = int(input('enter the value of p '))
q = int(input('enter the value of q '))
plaintext = input('enter the plaintext ')
f.write('plaintext ' + plaintext + '\n')
e, d, n = genkey(p, q)

print('public key ', e, n)
f.write('public key ' + str(e) + ',' + str(n) + '\n')
print('private key ', d, n)
f.write('private key ' + str(d) + ',' + str(n) + '\n')
c = E(e, n, plaintext)
pt = D(d, n, c)
print('cipher text after encription using stream cipher', c)
f.write('cipher text after encription using stream cipher' + '\n' + str(c) + '\n')
print('plain text after decription using stream cipher', pt)
f.write('plain text after decription using stream cipher' + '\n' + str(pt)+'\n\n')

f.write('blockcipher'+'\n')
l1 =[]
l2 =[]
ini = plaintext
while ini != '':
    print("block")
    pt1, fin = size(ini, n)
    block_ciphr = BE(pt1, e, n)
    f.write('cipher text after encription using block cipher' + '\n' + str(block_ciphr) + '\n')
    print('blockcipher:',block_ciphr,)
    l2.append(str(block_ciphr))
    dcpt = DB(block_ciphr, d, n)
    print("After Decryption :-", dcpt)
    f.write('plaintext text  value after Decryption using block cipher' + '\n' + str(dcpt) + '\n\n')
    l1.append(str(dcpt))
    ini = fin
    print()
print(l1)
print('plaintext is :-',end='')
f.write('plaintext'+'\n')
x = ''
for i in range(len(l1)):
    for j in l1[i]:
        x += j
        if int(x) > 31:
            print(chr(int(x)),end="")
            f.write(str(chr(int(x))))

            x = ''
f.close()