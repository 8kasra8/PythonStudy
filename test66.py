def sqrt(x):
    """
    Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root to be camputed.
    
    Returns:
        The square root of x.
    """

    guess = x
    i = 0
    while guess*guess != x and i < 20:
        guess = (guess + (x /guess))/ 2.0
        i += 1

    return guess

def main():
    while True:
        result = input("give me an integer: ")
        if result == 'q':
           break 
        try:
            print( sqrt(int(result)))
        except ZeroDivisionError:
            print(f"Division by Zerro Occured, Square Root of {result} in not Possible")

if __name__ == "__main__":
    main()
