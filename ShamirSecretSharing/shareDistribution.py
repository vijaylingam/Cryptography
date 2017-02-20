__author__ = 'vijaychandra'

import random
import numpy as np;

def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5):  # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:  # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def primegenerator(n):  # solovoy stassen method
    count = 0;
    for i in range(0, 20):
        x = rabinMiller(n);
        if (x == True):
            count = count + 1;
    if (count == 20):
        return n;
    else:
        return -1;

t = int(input("Enter the value of t: "))
n = int(input("Enter the value of n: "))
K = int(input("Enter the value of Key in binary form: "),2)
print("Key: " + str(K))

x = len(bin(K))
p = 0
while (True):
    new = random.randint(2 ** (x - 1), 2 ** x)
    if (new % 2 == 0):
        continue
    else:
        prime = primegenerator(new)
        if (prime != -1):
            p = new
            break
print("The value of p is: " + str(p))
polynomialCoefs = []

for i in range(1,t+1):
    while(True):
        x = random.randint(1,p-1)
        if(x in polynomialCoefs):
            continue
        else:
            polynomialCoefs.append(x)
            break

polynomialCoefs.append(K)

#print(polynomialCoefs)

polynomial = np.poly1d(polynomialCoefs)

#print(polynomial)

output = []

for i in range(1,n+1):
    x = []
    x.append(i)
    x.append(polynomial(i)%p)
    output.append(x)
print()
print(output)
print()
target = open("Shares.txt",'w')
target.write("Value of p is: %s" %p)
target.write("\n")
target.write("%s" %output);
target.write("\n")
target.write("Key: %s" %K);