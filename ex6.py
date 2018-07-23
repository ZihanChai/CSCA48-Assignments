def rsum(list1):
    if (type(list1) == list):
        if(len(list1) == 0):
            result = 0
        elif (len(list1) == 1):
            if (type(list1[0]) == list):
                result = rsum(list1[0])
            else:
                result = list1[0]
        else:
            result = rsum(list1[0]) + rsum(list1[1:])
    else:
        result = list1
    return result

def rmax(list1):
    if (type(list1) == list):
        if(len(list1) == 0):
            result = None
        elif(len(list1) == 1):
            result = rmax(list1[0])
        else:
            current_max = rmax(list1[1:])
            if (current_max == None):
                result = rmax(list1[0])
            elif (rmax(list1[0]) == None):
                result = rmax(list1[0])
            elif(rmax(list1[0]) > current_max):
                result = rmax(list1[0])
            else:
                result = current_max
    else:
        result = list1
    return result

