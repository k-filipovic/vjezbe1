
class Field:
    import numpy as np
    def __init__(self, m, q, v, E, B):
        self.m=m
        self.q=q
        self.vx, self.vy, self.vz = v[0], v[1], v[2]
        self.Ex, self.Ey, self.Ez = E[0], E[1], E[2]
        self.Bx, self.By, self.Bz = B[0], B[1], B[2]
        self.x, self.y, self.z= 0,0,0           #proizvoljni pocetni polozaj
        self.x_lista=[]
        self.y_lista=[]
        self.z_lista=[]

    def __move(self, dt):

        ax = (self.q / self.m) * (self.Ex + self.vy * self.Bz - self.vz * self.By)  #vektorsko mnozenje v i B (sila magn polja je q*vxB)
        ay = (self.q / self.m) * (self.Ey + self.vz * self.Bx - self.vx * self.Bz)
        az = (self.q / self.m) * (self.Ez + self.vx * self.By - self.vy * self.Bx)

        self.vx += ax*dt      #Euler
        self.vy += ay*dt
        self.vz += az*dt

        self.x += self.vx*dt
        self.y += self.vy*dt
        self.z += self.vz*dt

        self.x_lista.append(self.x)
        self.y_lista.append(self.y)
        self.z_lista.append(self.z)
    
    def graf(self):
        t=0
        t_kon=15
        dt=0.001
        while t<=t_kon:
            self.__move(dt)
            t+= dt

        import matplotlib.pyplot as plt
        fig = plt.figure()
        plt.axes(projection='3d')           #za 3D
        plt.plot(self.x_lista, self.y_lista, self.z_lista, label="Gibanje")
        plt.xlabel('X [m]')
        plt.ylabel('Y [m]')
        plt.gca().set_zlabel('Z [m]') 
        plt.legend()
        plt.show()

