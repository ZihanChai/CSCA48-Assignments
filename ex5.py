def rsum(input_list):
    ''' (list of int) -> int

    Return the sum of numbers in L.

    REQ: L is not empty.

    >>> listsum1([5])
    >>> 5
    >>> listsum1([4,1,6])
    >>> 11
    '''

    # if list has just one element
    if len(input_list) == 1:
        result = input_list[0]
    else:
        # add first number to sum of rest of list
        result = input_list[0] + rsum(input_list[1:])

    return result

def rmax(input_list):
    if len(input_list)==1:
        result = input_list[0]
    else:
        current_max = rmax(input_list[1:])
        if(input_list[0] > current_max):
            result = input_list[0]
        else:
            result = current_max
    return result

def second_smallest(input_list):
    if(len(input_list) == 2):
        if(input_list[0] > input_list[1]):
            result = input_list[0]
        elif(input_list[0] < input_list[1]):
            result = input_list[1]
        elif(input_list[0] == input_list[1]):
            result = input_list[1]
    else:
        if(input_list[0] >= input_list[1] and input_list[0] >= input_list[2]):
            input_list[:] = input_list[1:]
            result = second_smallest(input_list[:])
        elif(input_list[1] >= input_list[0] and input_list[1] >= input_list[2]):
            input_list[:] = input_list[:1] + input_list[2:]
            result = second_smallest(input_list[:])
        else:
            input_list[:] = input_list[:2] + input_list[3:]
            result = second_smallest(input_list[:])
    return result

def sum_max_min(input_list):
    if(len(input_list) == 1):
        result = input_list[0] * 2
    elif(len(input_list) == 2):
        result = input_list[0] + input_list[1]
    else:
        if((input_list[2] <= input_list[1] and input_list[1] <= input_list[0]) 
           or (input_list[0] <= input_list[1] and input_list[1] <= input_list[2])):
            input_list[:] = input_list[:1] + input_list[2:]
            result = sum_max_min(input_list[:])
        elif((input_list[1] <= input_list[0] and input_list[0] <= input_list[2]) or
             (input_list[2] <= input_list[0] and input_list[0] <= input_list[1])):
            input_list[:] = input_list[1:]
            result = sum_max_min(input_list[:])
        else:
            input_list[:] = input_list[:2] + input_list[3:]
            result = sum_max_min(input_list[:])
    return result