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
MIN_WIDTH = 5

ramifications = list()

for i in range(1, max_length + 1):
    if i * MIN_WIDTH % 2 == 0:
        ramifications.append(i ** 2 * MIN_WIDTH + 1)
    else:
        ramifications.append(i ** 2 * MIN_WIDTH)
        
WIDTH = sum(ramifications) + max_length + 1
    
ramifications = list(reversed(ramifications))

bin_tree = str()
previous_indent = 0
previous_center = 0

def check_index(cont, indexes) -> bool:
    for elem in indexes:
        if elem in cont:
            cont = cont[elem]
        else:
            return False
        
    return True

def find_path (power, ram):
    result1 = str()
    
    for i in range(1, power + 1):
        if ram * 2 <= 2 ** i // 2:
            result1 += '0'
        else:
            result1 += '1' 
           
    return result1[::-1][:len(result1) - 1] + '0', result1[::-1]
            
for i in range(len(ramifications)):
    rams, foots = 0, str()
    
    if previous_indent == 0:
        previous_indent = (WIDTH - ramifications[i]) // 2
        
        half1 = MAIN_SIGN if container.get('0') else DIVIDER
        half2 = MAIN_SIGN if container.get('1') else DIVIDER
        
        print(DIVIDER * previous_indent, 
              '0' if container.get('0') else ' ', 
              half1 * ((ramifications[i] - 2) // 2), 
              MAIN_SIGN, 
              half2 * ((ramifications[i] - 2) // 2), 
              '1' if container.get('1') else ' ', 
              DIVIDER * previous_indent, 
              sep='', 
              end='')
        
        foots += DIVIDER * previous_indent + half1 + DIVIDER * (ramifications[i] - 2) + half2 + DIVIDER * previous_indent
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
                    rams += 1
                    
                    path1, path2 = find_path(i + 1, rams)

                    # problem in find_path func -> the same pass appears > 1 onces
                    print(container, file = open('output.txt', 'a'))
                    print(path1, path2, file = open('output.txt', 'a'))
                    print(check_index(container, path1), check_index(container, path2), file = open('output.txt', 'a'))

                    half1 = MAIN_SIGN if check_index(container, path1) else DIVIDER
                    half2 = MAIN_SIGN if check_index(container, path2) else DIVIDER

                    print(' ' if half1 == DIVIDER else '0', 
                          half1 * ((ramifications[i] - 2) // 2), 
                          ' ' if half1 == DIVIDER and half2 == DIVIDER else MAIN_SIGN, 
                          half2 * ((ramifications[i] - 2) // 2), 
                          ' ' if half2 == DIVIDER else '1', end='', sep='')
                    
                    foots += half1 + DIVIDER * (ramifications[i] - 2) + half2
                else:
                    rams_count = ramifications[i] * 2 ** i
                    indent_length = 2 ** (i - 1) * (ramifications[i - 1] - ramifications[i] - 1)
                    indent = (WIDTH - rams_count - 2 * previous_indent - indent_length - previous_center) # indent between both ramifications
                    
                    is_center = k == (2 ** (i + 1) + 1) // 2
                    if rams % 2 == 0 and not is_center:
                        indent //= (i - 2) * 2
                        
                        print(DIVIDER * indent, end='')
                        foots += DIVIDER * indent
                    elif is_center:
                        print(DIVIDER * previous_center, end='')                                            
                        foots += DIVIDER * previous_center

                    else:
                        print(DIVIDER * (ramifications[i - 1] - ramifications[i] - 1), end='')
                        foots += DIVIDER * (ramifications[i - 1] - ramifications[i] - 1)
                        
    foots = '\n' + foots
    foots *= R_HEIGHT
    print(foots)