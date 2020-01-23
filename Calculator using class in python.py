# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:36:35 2020

@author: Hp
"""

class Mathmatics:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Plus(self):
        Add = self.x + self.y
        print(Add)
    def Minus(self):
        Sub = self.x - self.y
        print(Sub)
    def Multiply(self):
        mul = self.x *self.y
        print(mul)
    def Divide(self):
        Div = self.x / self.y
        print(Div)
print("Type 1 for Add")
print("Type 2 for Sub")
print("Type 3 for Mul")
print("Type 4 for Div")        
i = 1      
while i != 0:   
    choose = (int(input("Choose the number 1/2/3/4 :::: ")))     
    if choose<=4 and choose >= 1:
        p1 = Mathmatics((int(input("Enter the First Number : "))),(int(input("Enter the Second Number : "))))    
        if choose == 1:
            p1.Plus()
        elif choose == 2:
            p1.Minus()
        elif choose == 3:
            p1.Multiply()
        elif choose == 4:
            p1.Divide()
    else:
        print("Invalid Number")