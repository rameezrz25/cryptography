import math
ip= ['58 ', '50 ', '42 ', '34 ', '26 ', '18 ', '10 ', '2',
             '60 ', '52 ', '44 ', '36 ', '28 ', '20 ', '12 ', '4',
             '62 ', '54 ', '46 ', '38 ', '30 ', '22 ', '14 ', '6', 
            '64 ', '56 ', '48 ', '40 ', '32 ', '24 ', '16 ', '8', 
            '57 ', '49 ', '41 ', '33 ', '25 ', '17 ', '9 ', '1',
             '59 ', '51 ', '43 ', '35 ', '27 ', '19 ', '11 ', '3',
             '61 ', '53 ', '45 ', '37 ', '29 ', '21 ', '13 ', '5',
             '63 ', '55 ', '47 ', '39 ', '31 ', '23 ', '15 ', '7']

ipi = ['40 ', '8 ', '48 ', '16 ', '56 ', '24 ', '64 ', '32',
                 '39 ', '7 ', '47 ', '15 ', '55 ', '23 ', '63 ', '31',
                 '38 ', '6 ', '46 ', '14 ',  '54 ', '22 ', '62 ', '30',
                 '37 ', '5 ', '45 ', '13 ', '53 ', '21 ', '61 ', '29',
                 '36 ', '4 ', '44 ', '12 ', '52 ', '20 ', '60 ', '28',
                 '35 ', '3 ', '43 ', '11 ', '51 ', '19 ', '59 ', '27', 
                 '34 ', '2 ', '42 ', '10 ', '50 ', '18 ', '58 ', '26',
'33 ', '1 ', '41 ', '9 ', '49 ', '17 ', '57 ', '25']

def aip(P, PT):
    p = ""
    for i in P:
        p += PT[int(i)-1]
    return p

et1=''
dt1=''
ft=''
p=(input('enter the plaintext: '))
tl=len(p)
if tl%8!=0:
    padbit=8-(len(p)%8)
else:
    padbit=0
i=0
while (i<padbit):
    i+=1
    p+='0'
print('the text to be permutated after pading',p)
bt=[bin(ord(c))[2:].zfill(8) for c in p]
s=''.join(bt)
print('initial permutation')
for i in range(0,len(s),64):
    t=s[i:i+64]
    et= aip(ip,t)
    print(et)
    print(hex(int(et,2)))
    et1+=et
print('final permutation')
for j in range(0,len(et1),64):
    x=et1[j:j+64]
    dt=aip(ipi,x)
    print(dt)
    print(hex(int(dt,2)))
    dt1+=dt

for k in range(0,len(dt1),8):
    o=dt1[k:k+8]
    ft+=chr(int(o,2))
print('plaintext',ft[:tl])
