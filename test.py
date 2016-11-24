import sys
import math
def returnSquare (x):
    return x**2

def main(a):
    print returnSquare(int(a))
    
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            main(sys.argv[1])
        except:
            print "Not an Integer"
