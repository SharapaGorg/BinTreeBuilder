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
MAIN_SIGN = '*'
DIVIDER = ' '

ramifications = list()

for i in range(1, max_length + 1):
    if i * 5 % 2 == 0:
        ramifications.append(i ** 2 * 5 + 1)
    else:
        ramifications.append(i ** 2 * 5)
        
WIDTH = sum(ramifications) + max_length + 1
    
ramifications = list(reversed(ramifications))

bin_tree = str()
previous_indent = 0
previous_center = 0

for i in range(len(ramifications)):
    rams, foots = 0, str()
    
    if previous_indent == 0:
        previous_indent = (WIDTH - ramifications[i]) // 2
        
        print(DIVIDER * previous_indent, '0', MAIN_SIGN * (ramifications[i] - 2), '1', DIVIDER * previous_indent, sep='', end='')
        foots += DIVIDER * previous_indent + MAIN_SIGN + DIVIDER * (ramifications[i] - 2) + MAIN_SIGN + DIVIDER * previous_indent
    else:
        if previous_center == 0:
            previous_center = ramifications[i - 1] - ramifications[i] // 2 * 2 - 2
        else:
            previous_center -= ramifications[i] // 2 * 2
            
        previous_indent = previous_indent - ramifications[i] // 2
        
        for k in range(2 ** i * 2 + 1):
            if k == 0 or k == 2 ** i * 2:
                print(DIVIDER * previous_indent, end='')
                foots += DIVIDER * previous_indent
                
            else:
                if (k + 1) % 2 == 0:
                    print('0' + MAIN_SIGN * (ramifications[i] - 2) + '1', end='')
                    foots += MAIN_SIGN + DIVIDER * (ramifications[i] - 2) + MAIN_SIGN
                    
                    rams += 1
                else:
                    rams_count = ramifications[i] * 2 ** i
                    indent_length = 2 ** (i - 1) * (ramifications[i - 1] - ramifications[i] - 1)
                    indent = (WIDTH - rams_count - 2 * previous_indent - indent_length - previous_center) # indent between both ramifications
                    
                    is_center = k == (2 ** (i + 1) + 1) // 2
                    if rams == 2 and not is_center:
                        rams = 0
                        indent //= (i - 2) * 2
                        
                        print(DIVIDER * indent, end='')
                        foots += DIVIDER * indent
                    elif is_center:
                        rams = 0
                        print(DIVIDER * previous_center, end='')
                        foots += DIVIDER * previous_center

                    else:
                        print(DIVIDER * (ramifications[i - 1] - ramifications[i] - 1), end='')
                        foots += DIVIDER * (ramifications[i - 1] - ramifications[i] - 1)
                        
    foots = '\n' + foots
    foots *= R_HEIGHT
    print(foots)