import sys
from math import exp

def read_altitude():
    try:
        h = float(sys.argv[1])
    except IndexError:
        raise IndexError(
            'The altitude must be supplied on the command line.'
        )
    except ValueError:
        raise ValueError(
            f'Altitude must be a number, not "{sys.argv[1]}".'
        )
    
    if h < -430 or h > 13000:
        raise ValueError(
            f'The formula is not valid for h = {h}!'
        )
    
    return h

try:
    h = read_altitude()
    p0 = 100.0
    h0 = 8400
    print(p0 * exp(-h/h0))
except (IndexError, ValueError) as e:
    print(e)
    exit()