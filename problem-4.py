#! /usr/bin/env python

###########
#
# Largest palindrome product
#
###########

def is_palin(prod):
   snumber = str(prod)
   rev = snumber[::-1]

   if snumber == rev:
      return True
   else:
      return False

def main():

  l = []
  for i in range(100,1000):
      for j in range(i,1000):
         prod = i * j
         if is_palin(prod):
            l.append(prod)

  print "Largest palindrome made from the product of two 3-digit numbers is: ", max(l)

if __name__ == '__main__':
   main()
