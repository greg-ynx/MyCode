def same_structure_as(original,other):
    if type(original) == list and type(other) == list :
        if len(original) != len(other) : return False
        for i in range(len(original)):
            if not same_structure_as(original[i],other[i]):
                return False
        return True
    elif type(original) != list and type(other) != list :
        return True
    else : return False