import numpy as np
import math
# 5 mjerenja temperature vrenja vode [u stupnjevima Celzijusa]
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]
# 10000 mjerenja istog eksperimenta (simulacija)
np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()


def sigma (n):      #Standardna devijacija populacije
    sr=sum(n)/len(n)
    zb=0
    for i in n:
        zb+=(i-sr)**2
    s=math.sqrt(zb/len(n))
    return s

def s(n):       #Standardna devijacija uzorka
    sr=sum(n)/len(n)
    zb=0
    for i in n:
        zb+=(i-sr)**2
    s=math.sqrt(zb/(len(n)+1))
    return s

def sigmax(n):      #Standardna pogreška aritmetičke sredine (SEM)
    sr=sum(n)/len(n)
    zb=0
    for i in n:
        zb+=(i-sr)**2
    s=math.sqrt(zb/(len(n)+1))
    x=s/math.sqrt(len(n))
    return x

sigma_malo=sigma(malo_n)
sigma_veliko= sigma(veliko_n)
s_malo= s(malo_n)
s_veliko= s(veliko_n)
sigmax_malo= sigmax(malo_n)
sigmax_veliko= sigmax(veliko_n)

print('sigma malo=', sigma_malo)
print('sigma veliko=', sigma_veliko)
print('s malo=', s_malo)
print('s_veliko=', s_veliko)
print('sigmax_malo=', sigmax_malo)
print('sigmax_veliko=', sigmax_veliko)

print('a) Povecanjem broja mjerenja s ostaje priblizno isti, dok se sigmax smanjuje (veci broj mjerenja daje tocniji rezultat)')
print('b) Veca je razlika za manji skup. Za veci je priblizno jednaka')
print('c) np.std() koristimo za sigma jer dijeli sa korijen iz n')


