import matplotlib.pyplot as p
import numpy as np
def quadratic(time,a,b,c):
  temp=a*time**2+b*time+c
  return temp
a1=0.01
b1=-0.3
c1=40
time=np.arange(0,50,1)
p.plot(time,quadratic(time,a1,b1,c1),label='hard code')
a=float(input("Enter a value: "))
b=float(input("Enter b value: "))
c=float(input("Enter c value: "))

p.plot(time,quadratic(time,a,b,c),label='user input')
p.xlabel("TEMPERATURE")
p.ylabel("TIME")
p.show()
