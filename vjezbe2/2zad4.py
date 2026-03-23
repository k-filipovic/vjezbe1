import math
import calculus as c
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2*x**2+3

print('gornja i donja integralna suma su: ', c.pravokutna(f, 0, 1, 100))
print('integral pomoću trapeza ', c.trapezna(f, 0, 1, 100))

n=np.arange(50, 501, 20)
x=np.linspace(50, 501, 200)
y=np.linspace(11/3, 11/3, 200)
n=n.tolist()
trapezni=[]
pgornji=[]
pdonji=[]
for i in n:
    k=c.trapezna(f, 0, 1, i)
    trapezni.append(k)
for j in n:
    u=c.pravokutna(f, 0, 1, j)
    pgornji.append(u[0])
    pdonji.append(u[1])

plt.title('Derivacija funkcije x^3')
plt.legend()
plt.xlabel('n')
plt.ylabel('Integral')
plt.plot(x, y)
plt.scatter(n, trapezni, s=5)
plt.scatter(n, pgornji, s=5)
plt.scatter(n, pdonji, s=5)
plt.show()
