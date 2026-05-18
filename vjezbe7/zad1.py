import numpy as np
np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02] # pogreske pri redukciji podataka


def histogram(podaci, k):
    x_min=min(podaci)
    x_max=max(podaci)
    h=(x_max-x_min)/k
    rubovi = []
    for i in range(k + 1):
        rub= x_min + i*h
        rubovi.append(rub)

    k={         #stvaram dictionary

        } 
    
    for i in range(len(rubovi)):
        for j in podaci:
            if j>=rubovi[i] and j<rubovi[i+1]:
                kljuc=str(rubovi[i])+' - '+ str(rubovi[i+1])
                vrijednost=j
                k[kljuc]=vrijednost
    print(k)
        

histogram(mase_ciste, 10)


    
