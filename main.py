# from json import dumps

BIN_DATA = 'data.txt'

container, max_length = dict(), 0

"""
Creating data dictionary
"""
   
def locate(cont, *indexes):
    if not cont.get(indexes[0]):
        cont[indexes[0]] = dict()
        
    if indexes[1:]:    
        locate(cont[indexes[0]], *indexes[1:])

with open(BIN_DATA, 'r') as read_stream:
    rows = read_stream.readlines()
    
    for row in rows:
        if len(row.rstrip('\n')) > max_length:
            max_length = len(row.rstrip('\n'))
    
    for row in rows:
        locate(container, *[i for i in row.rstrip('\n')])
    
# print(dumps(container, sort_keys=True, indent=4))

"""
Painting binary tree
"""

R_HEIGHT = 5
MAIN_SIGN = '+'
DIVIDER = '-'

ramifications = list()

for i in range(1, max_length + 1):
    if i * 5 % 2 == 0:
        ramifications.append(i * 5 * i+ 1)
    else:
        ramifications.append(i * 5 * i)
        
WIDTH = sum(ramifications) + max_length + 1
    
ramifications = list(reversed(ramifications))

bin_tree = str()
previous_indent = 0

for i in range(len(ramifications)):
    print()
    
    if previous_indent == 0:
        previous_indent = (WIDTH - ramifications[i]) // 2
        
        print(DIVIDER * previous_indent, MAIN_SIGN * ramifications[i], DIVIDER * previous_indent, sep='', end='')
    else:
        previous_indent = previous_indent - ramifications[i] // 2
        
        for k in range(2 ** i * 2 + 1):
            if k == 0 or k == 2 ** i * 2:
                print(DIVIDER * previous_indent, end='')
            else:
                if (k + 1) % 2 == 0:
                    print(MAIN_SIGN * ramifications[i], end='')
                else:
                    # if (k + 1) % 5 == 0:
                        # print(DIVIDER * ((WIDTH - (2 ** i * ramifications[i] + (ramifications[i - 1] - ramifications[i] - 1) * (2 ** (i - 1)))) // (i + 1)), end='')
                    
                    print(DIVIDER * (ramifications[i - 1] - ramifications[i] - 1), end='')