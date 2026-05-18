import math

def volumen_valjka(R, L):
    V=((R/10)**2)*(L/10)*math.pi
    return V

def sigma_volumena(R, sigma_R, L, sigma_L):
    parcR= ((L/10)*2*(R/10)*math.pi*(sigma_R/10))**2
    parcL= (((R/10)**2)*math.pi*(sigma_L/10))**2
    s=math.sqrt(parcL+parcR)
    return s


#dio prvog zadatka
from arithm import sredina
from arithm import devijacija

#liste
_2R1= [19.98, 20.18, 20.10, 20.08, 19.74]
_2R2= [19.92, 19.82, 19.96, 19.98, 19.88]
_2R3= [24.96, 24.98, 24.98, 24.92, 24.94]

L1= [49.80, 49.00, 50.48, 49.80, 49.96]
L2= [52.56, 52.50, 52.62, 52.58, 52.54]
L3= [55.34, 55.40, 55.30, 55.44, 55.48]

#radijusi
R1= sredina(_2R1)/2
R2= sredina(_2R2)/2
R3= sredina(_2R3)/2
devR1= devijacija(_2R1)/2
devR2= devijacija(_2R2)/2
devR3= devijacija(_2R3)/2

#duljine
l_1= sredina(L1)
l_2= sredina(L2)
l_3= sredina(L3)
devl1= devijacija(L1)
devl2= devijacija(L2)
devl3= devijacija(L3)

print('V1=', volumen_valjka(R1, l_1))
print('V2=', volumen_valjka(R2, l_2))
print('V3=', volumen_valjka(R3, l_3))

print('Devijacija1=', sigma_volumena(R1, devR1, l_1, devl1))
print('Devijacija2=', sigma_volumena(R2, devR2, l_2, devl2))
print('Devijacija3=', sigma_volumena(R3, devR3, l_3, devl3))
