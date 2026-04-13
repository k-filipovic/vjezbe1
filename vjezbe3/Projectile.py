import math
import numpy as np

class Projectile:
    def __init__(self, v, k, m, x, y, rho=1.225, c=0.5, r=0.06):
        A=(r**2)*math.pi
        b=0.5*rho*c*A
        self.b=b              #koef. otpora zraka
        self.v=v
        self.k=math.radians(k)
        self.m=m
        self.v0=v
        self.x0 = x
        self.y0 = y
        self.x=x
        self.y=y
        self.x_eul = [self.x]   #pravim listu u koju ce se poslije spremati x
        self.y_eul = [self.y]
        self.x_r4= [self.x]
        self.y_r4= [self.y]
        self.vx=v*math.cos(self.k)
        self.vy=v*math.sin(self.k)

    def __Euler(self, dt): 
        g=9.81
        v=math.sqrt(self.vx**2 + self.vy**2)      #ukupna brzina, Pitagora
        self.ax= -self.b*self.vx*v/self.m
        self.ay=-g-(self.b/self.m)*v*self.vy    #akcel. prema kvadratnom otporu

        self.vx=self.vx + self.ax*dt
        self.vy=self.vy + self.ay*dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.x_eul.append(self.x)
        self.y_eul.append(self.y)

    def __R4(self, dt):
        g=9.81
        #k1
        v1=np.sqrt(self.vx**2+self.vy**2)
        ax1=-(self.b/self.m)*v1*self.vx
        ay1=-g-(self.b/self.m)*v1*self.vy

        #k2
        vx2=self.vx+ax1*dt/2
        vy2=self.vy+ay1*dt/2
        v2=np.sqrt(vx2**2+vy2**2)
        ax2=-(self.b/self.m)*v2*vx2
        ay2=-g-(self.b/self.m)*v2*vy2

        #k3
        vx3=self.vx+ax2*dt/2
        vy3=self.vy+ay2*dt/2
        v3=np.sqrt(vx3**2+vy3**2)
        ax3=-(self.b/self.m)*v3*vx3
        ay3=-g-(self.b/self.m)*v3*vy3
    
        #k4
        vx4=self.vx+ax3*dt
        vy4=self.vy+ay3*dt
        v4=np.sqrt(vx4**2+vy4**2)
        ax4=-(self.b/self.m)*v4*vx4
        ay4=-g-(self.b/self.m)*v4*vy4

        #polozaj prema r4
        self.x=self.x+(dt/6)*(self.vx+2*vx2+2*vx3+vx4)
        self.y=self.y+(dt/6)*(self.vy+2*vy2+2*vy3+vy4)
    
        #brzina prema r4
        self.vx=self.vx+(dt/6)*(ax1+2*ax2+2*ax3+ax4)
        self.vy=self.vy+(dt/6)*(ay1+2*ay2+2*ay3+ay4)

        self.x_r4.append(self.x)
        self.y_r4.append(self.y)

    
    def graf(self):
        dt=0.01
        while self.y >= 0:      #pomičemo česticu sve dok ne padne na tlo za neki dt
            self.__Euler(dt)

        self.x = self.x0        #moramo resetirati vrijednosti na pocetne jer su se u meduvremenu promijenile
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.k)
        self.vy = self.v0 * math.sin(self.k)

        while self.y >= 0:  #isto radimo i za r4 metodu
            self.__R4(dt)
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10,6))
        plt.xlabel('x/m')
        plt.ylabel('y/m')
        plt.title('Gibanje čestice sa otporom zraka')
        plt.plot(self.x_eul,self.y_eul,label='Eulerova metoda',linestyle='--',color='red')
        plt.plot(self.x_r4,self.y_r4,label='Runge-Kutta (R4)',linewidth=2,color='blue')
        plt.legend()
        return plt.show()
