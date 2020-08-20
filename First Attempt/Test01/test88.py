from math import sqrt
""" 
Prime Number Detector
"""


def is_prime(x):
    if x<2:
        return False

    for i in range(2, int(sqrt(x))+1):
        if x % i == 0:
            return False

    return True

def main():

    while True:
        inp = input("Give me a number to see if it is Prime: ")
        try:
            if is_prime(int(inp)):
                print (f"Good job!!   {inp} is a PRIME Number")
            else:
                print (f"FUCK OFF!!   {inp} is NOT A PRIME Number :| :| : |")
        except ValueError as e:
            print (f"You entered {inp} -- Bye Bye", e)


if __name__ == "__main__":
    main()

