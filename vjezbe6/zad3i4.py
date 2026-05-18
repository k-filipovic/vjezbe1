import math

def gustoca_valjka(R, L, m):
    G= (m) / (L*math.pi*R**2)
    return G

def sigma_gustoce(R, sigma_R, L, sigma_L, m, sigma_m):
    #izracunate parcijalne derivacije za gustocu po varijablama 
    parcR= (( (-2*m)/(math.pi*L*(R**3)) )*(sigma_R))**2   
    parcL= ( (-m/(math.pi*(L**2)*(R**2))) *(sigma_L))**2
    parcm= 1/(math.pi*(L)*(R**2))
    s=math.sqrt(parcL+parcR+parcm)
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

m1= [138.92, 138.98, 139.20, 138.90, 138.92]
m2= [128.65, 128.60, 128.65, 128.35, 128.50]
m3= [71.89, 71.90, 71.79, 71.85, 71.70]

#radijusi
R1= sredina(_2R1)/20
R2= sredina(_2R2)/20
R3= sredina(_2R3)/20
devR1= devijacija(_2R1)/20
devR2= devijacija(_2R2)/20
devR3= devijacija(_2R3)/20

#duljine
l_1= sredina(L1)/10
l_2= sredina(L2)/10
l_3= sredina(L3)/10
devl1= devijacija(L1)/10
devl2= devijacija(L2)/10
devl3= devijacija(L3)/10

#mase 
m_1= sredina(m1)
m_2= sredina(m2)
m_3= sredina(m3)
devm1= devijacija(m1)
devm2= devijacija(m2)
devm3= devijacija(m3)

G1=gustoca_valjka(R1, l_1, m_1)
G2=gustoca_valjka(R2, l_2, m_2)
G3=gustoca_valjka(R3, l_3, m_3)

print('G1=', G1)
print('G2=', G2)
print('G3=', G3)

print('Devijacija1=', sigma_gustoce(R1, devR1, l_1, devl1, m_1, devm1))
print('Devijacija2=', sigma_gustoce(R2, devR2, l_2, devl2, m_2, devm2))
print('Devijacija3=', sigma_gustoce(R3, devR3, l_3, devl3, m_3, devm3))

Bakar= 8.96         #moze biti i nikal
Zeljezo=7.87        #moze biti i celik
Kvarc=2.65 

P1= (abs(Bakar-G1)/Bakar)*100
P2= (abs(Zeljezo-G2)/Zeljezo)*100
P3= (abs(Kvarc-G3)/Kvarc)*100

print('Relativna pogreska u usporedbi s literaturom u %:')
print(P1)
print(P2)
print(P3)