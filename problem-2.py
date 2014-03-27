#! /usr/bin/env python


########
#
# Even Fibonacci numbers
#
########

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():

    final_sum = 0
    max_sequence_value = 4000000
    i = 1
   
    while final_sum <= max_sequence_value:

      x = fib(i)
      if x%2 == 0:
         final_sum += x
      i += 1
    
    print "Fibanacci Sequence not exceeding ", max_sequence_value, " sum of even-valued terms is: ", final_sum

if __name__ == '__main__':
    main()

