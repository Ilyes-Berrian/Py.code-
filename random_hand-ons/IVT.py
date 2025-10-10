import math, random


#f(x)=....
#Df=[a,b]
#proof f(c)=0,c from [a,b] using IVT
#IVT: if f(x) is con. and monotone on [a,b] such that: f(a)*f(b)<0, then by IVT there is unique root c
#from [a,b] where f(c)=0  using Bisection method 
#a=0,b=3
#a=0,b=1.5

import math
from scipy.optimize import brentq

# Function
def f(x):
    return x**2 - 4

# Root in [1,2]
root = brentq(f, 0, 10)

print("Root:", root)
print("Check f(root):", round(f(root),10))

