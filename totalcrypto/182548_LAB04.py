pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

intp= ['58 ', '50 ', '42 ', '34 ', '26 ', '18 ', '10 ', '2',
             '60 ', '52 ', '44 ', '36 ', '28 ', '20 ', '12 ', '4',
             '62 ', '54 ', '46 ', '38 ', '30 ', '22 ', '14 ', '6', 
            '64 ', '56 ', '48 ', '40 ', '32 ', '24 ', '16 ', '8', 
            '57 ', '49 ', '41 ', '33 ', '25 ', '17 ', '9 ', '1',
             '59 ', '51 ', '43 ', '35 ', '27 ', '19 ', '11 ', '3',
             '61 ', '53 ', '45 ', '37 ', '29 ', '21 ', '13 ', '5',
             '63 ', '55 ', '47 ', '39 ', '31 ', '23 ', '15 ', '7']

finpi = ['40 ', '8 ', '48 ', '16 ', '56 ', '24 ', '64 ', '32',
                 '39 ', '7 ', '47 ', '15 ', '55 ', '23 ', '63 ', '31',
                 '38 ', '6 ', '46 ', '14 ',  '54 ', '22 ', '62 ', '30',
                 '37 ', '5 ', '45 ', '13 ', '53 ', '21 ', '61 ', '29',
                 '36 ', '4 ', '44 ', '12 ', '52 ', '20 ', '60 ', '28',
                 '35 ', '3 ', '43 ', '11 ', '51 ', '19 ', '59 ', '27', 
                 '34 ', '2 ', '42 ', '10 ', '50 ', '18 ', '58 ', '26',
'33 ', '1 ', '41 ', '9 ', '49 ', '17 ', '57 ', '25']


pc2 = [13, 16, 10, 23, 0, 4,
       2, 27, 14, 5, 20, 9,
       22, 18, 11, 3, 25, 7,
       15, 6, 26, 19, 12, 1,
       40, 51, 30, 36, 46, 54,
       29, 39, 50, 44, 32, 47,
       43, 48, 38, 55, 33, 52,
       45, 41, 49, 35, 28, 31]
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]
S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]
def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval 
    return binval

def split(s, n):
    return [s[k:k+n] for k in range(0, len(s), n)]

def substitute(d):
        subblocks = split(d, 6)
        res = list()
        for i in range(len(subblocks)): 
            block = subblocks[i]
            r= int(str(block[0])+str(block[5]),2)
            c = int(''.join([str(x) for x in block[1:][:-1]]),2) 
            val = S_BOX[i][r][c]
            bin = binvalue(val, 4)
            res += [int(x) for x in bin]
        str1 = ''.join(str(e) for e in res)
        return str1


def swapper(lb,lr):
    t = lb
    lb = lr
    lr = t
    return lb,lr
def aip(P_TABLE, PLAINTEXT):
    permutated_M = ""
    for index in P_TABLE:
        permutated_M += PLAINTEXT[int(index) - 1]
    return permutated_M
def fun(x,rk):
    x1=''
    for i in range(48):
        x1+=x[int(E[i])-1]
    x1=aip(E,x)
    xo=xor(x1,rk)
    so=substitute(xo)
    so=aip(P,so)
    return so
def xor(a, b):
    xo=''
    lb=''
    xo=a
    lb=b
    return '{1:0{0}b}'.format(len(xo), int(xo, 2) ^ int(lb, 2))

def mixer(lb,rb,rk):
    x = rb
    xo = fun(x,rk)
    lb = xor(xo,lb)
    return lb

def roundkey(x):
    rndkey = ['0']*16
    for i in range(16):
        ip=['0']*48
        f.write('round key'+str(i+1)+'\n')
        #print('round key', i + 1)

        k = 0
        xl = ''
        xr = ''
        xl = x[:28]
        xr = x[28:]
        if i == 0 or i == 1 or i == 8 or i == 15:
            s = 1
        else:
            s = 2
        xl = shiftbit(xl, s)
        xr = shiftbit(xr, s)
        x = xl[0:] + xr[0:]
        for j in range(48):
            ip[j] = x[pc2[j]]
        str2 = ''.join(str(e) for e in ip)
        rndkey[i]=str2
        f.write(str2+"\n")
        #print(str2)
        #f.write(hex(int(str2,2))+'\n')
    return rndkey


def shiftbit(string1, n):
    i = 0
    l = list(string1)
    # print(l)
    while i < n:
        temp = l.pop(0)
        l.append(temp)
        i += 1
    string1 = ''.join(l)
    return string1

et1 = ''
dt1 = ''
ft = ''
ip=''
inp = (input('enter the plaintext in size 8 character:'))
bt1 = [bin(ord(c))[2:].zfill(8) for c in inp]
s1 = ''.join(bt1)
ip=aip(intp,s1)
print('after initial permutation',ip)

#p = (input('enter the key in size 8 character:'))
#bt = [bin(ord(c))[2:].zfill(8) for c in p]
#s = ''.join(bt)
f = open("roundkeypossiblekey", "w")
f1=open("possiblekey.txt","r")
f2 = open("cipertextpossiblekey", "w")
s=''
k=0
for filind in f1:
    k+=1
    s=filind[0:64]
    print('NO '+str(k)+": key:"+s)
    f.write('NO '+str(k)+": key:"+s+'\n')
    et = aip(pc1, s)
    rndkey=roundkey(et)
    inpl = s1[0:32]
    inpr = s1[32:64]
    for i in range(16):
        inpl=mixer(inpl,inpr,rndkey[i])
        if i!=15:
            inpl,inpr=swapper(inpl,inpr)
        print('round :',i+1)
        print(inpl,inpr)
        inp=inpl[0:32]+inpr[0:32]
    print('ciper text after 16 round',inp)
    inp=aip(finpi,inp)
    print('ciper text after final permutation',inp)

    f2.write('ciper text after final permutation:'+inp+"\n")
f.close()
f1.close()
f2.close()





