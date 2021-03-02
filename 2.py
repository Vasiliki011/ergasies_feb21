import random

term = int(input("Give the sequence's term you'd like: "))
# The Fibonacci sequence
n0, n1 = 0, 1   # first two terms
# 1os oros:0, 2os:1, 3os:1, 4os:2, 5os:3 kai ta loipa...
count = 2
if term == 1:
   print("Term", term, "equals to:", n0)
   print('Your p:', n0, ',', 'is not prime!')
elif term == 2 or term==3:
    print("Term", term, "equals to:", n1)
    print('Your p:', n1, ',', 'is not prime!')
elif term <= 0:
    print('Please enter a value greater than 0!')
else:
    while count < term:
        p = n0 + n1
        n0 = n1
        n1 = p
        count += 1
    print('Term', term, 'equals to:', p)
    x = 0
    for i in range(20):
        a = (random.randint(1, 2000))  #random number from 1 to 2.000, you can change the range
        #print(a)

        #if ((a ** p)-a) % p == 0:
        if (a**p) % p == a%p:
            x += 1
    #print(x)
    if x == 20:
        print('Your p:', p, ',', 'is prime!')
    else:
        print('Your p:', p, ',', 'is not prime!')
