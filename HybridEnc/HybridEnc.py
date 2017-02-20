__author__ = 'vijaychandra'
import os
import random
from Crypto import Random
from Crypto.Cipher import AES
import codecs

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

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=128):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open("enc_"+ file_name, 'wb') as fo:
        fo.write(enc)

#get (p,g,h)
file = open('PublicKey.txt', 'r');
p = int(file.readlines()[0])
file = open('PublicKey.txt', 'r');
g = int(file.readlines()[1])
file = open('PublicKey.txt', 'r');
h = int(file.readlines()[2])

hexlify = codecs.getencoder('hex')
key = hexlify(os.urandom(16))[0];


inpfile = input("Enter the name of the file you wish to encrypt along with the extension (For example: test.jpeg): ")
C1 =encrypt_file(inpfile, key) #add user input for asking the filename
Kdash = int(key, 16)
r = random.randint(0,p-2)
C2 = squareAndMultipy(g,r,p)
C3 = squareAndMultipy(h,r,p)
C3 = squareAndMultipy(Kdash*C3,1,p)


target = open("Cipher.txt",'w');
target.write("%s" %C2);
target.write("\n");
target.write("%s" %C3);
target.write("\n");

print("Encrytion done")
