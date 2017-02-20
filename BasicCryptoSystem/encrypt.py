#Author: Vijay Lingam

from __future__ import print_function
import binascii

s = " ";
message = [];
messagestr = [];
file = open('input.txt', 'r')
for line in file.readlines():
	messagestr.append(line);
binaryMessage = bin(int(binascii.hexlify(s.join(messagestr)), 16));

#print("Binary Message: ");
#print(binaryMessage);
#print();

Z = [1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1]; # value of Z (32 bit)
C = [0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0]; # value of C (32 bit)

binaryMessage = binaryMessage[2:];
for k in range(0,len(binaryMessage)):
	num = int(binaryMessage[k]);
	message.append(num);

messsageLength = len(message);
cipherText = [];
for x in range(0, (messsageLength-32)):
	sum = 0;
	for y in range(0,32): #indexes from 1 to 32
		sum = sum + C[y]*Z[x+y];
	Z.append(sum);
for i in range(0,messsageLength):
	cipherText.append((message[i] + Z[i])%2);

for j in range(0,messsageLength):
	#print (cipherText[j], end=""); 
	cipherText[j] = str(cipherText[j]);

encStr = ''.join(cipherText);
text_file = open("encryptedtext.txt", "w")
text_file.write("%s" % encStr)
text_file.close()

print("File Encrypted");