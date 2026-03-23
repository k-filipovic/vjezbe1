import math

def graf(v0, k):
    def pogreska(v0, k, dt):
        def analitickiD(v0, k):
            d=((v0**2)*math.sin(2*math.radians(k)))/9.81
            return d

        def numerickiD(v0, k, dt):
            vx=v0*math.cos(math.radians(k))
            vy=v0*math.sin(math.radians(k))
            x=0
            y=0
            xl=[x]
            yl=[y]
            while y>0:
                x+=vx*dt
                y+=vy*dt
                vy=vy-9.81*dt
            return x
        p=(math.fabs(numerickiD(v0, k, dt)-analitickiD(v0, k))/(analitickiD(v0, k)))*100
        return p 

    import matplotlib.pyplot as plt
    import numpy as np
    
    t= [i * 0.001 for i in range(1, 101)]
    pogreske=[]
    for i in t:
        p=pogreska(v0, k, i)
        pogreske.append(p)
   
    plt.xlabel('dt')
    plt.ylabel('pogreška u %')
    plt.plot(t, pogreske)
    plt.show()
    
v0=10
k=60
graf(v0, k)
