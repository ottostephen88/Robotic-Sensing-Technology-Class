import time

def PID(error,previousError,Kp,Ki,Kd,t1,Int):

    t2=time.time()
    dt=t2-t1

    Int=(Ki*Int)+(error*dt)
    Deriv=(error-previousError)/dt

    
    u=Kp*error+Ki*Int+Kd*Deriv
    

    t1=time.time()
    previousError= error
    return t1, previousError, u, Int

def system(u,Mass,NatFreq,DampRatio,Int1,Int2,Sum2):
    Sum1= (u/Mass)-Sum2
    Freq=NatFreq*2*3.14
    Sum2=((Freq)*(2)*(DampRatio)*Int1)+((Freq*Freq)*Int2)
    k=(Freq*Freq)*Mass
    staticResponse= u/k
    
    Int1= Sum1*dt
    Int2= Int1*dt
    return Int1, Int2, k, staticResponse, Sum2
"N"
Force = 5
output = 0

previousError = 0
"seconds"
t1=0

Setpoint = 0

"kg"
Mass = 2
"Hz"
Freq= 2
DampRatio=.001
Int = 0
Int1=0
Int2 = 0
Sum2 = 0
while True:
    input = Force - Int2
    error= input-Setpoint
    t1 , previousError, u, Int = PID(error,previousError,200,.2,.2,t1,Int)
    Int1, Int2, k, staticResponse,Sum2 = system(u,Mass,Freq,DampRatio,Int1,Int2,Sum2)
    
