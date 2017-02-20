__author__ = 'vijaychandra'
import random
import math
def rabin(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if (num % prime == 0):
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime.
    return rabin(num)

def primegenerator(n):  # using rabin miller method
    count = 0;
    for i in range(0, 20):
        x = isPrime(n);
        if (x == True):
            count = count + 1;
    if (count == 20):
        return n;
    else:
        return -1;

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

x = 150;
generatorCondition = True;
p = 0; #prime
q = 0; #prime
r = 0;
while(generatorCondition):
    z = True;
    new = 0;
    q = 0;
    # Generating first prime number (P)
    while (z):
        new = random.randint(2 ** (x - 1), 2 ** x);
        if (new % 2 == 0):
            z = True;
        else:
            prime = primegenerator(new);
            if (prime != -1):
                q = new;
                z = False;

    # Generating p2
    r = random.randint(2 ** (x - 1), 2 ** x);
    # Computing p
    p = (q*r)+1;

    check = primegenerator(p);
    if(check != -1):
        print("Value of p is: %d" % p);
        generatorCondition = False;
    else:
        generatorCondition = True;

Condition = True;
generator = 0;
h = 0;
while(Condition):
    x = random.randint(1, p);
    value = squareAndMultipy(x,math.floor((p-1)/q),p);
    if(value != 1):
        h = x;
        generator = value;
        Condition = False;
    else:
        Condition = True;

print("Value of g is: %d " %generator);

a = random.randint(1, q);

h = squareAndMultipy(generator, a, p);

print("Value of h is: %d" %h);
print("Secret Key (a) is : %d" %a);

target = open("PublicKey.txt",'w');
target.write("%s" %p);
target.write("\n");
target.write("%s" %generator);
target.write("\n");
target.write("%s" %h);

target1 = open("SecretKey.txt", 'w');
target1.write("%s" %a);

