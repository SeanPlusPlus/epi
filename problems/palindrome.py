#!/usr/bin/env python

# is a string a palindrome

def main():
    myStr = 'racecar'
    length = (len(myStr) - 1)

    def is_palindrome(el):
        print str(el) + ' ' + myStr[el] + ' ' + myStr[(length - el)] + ' ' + str(length - el)
        if el == length:
            return True
        elif myStr[el] != myStr[( length - el )]:
            return False
        else:
            el += 1
            return is_palindrome(el)

    print is_palindrome(0)


if __name__ == '__main__':
    main()
