import math
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
time = []
xs = []
ys = []
x = []
y = []
z = []
vx = []
vy = []
vz = []
Q = []
h_max = float
v = float
deg = float
dt = float
w = 30
g = 9.8
m = 5.5
C = 4 * math.pow(10,-5)
h = float
f_lateral = []
air_res = float
t_zero = float
t_zero_final =float
h_max = float

def setup():
    global dt,h,t_zero
    print("current air temperature ground zero:")
    t_zero = float(input())
    print("initial speed:")
    v = float(input())
    print("degree of the shot:")
    deg = float(input())
    if deg>90:
        print("Degree value of the shot must be between 90-0")
        sys.exit()
    deg_rad = math.radians(deg)
    print("time interval:")
    dt = float(input())
    print("Hight of shot:")
    h = float(input())
    y.insert(0,h)
    x.insert(0,0.0)
    time.insert(0,0.0)
    vz.insert(0,0.0)
    Q.insert(0,0.0)
    max_deg = math.radians(90)
    vy.insert(0,float(math.sin(deg_rad))*v)
    vx.insert(0,float(math.sin(max_deg-deg_rad))*v)
    return()

def drag(v_cal,y,v_cal2):
    global C,t_zero,t_zero_final
    v = math.sqrt(math.pow(v_cal,2)+math.pow(v_cal2,2))
    a = 6.5*math.pow(10,-3)
    alpha = 2.5
    t_zero_final = float(t_zero)+273
    air_res = C*float(v)*abs(float(v_cal))
    f_air1 = math.pow((1-(a*y/t_zero_final)),5)
    f_air = math.sqrt(f_air1)*air_res
    return(f_air)


def calculate():
    global h_max,x,y
    i=0
    while True:
        if(y[i]<0):
            y[i] = 0
            break
        time.insert(i+1,float(time[i])+dt)
        x.insert(i+1,float(x[i])+float(vx[i])*dt)
        y.insert(i+1,float(y[i])+(float(vy[i])*dt))
        vx.insert(i+1,float(vx[i])-(drag(vx[i],y[i+1],vy[i])*dt))
        vy.insert(i+1,float(vy[i])-(dt*g)-(drag(vy[i],y[i+1],vx[i])*dt))
        vz.insert(i+1,float(vz[i])-(C*float(vx[i])*w))
        Q.insert(i+1,float(Q[i])+dt*w)


        if (y[i+1]>y[i]):
            h_max = y[i+1]
        i = i+1
    return(Q)

def lateral():
    global g,m
    for i in Q:
        f_lateral.append((m*g)/2*(math.sin(4*i)-(math.sin(8*i)/4)+(math.sin(12*i)*0.08)-(0.025*math.sin(16*i))))
    return()


def graph():
    plt.ylabel('Height')
    plt.xlabel('Range')
    plt.title('Trajactory')
    plt.plot(x,y)
    plt.show()

setup()
calculate()
#lateral()
graph()
