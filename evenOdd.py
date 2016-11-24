import sys
import math

def main(a):
    if a%2 == 0:
        print "Even"
    else:
        print "Odd"
    
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            main(int(sys.argv[1]))
        except:
            print "Not an Integer"
