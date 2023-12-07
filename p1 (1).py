import matplotlib.pyplot as p
import numpy as np
def quadratic(time,a,b,c):
  temp=a*time**2+b*time+c
  return temp

a=float(input("Enter a value"))
b=float(input("Enter b value"))
c=float(input("Enter c value"))
time=np.linspace(0,10,100)
p.plot(time,quadratic(time,a,b,c))
p.xlabel("TEMPERATURE")
p.ylabel("TIME")
p.show()
