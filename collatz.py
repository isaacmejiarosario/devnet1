#!/usr/bin/env python

import time
import sys



def collatz(number):

    if number % 2 == 0:            
        r = number // 2
        print (r)
        return r

    elif number % 2 == 1:
        r = 3 * number + 1
        print(r)
        return r

def program(): 
    try:
        num = int(input("Please enter your number:"))

        while num != 1:
            num = collatz(int(num))
        if num == 1:
            print ("Your are done!!")
    except ValueError:
        print('Value Error. Please enter integer.')
        program()


program()
