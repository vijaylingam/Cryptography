__author__ = 'vijaychandra'
file = open('SecretKey.txt', 'r');
d = int(file.readlines()[0]);
file = open('SecretKey.txt', 'r');
n = int(file.readlines()[1]);
file = open('EncryptedMessage.txt', 'r');
cipher = int(file.readlines()[0]);


def squareAndMultipy(x,c,n):
    c1 = bin(c).lstrip('0b');
    c2 = [];
    for bit in c1:
        c2.append(int(bit));
    c2.reverse()
    l = len(str(bin(c).lstrip('0b')));
    z = 1;
    for i in range(l-1,-1,-1):
        z = (z**2)%n;
        if(c2[i] == 1):
            z = (z*x)%n;
    return z;


Message = squareAndMultipy(cipher,d,n);
#Message = pow(cipher,d,n);


target = open("DecipheredMessage.txt",'w');
target.write("%s" %Message);
print(Message);