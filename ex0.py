def greeting(name):
    ''' (string) -> string
    returns a greeting in the form Hello <name> how are you today? where
    <name> is replaced by the input parameter.
    >>>greeting('Mars')
       'Hello Mars how are you today?'
    '''
    return 'Hello ' + name + ' how are you today?'


def mutate_list(the_list):
    ''' (list) -> Nonetype
    Return a nonetype the input must be a list and for any element
    that is an integer is multipled by 2; any element that is a boolean is
    inverted (True becomes False, False becomes True); any element that is
    a string has its first and last letters removed; the 0th element of the
    list is set to the string Hello, regardless of what it was originally
    REQ: the input must be a list
    >>>mutate_list([1, True, 2, 'Mars'])
       ['Hello', False, 2, 'ar']
    '''
    # Check the type of elements in the list one by one
    for element in range(len(the_list)):
        if type(the_list[element]) == int:
            element = element * 2
        elif type(the_list[element]) == bool:
            if the_list[element] is True:
                the_list[element] = False
            elif the_list[element] is True:
                the_list[element] = False
        elif type(the_list[element]) == str:
            the_list[element] = the_list[element][1:-1]
    the_list[0:1] = ['Hello']


def merge_dicts(fir_dict, sec_dict):
    ''' (dict of  {str: list of ints}, dict of dict of  {str: list of ints}) ->
    dict of dict of  {str: list of ints}
    Return a new dictionary with all key:value pairs from both dictionaries. 
    If the dictionaries share a key, the resulting value will be the list from
    the second dictionary appended to the list from the firs dictionary
    >>> d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    >>> d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    >>> merge_dicts(d1, d2)
    {'a': [1, 2, 3, 2], 'b': [4, 8, 9, 0], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    >>> merge_dicts(d2, d1)
    {'a': [2, 1, 2, 3], 'b': [8, 9, 0, 4], 'c': [5, 6, 7], 'd': [10, 11, 12]}
    '''
    # Create a new dict
    new_dict = {}
    # Create a new list to store all the keys of both dictionaries
    keys = []
    # Find the common key shared by two dictionaries and append the second dict
    # value to the first dict's value
    for key1 in fir_dict:
        for key2 in sec_dict:
            if key1 == key2:
                keys.append(key1)
                new_dict[key1] = fir_dict[key1]
                for value in sec_dict[key1]:
                    new_dict[key1].append(value)
    # Add the different values to the new dict
    for key1 in fir_dict:
        for key2 in sec_dict:
            if key1 not in keys:
                new_dict[key1] = fir_dict[key1]
            elif key2 not in keys:
                new_dict[key2] = sec_dict[key2]
    return new_dict