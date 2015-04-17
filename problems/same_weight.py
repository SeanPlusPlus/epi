#!/usr/bin/env python

# find the closes int with same weight.
#
# the weight of a non negative int x is number of bits that are 
# set to 1 in the binary representation. for ex 92 in base 2 is
# (1011100)2, the weight of 92 is 4.
#
# write a program which takes a non negative int x and return y,
# such that y is not equal to x, and y has same weight as x, and 
# the difference between y and x is as small as possible
# assume x is not zero or all 1s

def closest(x):
    weight = bin(x).count("1")
    return weight

def main():
    ans = closest(92)
    print ans

if __name__ == '__main__':
    main()
