def edit_distance(s1, s2):
    mid = len(s1)//2 + 1
    if (len(s1) == 0) and (len(s2) == 0):
        result = 0
    elif(s1[0] != s2[0]):
        result = (1 + edit_distance(s1[1:mid], s2[1:mid]))
    elif(s1[0] == s2[0]):
        result = (0 + edit_distance(s1[1:mid], s2[1:mid]))
    return result


def subsequence(s1, s2):
    if (len(s1) == 0):
        result = True
    elif (len(s2) == 0):
        result = False
    else:
        try:
            result = subsequence(s1[1:], s2[(s2.index(s1[0]) + 1):])
        except:
            result = False
    return result


def perms(s):
    if (len(s) <= 1):
        result = s
    else:
        new_list = []
        rest_string = perms(s[1:])
        curr_letter = s[0]
        for letter in rest_string:
            for i in range(len(letter)+1):
                new_list.append(letter[:i] + curr_letter + letter[i:])
        result = new_list[:]
    return result