#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    sparearray = []
    locationx = 1
    FIDIM = 0
    locationy = 1
    goodboypoints = 0
    chosenone = 0
    for i in range(15):
        if  FIDIM == 4 :
            locationx = 1
            locationy=locationy+1;
            FIDIM = 0
        locationxplus=locationx+1
        locationxminus=locationx-1

        locationyplus=locationy+1
        locationyminus=locationy-1
        FIDIM = FIDIM+1
        
        sum=arr[locationy][locationx]+arr[locationyplus][locationx]+arr[locationyminus][locationx]+arr[locationyminus][locationxminus]+arr[locationyminus][locationxplus]+arr[locationyplus][locationxplus]+arr[locationyplus][locationxminus]
        sparearray.append(sum)
        locationx=locationx+1
        
    print(sparearray)
    for i in range(15):
        goodboypoints = 0
        for i2 in range(15):
            if sparearray[i] >= sparearray[i2]:
                goodboypoints=goodboypoints+1
            if goodboypoints==15:
                print("triggered")
                chosenone = sparearray[i]
        print("Divider:"+str(chosenone))
           
    return(chosenone)
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
