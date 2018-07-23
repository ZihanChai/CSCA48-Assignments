from container import *
    
def banana_verify(source_word, goal_word, container, list_moves):
    '''(str, str, class, list) -> bool
    Return true if the word aftersource word changed by the order of movement
    in the ist is same as the goal word and there is no character left
    in the container, otherwise return false.
    '''
    new_string = ''
    i = 0
    character = 0
    cur = container()
    while character != source_word:
        while i != range(len(list_move)):
            if list_move[i] == 'p':
                try:
                    cur.put(source_word[character])
                except ContainerFullException:
                    return False
                i += 1
                character += 1
            elif list_move[i] == 'M':
                new_string += source_word[character]
                i += 1
                character += 1                
            elif list_move[i] == 'G':
                try:
                    new_string += cur.get()
                except ContainerEmptyException:
                    return False
                i += 1
                character += 1
    if container.is_empty() is False:
        return False    
    return new_string == goal_word
