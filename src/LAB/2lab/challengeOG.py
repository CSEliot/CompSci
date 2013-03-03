
import math
 
def isPrime(n):
    if n == 2:
        return True
    for divisor in range(2, int(math.sqrt(n))+2):
        if n % divisor == 0:
            return False
    return True
 
def main():
    for i in range(2, 18):
        print "Is %d prime?  %s" % (i, isPrime(i))
 
main()
