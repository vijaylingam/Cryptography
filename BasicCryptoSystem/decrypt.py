#Author: Vijay Lingam

from __future__ import print_function
import binascii

encryptedMessage = [];
file = open('encryptedtext.txt', 'r')
for line in file.readlines():
	encryptedMessage.append(line);

Z = [1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,1]; # value of Z (32 bit)
C = [0,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0]; # value of C (32 bit)

cipherMessage = [];
encryptedstring = encryptedMessage[0];
for k in range(0,len(encryptedstring)):
	num = int(encryptedstring[k]);
	cipherMessage.append(num);

messsageLength = len(cipherMessage);
decryptedText = [];
for x in range(0, (messsageLength-32)):
	sum = 0;
	for y in range(0,32): #indexes from 1 to 32
		sum = sum + C[y]*Z[x+y];
	Z.append(sum);
for i in range(0,messsageLength):
	decryptedText.append((cipherMessage[i] + Z[i])%2);

for j in range(0,messsageLength):
	#print (decryptedText[j], end=""); 
	decryptedText[j] = str(decryptedText[j]);	

decStr = ''.join(decryptedText);
decStr = '0b'+decStr;
n = int(decStr, 2)
dec = binascii.unhexlify('%x' % n);

text_file = open("decryptedtext.txt", "w")
text_file.write("%s" % dec)
text_file.close()

print("File decrypted");