import sys

def main(a, b):
    if a <= b:
        print round(a/b, 2)
    else:
        print round(a * b, 2)
    
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        try:
            main(float(sys.argv[1]), float(sys.argv[2]))
        except:
            print "Not an Integer"
