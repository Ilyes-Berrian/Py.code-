import random


class Dice:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def roll(self):
        x=random.randint(self.a,self.b)
        y=random.randint(self.a,self.b)
        
        cordonate=(x,y)
        print(cordonate)