import math
import array as arranastran

#area function
def tri_area(p1,p2,p3,q1,q2,q3,r1,r2,r3):
  A=(q1-p1)**2 + (q2-p2)**2 + (q3-p3)**2
  B=(q1-r1)**2 + (q2-r2)**2 + (q3-r3)**2
  C=(p1-r1)**2 + (p2-r2)**2 + (p3-r3)**2
  area=math.sqrt((4*A*B-(C-A-B)**2)/16)
  return area;

#array in decimal form
gridx= arranastran.array('d')
gridy= arranastran.array('d')
gridz= arranastran.array('d')

counter=0
numberid = 0
counter2=0
i=0
j=0
totalarea=0

#needed because some numbers for grid are skipped in document
while j < 10:
    gridx.append(0)
    gridy.append(0)
    gridz.append(0)
    j=j+1
    
with open('Bar2-000.dat') as reader:
    line=reader.readline()
    while line !='':

        line=reader.readline()
        if (line[0:5]=='GRID '):
            numberid=int(line[8:16])
            
            xcoord=float(line[24:32])
            ycoord=float(line[32:40])
            zcoord=float(line[41:48])
            gridx.insert(numberid,xcoord)
            gridy.insert(numberid,ycoord)
            gridz.insert(numberid,zcoord)
            #print(line[0:4],numberid+1,gridx[i],gridy[i],gridz[i])
            counter=counter+1
            i= i+1
        elif (line[0:6]=='CQUAD4'):
            numberidC=int(line[8:16])
            
            node1=int(line[24:32])
            n1x=gridx[node1]
            n1y=gridy[node1]
            n1z=gridz[node1]
            
            node2=int(line[32:40])
            n2x=gridx[node2]
            n2y=gridy[node2]
            n2z=gridz[node2]
            
            node3=int(line[40:48])
            n3x=gridx[node3]
            n3y=gridy[node3]
            n3z=gridz[node3]
            
            node4=int(line[48:56])
            n4x=gridx[node4]
            n4y=gridy[node4]
            n4z=gridz[node4]

            a1 = tri_area(n1x,n1y,n1z,n2x,n2y,n2z,n3x,n3y,n3z)
            a2 = tri_area(n1x,n1y,n1z,n3x,n3y,n3z,n4x,n4y,n4z)
            area=a1+a2
            totalarea=area+totalarea
            counter2=counter2+1
                
    print('The number of grids read ',counter)
    print('The number of elements read',counter2)
    print('Total area is',totalarea)

            
        
