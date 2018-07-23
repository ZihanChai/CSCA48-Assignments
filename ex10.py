from container import *


def banana_game(s1, s2, c):
    result = find_result(s1, s2, c)
    if (result == s2):
        result = True
    else:
        result = False
    return result


def find_result(s1, s2, c):
    result = ''
    if (len(s1) == 0):
        while not c.is_empty():
            result = result + c.get()
    else:
        if (s1 == s2):
            result = result + s1
        elif (not c.is_empty()) and (c.peek() == s2[0]):
            result = result + c.get()
            result = result + find_result(s1, s2[1:], c)
        elif (s1[0] == s2[0]):
            result = result + s1[0]
            result = result + find_result(s1[1:], s2[1:], c)
        else:
            try:
                c.put(s1[0])
                result = result + find_result(s1[1:], s2, c)
            except ContainerFullException:
                result = ''
    return result
