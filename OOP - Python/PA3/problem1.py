#Amandeep Singh Ruid 145003464

def replace_char(astr, old_char, new_char):
    '''recursive function to replace char'''
    empty='' #initially empty
    if astr == empty:
        return astr
    if astr[0] == old_char: #if old char found
        return new_char + replace_char(astr[1:], old_char, new_char) #replace and recusrively send second part
    return astr[0] + replace_char(astr[1:], old_char, new_char)


def num_double_letters(astr):
    '''counts number of double letters in input string'''
    empty=""
    if astr == empty or len(astr) == 1: #base case
        return 0
    elif len(astr) == 2:
        if astr[0] == astr[1]: #second base case
            return 1
        else: 
            return 0
    elif astr[0] != astr[1]: #take latter part
        ret_str=astr[1:]
        return 0 + num_double_letters(ret_str)
    elif astr[0] == astr[1]:
        ret_str=astr[2:]  #take letter skipping 2
        return 1 + num_double_letters(ret_str)


def has_repeats(L):
    '''checks for repeating elements in list L recursively'''
    start=0
    mid=1
    end=2
    if len(L) <= mid: # if 0 element
        return False
    if L[start] == L[mid]:  #if 1 element
        return True
    if has_repeats([L[start]] + L[end:]): 
        return True
    if has_repeats(L[mid:]):
        return True
    return False
