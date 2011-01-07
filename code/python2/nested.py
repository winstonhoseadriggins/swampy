# quiz solution as posed

def find_depth(t, target):
    try:
        for x in t:
            if x == target:
                return 1
            else:
                depth = find_depth(x, target)
                if depth:
                    return depth+1
        return 0
    except TypeError:
        return 0

# slightly better version (different interface)

def find_depth(t, target):
    if t == target:
        return 0

    try:
        for x in t:
            depth = find_depth(x, target)
            if depth != -1:
                return depth+1
        return -1

    except TypeError:
        return -1

t = [1, [2,3], [4, [5,6, [7,8]]]]

for i in range(9):
    print i, find_depth(t, i)
