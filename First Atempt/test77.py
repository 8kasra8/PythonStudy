import sys

def sqrt(x):
    """
    Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root to be camputed.
    
    Returns:
        The square root of x.

    Raises:
        ValueError : if x is negative
    """

    if x<0:
        raise ValueError (f"SQRT of {x} not possible")
    guess = x
    i = 0
    while guess*guess != x and i < 20:
        guess = (guess + (x /guess))/ 2.0
        i += 1

    return guess



def main():
    while True:
        result = input("give me an integer: ")
        try: 
            result_int = int(result)
            try: 
                print( sqrt(result_int))
            except ValueError as err:
                print (err , file=sys.stderr)
        except ValueError as e:
           print ("this is the cought error: ",e)
           break
     
            
if __name__ == "__main__":
    main()
