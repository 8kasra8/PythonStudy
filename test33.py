def nth_root(radicand, n):
    return radicand ** (1/n)

def ordinal_suffix(value):
    valueInString = str(value)

    if valueInString.endswith('11') or valueInString.endswith('12') or valueInString.endswith('13'):
        return 'th'
    elif valueInString.endswith('1'):
        return 'st'
    elif valueInString.endswith('2'):
        return 'nd'
    elif valueInString.endswith('3'):
        return 'rd'
    else:
        return 'th'

        
def ordinal (value):
    return str(value) + ordinal_suffix(value)

def display_nth_root (radicand, n):
    root = nth_root(radicand,n)
    message = "The " + ordinal(n) + " root of " + str(radicand) + " is "+ str(root)

    print(message)

if __name__ == "__main__":
    display_nth_root(16,2)