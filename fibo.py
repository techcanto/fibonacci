#!/usr/bin/env python3

#By antonioclash819@gmail.com
#GNU/GPL License
#My first secuence

# Fibonacci sequence
# a b c
#   a  b  c
#1, 2, 3, 5, 8, 13, ...
#1/1, 1/2, 2/3, 3/5, 5/8 ..... 1+sqrt(5)/2.0
#c = a + b
import math as m
import matplotlib.pyplot as plt
suma = 1+2+3+4+5+6+7+8+9+10
a = 1
b = 1

fibo = []
N = 100
c = a + b
print(a)
print(b)
fibo.append(a)
fibo.append(b)


for x in range(N + 1):
    c = a + b
    # print(c)
    fibo.append(c)
    a = b
    b = c
print(fibo)

    
for i in range(len( fibo)-1):
    print(fibo[i+1]/fibo[i])

    
gold_ratio = (fibo[len(fibo)-1]/fibo[len(fibo)-2])
print(gold_ratio)

x = [0,1, 1, 0,0]
y = [0,0, gold_ratio,gold_ratio,0]
plt.plot(x,y)
plt.gca().set_aspect("equal")
plt.show()

#print((1.0 + m.sqrt(5)) /2.0)


