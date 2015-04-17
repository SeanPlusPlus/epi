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

def closest(bin_x, place):
    if bin_x[place] != bin_x[place - 1]:
        li = list(bin_x)
        li[place] = bin_x[place - 1]
        li[place - 1] = bin_x[place]
        return "".join(li)
    place -= 1
    return closest(bin_x, place)


def main():
    x = 92
    bin_x = "{0:08b}".format(x)
    place = 0
    bin_y = closest(bin_x, (len(bin_x) - 1))
    print int(bin_y, 2)


if __name__ == '__main__':
    main()
