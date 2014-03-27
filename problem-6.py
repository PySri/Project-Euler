#! /usr/bin/env python

########
#
# Sum square difference
#
########

def main():
    target = 100

    sq_sum = 0

    l = list(range(1,target+1))

    for i in l:
       sq_sum += (i*i)

    others = sum(l) * sum(l)

    if sq_sum > others:
      res = sq_sum - others
    else:
      res =  others - sq_sum

    print "Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum : ", res

if __name__ == '__main__':
    main()
