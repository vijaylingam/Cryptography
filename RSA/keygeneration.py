__author__ = 'vijaychandra'
import random
import math
lambdavalue = input('Input the value of lambda: ');

x = int(int(lambdavalue) / 2);

print("The value of x (size of prime) is: %d" % x);


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


def jacobi(a, n):
    """
    Return Jacobi symbol (or Legendre symbol if n is prime)
    """
    s = 1
    while True:
        if n < 1: raise ValueError("Too small module for Jacobi symbol: " + str(n))
        if n & 1 == 0: raise ValueError("Jacobi is defined only for odd modules")
        if n == 1: return s
        a = a % n
        if a == 0: return 0
        if a == 1: return s

        if a & 1 == 0:
            if n % 8 in (3, 5):
                s = -s
            a >>= 1
            continue

        if a % 4 == 3 and n % 4 == 3:
            s = -s

        a, n = n, a
    return


z = True;
new = 0;
p = 0;
q = 0;
# Generating first prime number (P)
while (z):
    new = random.randint(2 ** (x - 1), 2 ** x);
    if (new % 2 == 0):
        z = True;
    else:
        prime = primegenerator(new);
        if (prime != -1):
            p = new;
            z = False;
# Generating second prime number (Q)
k = True;
while (k):
    new = random.randint(2 ** (x - 1), 2 ** x);
    if (new % 2 == 0):
        k = True;
    else:
        prime = primegenerator(new);
        if (prime != -1):
            q = new;
            k = False;


def gcd(a, b):  # euclid gcd
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

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

print("Value of P is: %d" % p);
print("Value of Q is: %d" % q);

product = p * q;
print("Value of n(PxQ): %d" % product);

euler_of_n = (p - 1) * (q - 1);

print("Euler Totient Value: %d" % euler_of_n);

condition = True;
e = 0;
while (condition):
    e1 = random.randint(1, euler_of_n);
    if (gcd(e1, euler_of_n) == 1):
        e = e1;
        condition = False;

print("Value of e is: %d" % e);

xyz = extendedEuclideanAlg(e, euler_of_n); #this is d (inverse of e(mod(euler_of_n)))
print("Value of d is: %d" % xyz);

target = open("PublicKey.txt",'w');
target.write("%s" %e);
target.write("\n");
target.write("%s" %product);

target1 = open("SecretKey.txt", 'w');
target1.write("%s" %xyz);
target1.write("\n");
target1.write("%s" %product);

print("value of (e*d)%(totientOfN): ");
#print((e*xyz)%euler_of_n);
