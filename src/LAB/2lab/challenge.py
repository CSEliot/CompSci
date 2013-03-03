import math
 
def isPrime(n):
    rooted = math.sqrt(n)
#    print n + 0.0
 #   print rooted
    if n == 2.0:
        return True
    else:
        for divisor in range(2, int(rooted)+2):
 #           print divisor
  #          print n % divisor
            if n % divisor == 0:
                return False
        return True
 
def main():
    for i in range(2, 18):
        print "Is {0} prime? {1}".format(i, isPrime(i))
 
main()
