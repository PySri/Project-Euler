#!/usr/bin/env python

##############
#
# Highly divisible triangular number
#
##############

def factors(n,i):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
    s = 0 
    i = 1
    flag = True

    while flag:
       s = sum(range(i+1))
       se = factors(s,i)
       if len(se) >= 500:
          #print s, " : factors---> ", se, "length is ", len(se)
          print "value of the first triangle number to have over five hundred divisors is: ", s
          flag = False

       i += 1

if __name__ == '__main__':
    main()

