digit_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def convert (s):
    number= ''
    try: 
        for token in s:
            number += digit_map[token]
    except (KeyError,TypeError) as e:
        print (f'Fuck your mother: {e!r}')
    
    return int(number)