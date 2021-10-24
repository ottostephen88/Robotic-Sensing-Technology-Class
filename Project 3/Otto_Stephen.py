# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:52:50 2021

-the function returns a list with dots,dashes,and spaces
-finding the character in the document hasn't been changed
-uses the list and reads the first lines to find if its a dash,
dot, or space and change the light accordingly with timing done
in a while loop with ifs and elseif

@author: Stephen Otto
011796499
"""
import csv
import time
import RPi.GPIO as GPIO


string='SOS SOS SOS'
string=string.upper()
elements=len(string)


# Pin definitions
led_pin_red = 12
led_pin_green = 13
led_pin_blue = 16
led = 6

# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)
GPIO.setup(led_pin_blue, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

def decoding(testchar,codes):
    sentence=[]
    for j in range(elements):
        index = 0
        i=0
        rdchar = ''
        if testchar[j]== ' ':
            sentence.append(' ')
            continue
        while(testchar[j] != rdchar):
            rdchar=codes[i][0]
            if(rdchar == testchar[j] and i<numcodes):
                index = i
                chcode= codes[i][1]
            i =i+1
        #print(' for character = ', rdchar, ' code = ',chcode)

        numdotdash = int(chcode/256)
        #print('Nuber of dots and dashes = ', numdotdash)

        send = ''
        for i in range(numdotdash):
            digit = 2**i
            if(digit & chcode == digit):
                output = 'dash'
            else:
                output = 'dot'
            send = send + output
        #print(testchar, '   ',send)
        sentence.append(send)
        j=j+1
    return(sentence)
    '''
reading from file was not changed
'''
dotdash = [0, 0, 0, 0 ,0 ,0]
filein = open('morse.txt', 'r') 
f = csv.reader(filein,dialect='excel',delimiter='\t')

numcodes = 0
for row in f:
    #print('row = ',row)
    ch = row[0]
    val = int(row[1])
    #print('ch = ',ch)
    #print('val = ',val)
    if numcodes == 0:
        codes = [[ch, val]]
    else:
        codes.append([ch, val])   
    numcodes= numcodes + 1     
#print(codes)   
#print('Number of rows read =', numcodes)



output=decoding(string,codes)
print(output)
i=0
j=0
index=0
#elements=[]
length = len(output)
#for i in range(length):
    #elements.append(output[i].count('dot')+output[i].count('dash'))
    
i=0
k=0
output2=[]
for i in output:
    output2.append(output[k]+' ')
    k=k+1
    
'''added to the end of array so i could
look one index ahead to see if a space was
coming
'''
output2.append('end')
#print(output2)


result=0
result2=0
k=0
'''
for loop to read lines from outputed list
'''
for i in output:
    letter=output2[k]
    letter2=output2[k+1]
    while j<100:
        
        if letter[j:j+3] == 'dot':
            
            #red
            #GPIO.output(led_pin_red, GPIO.HIGH)
            GPIO.output(led, GPIO.HIGH) 
            time.sleep(.05)
            #GPIO.output(led_pin_red, GPIO.LOW)
            GPIO.output(led, GPIO.LOW)
            print('dot')
            
            
            '''need this to determine if space is incoming to not
            add more time than neccessary '''
            if letter2[0] == ' ':
                if letter[j+3]!='d':
                    break
                else:
                    time.sleep(.5)
            else:
                time.sleep(.5)
                    
            j=j+3
            
        elif letter[j:j+3] == 'das':
              
            #green
            #GPIO.output(led_pin_green, GPIO.HIGH)
            GPIO.output(led, GPIO.HIGH) 
            time.sleep(.3)                   
            #GPIO.output(led_pin_green, GPIO.LOW)
            GPIO.output(led, GPIO.LOW) 
            print('dash')
            
            
            '''need this to determine if space is incoming to not
            add more time than neccessary '''
            if letter2[0] == ' ':
                if letter[j+4]!='d':
                    break
                else:
                    time.sleep(.5)
            else:
                time.sleep(.5)
              
                
            j=j+4
            
        elif letter[j:j+2] == '  ':
            
            #blue
            #GPIO.output(led_pin_blue, GPIO.HIGH) 
            time.sleep(1.5)                   
            #GPIO.output(led_pin_blue, GPIO.LOW)
            print('space')
            
            
            break
        
        
        else:
            time.sleep(.5)   
            j=101
            
            
    j=0
    k=k+1
             
    



    
