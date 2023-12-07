import matplotlib.pyplot as p
import numpy as np
def quadratic(time,a,b,c):
  temp=a*time**2+b*time+c
  return temp

a=-0.1
b=1
c=0.1
time=np.linspace(0,10,100)
p.plot(time,quadratic(time,a,b,c))
p.xlabel("TEMPERATURE")
p.ylabel("TIME")
p.title("Weather Model")
p.show()
