import RPi.GPIO as GPIO
import time
import csv


#from ultrasonicsensor import ultrasonicread
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT)
servo=GPIO.PWM(2,50)
servo.start(0)

GPIO_Trigger = 18
GPIO_Echo = 24

GPIO.setup(GPIO_Trigger, GPIO.OUT)
GPIO.setup(GPIO_Echo, GPIO.IN)
def regression(dist):
    x=[]
    y=[]
    i=0
    Sx=0
    Sx2=0
    Sy=0
    Sxy=0
    minimum= min(dist)
    threshold= minimum*1.33
    columns= len(dist)
    
    for i in range(columns):
        if dist[i] < threshold:
            x.append(i)
            y.append(dist[i])
            Sx= Sx+i
            Sx2=Sx2+i*i
            Sy=Sy+dist[i]
            Sxy=Sxy+i*dist[i]
            
        i=i+1
    n=len(y)
    if n>1:
        A=((Sy*Sx2)-(Sx*Sxy))/((n*Sx2)-(Sx*Sx))
        B=((n*Sxy)-(Sx*Sy))/((n*Sx2)-(Sx*Sx))
        averagedist=sum(y)/len(y)
        angle=(averagedist-A)/B
    else:
        averagedist = y[0]
        angle = x[0]
      
    return(averagedist,angle)
        
def radar():
    GPIO.output(GPIO_Trigger, True)
    time.sleep(.0001)
    GPIO.output(GPIO_Trigger, False)
    StartTime = time.time()
    StopTime = time.time()
        
        
    while GPIO.input(GPIO_Echo) == 0:
        StartTime = time.time()
        
    while GPIO.input(GPIO_Echo) == 1:
        StopTime = time.time()
    TimeElasped = StopTime - StartTime
    distance = (TimeElasped * 34300)/2
    return distance
    
servo.ChangeDutyCycle(2)
time.sleep(1)

angles=[]
distances=[]
t0=time.time()
t=[]
try:
    while True:
        
        dist= []
        for angle in range(0,180):
            
            x= angle / 18 + 2
            servo.ChangeDutyCycle(x)
            time.sleep(.01)
            distance=radar()
            dist.append(distance)
            
        average,angle = regression(dist)
        t.append(time.time()-t0)
        distances.append(average)
        angles.append(angle)
        
        
        dist2=[]
        for angle in range(180,0,-1):
            
            x= angle / 18 + 2
            servo.ChangeDutyCycle(x)
            time.sleep(.01)
            distance=radar()
            dist2.append(distance)
            
            
        dist2.reverse()
        average,angle = regression(dist2)
        t.append(time.time()-t0)
        distances.append(average)
        angles.append(angle)
        
except KeyboardInterrupt:
    with open('some.csv','r+') as csvfile:
        
        writer = csv.writer(csvfile)
        writer.writerow(t)
        writer.writerow(distances)
        writer.writerow(angles)