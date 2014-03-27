#! /usr/bin/env python

###########
#
# Multiples of 3 and 5
# 
############

def main():
    sum = 0
    for i in range(1,1000):
        if i%3 == 0 or i%5 == 0:
           sum += i

    print "Sum all of all multiples of 3 or 5 below 1000 is: ", sum


if __name__ == '__main__':
   main()

