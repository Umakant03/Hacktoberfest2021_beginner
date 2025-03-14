# Python3 program to find compound
# interest for given values.
 
def compound_interest(principle, rate, time):
 
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is ",end="")
    return CI
 
print(compound_interest(10000, 10.25, 5))
