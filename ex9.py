def radix_sort(a_list):
    
    return helper(a_list, -1, 0)

def helper(a_list, digit, count):
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    for i in a_list:
        if (len(str(i))-1) >= count:
            if str(i)[digit] == '0':
                zero.append(i)
            elif str(i)[digit] == '1':
                one.append(i)
            elif str(i)[digit] == '2':
                two.append(i)
            elif str(i)[digit] == '3':
                three.append(i)
            elif str(i)[digit] == '4':
                four.append(i)
            elif str(i)[digit] == '5':
                five.append(i)
            elif str(i)[digit] == '6':
                six.append(i)
            elif str(i)[digit] == '7':
                seven.append(i)
            elif str(i)[digit] == '8':
                eight.append(i)
            elif str(i)[digit] == '9':
                nine.append(i)
        else:
            zero.append(i)

    if (len(zero) == len(a_list)):
        result = zero[:]
    else:
        a_list = []
        a_list = helper1(a_list, zero)
        a_list = helper1(a_list, one)
        a_list = helper1(a_list, two)
        a_list = helper1(a_list, three)
        a_list = helper1(a_list, four)
        a_list = helper1(a_list, five)
        a_list = helper1(a_list, six)
        a_list = helper1(a_list, seven)
        a_list = helper1(a_list, eight)
        a_list = helper1(a_list, nine)
        #print(a_list)
        digit -= 1
        count += 1
        result = helper(a_list, digit, count)
    return result
def helper1(a_list, brunch):
    if len(brunch) > 0:
        for k in brunch:
            a_list.append(k)
    return a_list