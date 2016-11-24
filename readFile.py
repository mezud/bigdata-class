import sys
import math


def main(a):
    input = open(a, 'r')
    count = 0
    for line in input:
        print line
        count += 1
        if count >= 100:
            break
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            main(sys.argv[1])
        except:
            print "Not an Integer"
