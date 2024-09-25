#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:49:41 2024

@author: asgunzi
"""
import math

def isPrime(N):
    if N ==2:
        return(True)
    elif N % 2 ==0:
        return(False)
    else:
        nMax = math.ceil(math.sqrt(N))
        status = True
        for i in range(3, nMax+1, 2):
            if N % i == 0:  
                status = False
                break
        
        return(status)
            
    

def procuraNum():    
    for a in range(2, 100):
        for b in range(a+1,100):
            num = a**2 + b**3
            
            if isPrime(num):
                print(num, a, b)
                return(True)
        

procuraNum()
            
        
        