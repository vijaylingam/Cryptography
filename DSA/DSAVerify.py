__author__ = 'vijaychandra'
import hashlib
import math

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

filename = input("Enter the filename to be verified along with its extension: ")

file = open('VerKey.txt', 'r')
p = int(file.readlines()[0])
file = open('VerKey.txt', 'r')
q = int(file.readlines()[1])
file = open('VerKey.txt', 'r')
g = int(file.readlines()[2])
file = open('VerKey.txt', 'r')
h = int(file.readlines()[3])
file1 = open('Signature.txt', 'r')
C1 = int(file1.readlines()[0])
file1 = open('Signature.txt', 'r')
C2 = int(file1.readlines()[1])

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
sha1 = hashlib.sha1()
with open(filename, 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)
#print("Value of C2 is: " + str(C2))
C2inv = extendedEuclideanAlg(C2, q)
#print(int(sha1.hexdigest(),16))
#print("C2inverse: " + str(C2inv))
t1 = (int(sha1.hexdigest(),16) * C2inv)%q
#print("Value of t1 is: " + str(t1))
t2 = (C1*C2inv)%q
#print("Value of t2 is: " + str(t2))
x1 = squareAndMultipy(g,t1,p)
x2 = squareAndMultipy(h,t2,p)

if(((x1*x2)%p)%q == C1):
    print("Valid Signature")
else:
    print("Invalid Signature")