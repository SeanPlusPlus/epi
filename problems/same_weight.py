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

def closest(x, weight, distance):
    if (bin(x + distance).count("1")) == weight:
        return (x + distance)
    if (bin(x - distance).count("1")) == weight:
        return x - distance
    distance += 1
    return closest(x, weight, distance)

def main():
    x = 92
    weight = bin(x).count("1")
    y = closest(x, weight, 1)
    print y

if __name__ == '__main__':
    main()
