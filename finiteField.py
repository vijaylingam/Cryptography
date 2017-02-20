__author__ = 'vijaychandra'
import numpy as np;
import sys;

one = sys.argv[1];
polynomialsList = [];
characteristicEqn = [1,0,0,0,0,0,1,1];
inverseEqn = [];
inverseIndices = [];
input1 = [];
inverseIndices.append(0);
generator = [0, 0, 0, 0, 0, 1, 0];
A = [0, 0, 0, 0, 0, 1, 0];
for i in range(0, 2**7):
    y = '{:07b}'.format(i);
    arr = [];
    for j in range(0,len(y)):
        arr.append(int(y[j]));
    polynomialsList.append(arr);
    print(arr);


print();

remainder = np.polydiv(A, characteristicEqn)[1];

for x in range(1,128):
    xpowerlist = [0]*x+[0];
    xpowerlist[x] = 1;
    xpowerlist.reverse();
    y = (np.polydiv(xpowerlist, characteristicEqn)[1]);
    y = y.astype(np.int64);
    y = np.array(y).tolist();
    if(len(y)<7):
        extra = 7 - len(y);
        y = [0]*extra + y;
    for i in range(0, len(y)):
        y[i] = int(int(y[i])%2);

    inverseEqn.append(y);
    print(y);

for eqn in polynomialsList[1:]:
    inverseIndices.append(inverseEqn.index(eqn));
for i in range(0,len(one)):
    input1.append(int(one[i]));

inputIndex = polynomialsList.index(input1); #correct
out = 125 - inverseIndices[inputIndex]; #correct
invIndex = inverseIndices.index(out); #correct


#formatting output display
print("Given Input: ");
print();
print(np.poly1d(input1));
print();
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ");
print();
print("Additive Inverse of Input:");
print();
print(np.poly1d(input1));
print();
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ");
print();
print("Multiplicative Inverse of Input:");
print();
print(np.poly1d(polynomialsList[invIndex]));
print();
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ");
print();


z = (np.polydiv(np.polymul(polynomialsList[invIndex],input1)%2,characteristicEqn)[1]%2).astype(np.int64);
print(z);



