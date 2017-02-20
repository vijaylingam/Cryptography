__author__ = 'vijaychandra'
file = open('PublicKey.txt', 'r');
e = int(file.readlines()[0])
file = open('PublicKey.txt', 'r');
n = int(file.readlines()[1])
#print(e);
#print(n);
range1 = n-1;
k = int(input("enter message in range 0 to %d: " %range1));

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


encryptedMessage = squareAndMultipy(k,e,n);

target = open("EncryptedMessage.txt",'w');
target.write("%s" %encryptedMessage);