#! /usr/bin/env python

#########
#
# Smallest multiple
#
#########

def main():
    found = True

    number = 20
    
    while found:
       for i in range(2,21):
          if number % i != 0:
             divisible = False
             break
          else:
             divisible = True

       if divisible:
          found = False
       else: 
          number += 20 

    print "Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: ", number

if __name__ == '__main__':
    main()
