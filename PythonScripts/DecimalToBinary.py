import sys, os

#
# THIS IS UNFINISHED!!!!
#

OG = input("Enter floating point number to fit in IEEE: ")
if int(OG) > 2**22:
    print "TOO BIG"
    sys.exit()
elif not "." in str(OG):
    print "NEEDS '.'"
    sys.exit()
isNeg = 0

OG = str(OG)
if "-" in OG:
    isNeg = 1
OG = OG.replace("-", "")
OB

c, u = str(OG).split(".")
c = int(c)
u = int(u)
OG_c = c
OG_u = u

Mantissa_Len = 23
Exponent_Len = 8
binString1 = ""
binString2 = ""


print "MANTISSA - INTEGRAL"
for i in range(Mantissa_Len-1, -1, -1):
    bin_ = 2**i
    red_ = c - bin_
    if bin_ <= c:
        binString1 = binString1 + "1"
        outString = "2^" + "{:<2}".format(i) + " -- " + "{:<10}".format(c) 
        outString = outString + " - " + "{:<10}".format(bin_) + " = " 
        outString = outString + "{:<10}".format(red_) + " || " 
        outString = outString + "{:0<23}".format(binString1) 
        print outString
        c = red_
    else:
        binString1 = binString1 + "0"
binString1 = "0b" + binString1

print
print "MANTISSA - FRACTIONAL"
u = "0." + str(u)
u = float(u)
#NOTE: NORMALLY, WE'D JUST KEEP GOING TILL u*2 == 1
#BUT!! 8 digits of decimal is plenty, and 1/3 can take a while . . .
for i in range(Exponent_Len):
    u = u*2.0
    if u >= 1.0:
        binString2 = binString2 + "1"
        print "{:<10}".format(u/2.0) + " x 2 = " + "{:<10}".format(u) + "{:0<8}".format(binString2) 
        u = u - 1.0
    else:
        binString2 = binString2 + "0"

finString = binString1[2:] + "." + binString2
print
print "Final Binary is in Abs: "+ finString
print

print "NORMALIZE & COUNT EXP"
#add dot to right of leftest 1
dotLoc = 0
for i in range(len(finString)):
    if finString[i] == "1":
        finString = finString[:i+1] + "." + finString[o+1:]
        dotLoc = i
        break

#count distance between dots. This is your exponent.
exp = 0
for i in range(len(finString)):
    exp += 1
    if finString[dotLoc + i + 1] == ".":
        print "LOL"
#if integral is 0, then negative exponent 
#remove all zeros to the left of leftest 1
#remove that one and both dots
#fill empty rights with 0 till 23 total spaces
# turn that exponent into bin(exp + 127) 127 is 2^k - 1 and k is exponent field size.
# add leftest bit 1/0 for neg/not neg

print "Calculated Binary  = " + binString1
print "Calculated Mantisa = " + str(int(binString1, 2))
print "Given Binary       = " + "{:0>25}".format(str(bin(OG_c)))
print "Given Decimal      = " + str(OG)
