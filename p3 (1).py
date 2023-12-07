import matplotlib.pyplot as p
import numpy as np
def quadratic(time,a,b,c):
  temp=a*time**2+b*time+c
  return temp
n=int(input("Enter no of sets"))
for i in range(n):
  print("enter",i+1,"set value")
  a=float(input("Enter a value: "))
  b=float(input("Enter b value: "))
  c=float(input("Enter c value: "))
  time=np.arange(0,50,1)
  p.plot(time,quadratic(time,a,b,c))
p.xlabel("TEMPERATURE")
p.ylabel("TIME")
p.show()
