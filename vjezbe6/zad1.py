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
R1= sredina(_2R1)/2
R2= sredina(_2R2)/2
R3= sredina(_2R3)/2
devR1= devijacija(_2R1)/2
devR2= devijacija(_2R2)/2
devR3= devijacija(_2R3)/2

print('Prosječni Radijusi:', R1, R2, R3)
print('Prosječne devijacije za radijuse:', devR1, devR2, devR3)

#duljine
l_1= sredina(L1)
l_2= sredina(L2)
l_3= sredina(L3)
devl1= devijacija(L1)
devl2= devijacija(L2)
devl3= devijacija(L3)

print('prosječne duljine:', l_1, l_2, l_3)
print('Prosječne devijacije za duljine:', devl1, devl2, devl3)

#mase 
m_1= sredina(m1)
m_2= sredina(m2)
m_3= sredina(m3)
devm1= devijacija(m1)
devm2= devijacija(m2)
devm3= devijacija(m3)

print('prosječne mase:', m_1, m_2, m_3)
print('Prosječne devijacije za mase:', devm1, devm2, devm3)




