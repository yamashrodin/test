import math
import numpy as np
import time
from numpy.random import *
import random
import sys

y='a'
count=0
def calmc(month,year):

    if year%4==0:
        if month == 1:
            mc=5 #if it's a leap year, 5
        elif month == 2:
            mc=1   #if it's a leap year, 1 you may have to edit to realize this  
        elif month == 3:
            mc=2
        elif month == 4:
            mc=5
        elif month == 5:
            mc=0
        elif month == 6:
            mc=3
        elif month == 7:
            mc=5
        elif month == 8:
            mc=1
        elif month == 9:
            mc=4
        elif month == 10:
            mc=6
        elif month == 11:
            mc=2
        elif month == 12:
            mc=4
    else: 
        if month == 1:
            mc=6 #if it's a leap year, 5
        elif month == 2:
            mc=2   #if it's a leap year, 1 you may have to edit to realize this  
        elif month == 3:
            mc=2
        elif month == 4:
            mc=5
        elif month == 5:
            mc=0
        elif month == 6:
            mc=3
        elif month == 7:
            mc=5
        elif month == 8:
            mc=1
        elif month == 9:
            mc=4
        elif month == 10:
            mc=6
        elif month == 11:
            mc=2
        elif month == 12:
            mc=4

    return mc



while y!='f':
    year=1980+40*np.random.rand()
    year=int(year)
    month=int(round(1+11*np.random.rand(),0))
    day=1+int(27*np.random.rand())

    print(year,month,day)
    if 2000 <= year:
        yshift=year-2000
        yc=0+yshift+math.floor(yshift/4)
    elif  1900<=year:
        yshift=year-1900
        yc=1+yshift+math.floor(yshift/4)
    else:
        print("       I don't know")
        sys.exit()
    #yc=yc%7
    
    mc=calmc(month,year)
    #print(mc,yc)
    dow=(yc+mc+day)%7
    
    q=input()    
    if dow==1:
        print("                That's monday")
    if dow==2:                 
        print("                That's tuesday")
    if dow==3:                 
        print("                That's wednesday")
    if dow==4:
        print("                That's thursday")
    if dow==5:                 
        print("                That's friday")
    if dow==6:                 
        print("                That's saturday")
    if dow==0:                 
        print("                That's sunday")
    count+=1
    y=input()

print("\n      ************************************************")
print("      ************************************************")
print("      **            Goooood job!!!!!!!!!!           **")
print("      ************************************************")
print("      ************************************************")
print("      you did "+str(count)+" times.")










