__author__ = 'vijaychandra'
import random
import hashlib
import math
from Crypto.Hash import SHA

def squareAndMultipy(x,c,n):
    c1 = bin(c).lstrip('0b');
    c2 = [];
    for bit in c1:
        c2.append(int(bit));
    c2.reverse()
    l = len(str(bin(c).lstrip('0b')));
    z = 1;
    for i in range(l-1,-1,-1):
        z = pow(z,2,n);
        if(c2[i] == 1):
            z = (z*x)%n
    return z;

def extendedEuclideanAlg(a, b):
    a0 = a;
    b0 = b;
    t0 = 0;
    t = 1;
    s0 = 1;
    s = 0;
    q = math.floor(a0 / b0);
    r = a0 - q * b0;
    while (r > 0):
        temp = t0 - q * t
        t0 = t
        t = temp
        temp = s0 - q * s
        s0 = s
        s = temp
        a0 = b0
        b0 = r
        q = math.floor(a0 / b0)
        r = a0 - q * b0

    r = b0;
    return s % b;

file = open('VerKey.txt', 'r')
p = int(file.readlines()[0])
file = open('VerKey.txt', 'r')
q = int(file.readlines()[1])
file = open('VerKey.txt', 'r')
g = int(file.readlines()[2])
file = open('VerKey.txt', 'r')
h = int(file.readlines()[3])

file1 = open('SignKey.txt', 'r')
a = int(file1.readlines()[0])
C1 = 0  # initializing C1
C2 = 0  # initializing C2
file = input("Type the file name along with the extension: ")
print("Please Wait...")
while(True):
    r = random.randint(0,q-1)
    C1 = squareAndMultipy(g,r,p)%q

    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    sha1 = hashlib.sha1()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)

    rInv = extendedEuclideanAlg(r,q)
    #print(int(sha1.hexdigest(),16))
    C2 = ((int(sha1.hexdigest(),16) + a*C1)*rInv)%q
    if(C1 != 0 and C2 != 0):
        break

#print("Value of C1 is: " + str(C1))
#print("Value of C2 is: "+ str(C2))

target = open("Signature.txt",'w');
target.write("%s" %C1);
target.write("\n");
target.write("%s" %C2);

print("Signing Done!")