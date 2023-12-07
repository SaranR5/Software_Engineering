import matplotlib.pyplot as p
import numpy as np
def quadratic(time,a,b,c):
  temp=a*time**2+b*time+c
  return temp
f=open("file.txt",'r')
a1=f.read()
z=a1.split(",")
f.close()
a=float(z[0])
b=float(z[1])
c=float(z[2])
time=np.arange(0,50,1)
p.plot(time,quadratic(time,a,b,c))
p.xlabel("TEMPERATURE")
p.ylabel("TIME")
p.show()



