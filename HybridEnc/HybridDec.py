__author__ = 'vijaychandra'
import math
from Crypto.Cipher import AES

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

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open("dec_" + file_name[3:], 'wb') as fo:
        fo.write(dec)

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

#get C(C1,C2,C3) and a(secret key)
file = open('PublicKey.txt', 'r');
p = int(file.readlines()[0])
file = open('SecretKey.txt', 'r');
a = int(file.readlines()[0])
file = open('Cipher.txt', 'r');
C2 = int(file.readlines()[0])
file = open('Cipher.txt', 'r');
C3 = int(file.readlines()[1])

C2Dash = squareAndMultipy(C2,a,p);
C2dashinv = extendedEuclideanAlg(C2Dash, p);
KDash = (C3 * C2dashinv)%p;

inpfile = input("Enter the name of the file you wish to decrypt along with the extension (For example: testenc.jpeg): ")

if(len(str(hex(KDash).lstrip('0x'))) <32):
    key = str.encode('0'+(hex(KDash)).lstrip('0x'))
if(len((hex(KDash).lstrip('0x'))) == 32):
    key = str.encode((hex(KDash)).lstrip('0x'))

F = decrypt_file(inpfile, key)

print("Decrytion done")

