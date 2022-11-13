def dirReduc(arr):
    res = arr.copy()
    for i in range(len(arr)-1) :
        if {arr[i], arr[i+1]} == {"NORTH", "SOUTH"} or {arr[i], arr[i+1]} == {"WEST", "EAST"} :
            res[i] = res[i+1] = ''
            return dirReduc(list(filter(lambda l: l != '', res)))
    return res