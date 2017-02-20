__author__ = 'vijaychandra'
import math
from numpy import prod
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

p = int(input("Enter the value of p: "))
t = int(input("Enter the value of t + 1: "))
shares = []
numerator = []
values = []
for i in range(0,t):
    share = []
    x = int(input("Enter share number: "))
    y = int(input("Enter share " + str(x) + "'s " + "value: "))
    numerator.append(x)
    values.append(y)
    share.append(x)
    share.append(y)
    shares.append(share)

#print(shares)

numerators = []

for i in range(0,len(numerator)):
    x = prod(numerator)*((-1)**(len(numerator)-1))
    y = int(x/numerator[i])
    numerators.append(int(y))

#print(numerators)

denominators = []
for i in range(0, len(numerator)):
    denominator = []
    for j in range(0, len(numerator)):
        x = numerator
        denominator.append(x[i] - x[j])
    denominator.remove(0)
    product = prod(denominator)
    denominators.append(extendedEuclideanAlg(product,p))


key = 0
for i in range(0,len(numerator)):
    key = numerators[i]*denominators[i]*values[i] + key

print("Key: " + str(bin(key%p).lstrip('0b')))
