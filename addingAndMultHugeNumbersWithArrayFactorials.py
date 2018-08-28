#https://www.hackerrank.com/challenges/extra-long-factorials/problem

This problem was too easy in python. To solve this all I had to do was
say math.factorial(n), but I didn't want to do that since my whole point
of doing this was to hopefully learn a new algorithm or trick. At first
I tried to use Stirling's approximation but somehow I'm not accurate enough
on that yet (not giving up yet) so I looked at the problem writer's solution.
It took me a bit to understand it, but I'm glad I tried because I learned
a neat new trick! And ironically kind of obvious, although I never thought
of it on my own. Basically, use an array as a digit placeholder instead
of relying on long integers. I still don't think my code is as sophisticated
as the creater of this problem but I'm glad I found the general idea. I still
want to get stirling to work though! The Stirling approximation is close but
not close enough...

def extraLongFactorials(n):
    x=n
    z=(math.log(x)-1)*x
    w=(1/2)*math.log(x)
    o=(1/2)*math.log(2*math.pi)
    m1=1/(12*x)
    m2=1/(360*x**3)
    m3=1/(1260*x**5)
    m4=1/(1680*x**7)
    m5=1/(1188*x**9)
    l=z+w+o+m1-m2+m3-m4+m5
    ans=math.e**l
    print(ans)


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    arr=[0]*200
    carry=0
    l=str(n)[::-1] #reversing to put into the array backwards
    sl=len(l)
    for i in range(sl):
        arr[i]=int(l[i])
    #print(arr)
    
    #addme=10000
    #carry=addme
    #for i in range(200): 
    #    t=(arr[i]+carry)%10
    #    t2=int((arr[i]+carry)/10)
    #    arr[i]=t
    #    carry=t2
    
    #multme=8
    #carry=0
    #for i in range(200):
    #    t=(arr[i]*multme+carry)%10
    #    t2=int((arr[i]*multme+carry)/10)
    #    arr[i]=t
    #    carry=t2
    #print(arr)
    
    for j in range(1,n):
        carry=0
        for i in range(200):
            t=(arr[i]*j+carry)%10
            t2=int((arr[i]*j+carry)/10)
            arr[i]=t
            carry=t2
    #print(arr)
    arr.reverse()
    #print(arr)
    x=''.join(map(str, arr))
    x=x.lstrip("0")
    print(x)
    

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
