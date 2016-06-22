# Newton's iterative method for estimating 
# the square root of an arbitrary number, k:
# begin with an initial guess, x;
# replace x with the average of x and k/x;
# repeat until desired accuracy is reached.

from math import sqrt                              # needed only for comparison

def newton_estimate(radicand, accuracy):
#    root = radicand / 2                             # initial estimate is set at 1/2 the radicand
    root = log(radicand)                            # inital estimate is set at natural log of radicand
    limit = 0                                       # loop limiter
    while abs((root ** 2 - radicand)) > (1 / (10 ** accuracy)) and limit < 1000000:  # loops up to limit while accuracy not yet reached
        root = (root + radicand / root) / 2         # Newton's iterative method
        limit += 1                                  # increments limiter
    return root, limit

def newtons_root():
    accuracy = int(input("Enter up to 15 decimal places of accuracy: "))  # asks for accuracy level
    
#    option to set radicand
#    radicand = float(input("Enter the non-negative radicand: "))
#    print(radicand, newton_estimate(radicand, accuracy), "|", sqrt(radicand))

#    option for finding a range of roots
    for radicand in range(15, 100016, 10000):
        print(radicand, newton_estimate(radicand, accuracy), "|", sqrt(radicand))
    
def main():
    newtons_root()

main()
