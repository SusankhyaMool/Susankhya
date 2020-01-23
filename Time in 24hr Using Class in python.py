# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:42:12 2020

@author: Susankhya Mool

"""
class time:
    def __init__(self,hr,minu,sec,day):
        self.hr = hr
        self.minu = minu
        self.sec = sec
        self.day = day
        
    def watch(self):
        print("Your time is  : "+self.hr + ":" + self.minu + ":" + self.sec + ":" + self.day)
        
    def hour(self):
        if int(self.hr) == 12 and self.day == "PM":
            print("Time in 24hr : " + str(self.hr)+ ":" + self.minu + ":" + self.sec)
        elif int(self.hr) < 12 and self.day == "PM":
            a = int(self.hr) + 12
            print("Time in 24hr : " + str(a) + ":" + self.minu + ":" + self.sec)
        elif int(self.hr) == 12 and self.day == "AM":
            print("Time in 24hr : " "00" + ":" + self.minu + ":" + self.sec)
        elif int(self.hr) < 12 and self.day == "AM":
            print("Time in 24hr : " + str(self.hr)+ ":" + self.minu + ":" + self.sec)
        
        else:
            print("Invalid Number : ")
        
            
            
t1 = time((input("Enter the hr : ")),(input("Enter the min : ")),(input("Enter the sec : ")),(input("Enter the Day : ").upper()))
t1.watch()
t1.hour()
