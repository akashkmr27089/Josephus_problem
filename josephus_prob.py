#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 13:12:30 2018

@author: oxygen
"""

import numpy as np
dot = 0
echo = np.zeros((1,1))
def position(a, start = 0):
    if(a.__len__() == 1):
        global dot
        #return a[0]
        #print(a[0])
        dot = a[0]
    
    elif(start == 0):
        temp = a.__len__()
        print(a)
        for i in reversed(range(1,a.__len__(),2)):
            del a[a.index(a[i])]
        print(a,i)
        temp2 = a.__len__()
        print(temp, temp2)
        if((temp%2 != 0 and temp2%2 != 0) or (temp%2 != 0 and temp2%2 == 0)):
            position(a, start = 1)
        else:
            position(a, start = 0)
            
    elif(start == 1):   #starting from end
        a.insert(0,a[-1])
        del a[-1]
        temp = a.__len__()
        print(a)
        for i in reversed(range(1,a.__len__(),2)):
            del a[a.index(a[i])]
        print(a,i)
        temp2 = a.__len__()
        print(temp, temp2)
        if((temp%2 != 0 and temp2%2 != 0) or (temp%2 != 0 and temp2%2 == 0)):
            position(a, start = 1)
        else:
            position(a, start = 0)
            
def listing(n):
    global echo
    echo = np.zeros((2,n))
    for i in range(1,n):
        echo[0,i] = i
        data = [x for x in range(i)]
        position(data)
        echo[1,i] = dot+1
        
 
def main():
    a = int(input("Enter the Number :"))
    data = [x for x in range(1,a+1)]
   # print(data)
    x = position(data)
    print(dot)
    
if __name__ == '__main__':
    main()