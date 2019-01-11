pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

pc2 = [13, 16, 10, 23, 0, 4,
       2, 27, 14, 5, 20, 9,
       22, 18, 11, 3, 25, 7,
       15, 6, 26, 19, 12, 1,
       40, 51, 30, 36, 46, 54,
       29, 39, 50, 44, 32, 47,
       43, 48, 38, 55, 33, 52,
       45, 41, 49, 35, 28, 31]


def roundkey(x):
    for i in range(16):
        ip=['0']*48
        print('round key', i + 1)
        f.write('round key '+str(i+1)+'\n')
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
        f.write(str2 + "\n")

        f.write(hex(int(str2,2)) + "\n")
        print(str2)
        print(hex(int(str2,2)))


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


def aip(P_TABLE, PLAINTEXT):
    permutated_M = ""
    for index in P_TABLE:
        permutated_M += PLAINTEXT[int(index) - 1]
    return permutated_M


et1 = ''
dt1 = ''
ft = ''
p = (input('enter the plaintext: '))
bt = [bin(ord(c))[2:].zfill(8) for c in p]
s = ''.join(bt)
f = open("roundkeygeneration.txt", "w")
f.write("plain text: ")
f.write(p+"\n")
for i in range(0, len(s), 64):
    t = s[i:i + 64]
    et = aip(pc1, t)
    print(et)

    et1 += et
k = 0
for j in range(0, len(et1), 56):
    k += 1
    print('block', k)
    x = et1[j:j + 56]
    roundkey(x)
f.close()
