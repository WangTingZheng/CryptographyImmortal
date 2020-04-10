def affine(a, b, temp_list):
    # a = b*c + d
    c = a // b
    d = a % b
    if (d == 0):
        return temp_list
    else:
        temp_list.append(c)
    a = b
    b = d
    return affine(a, b, temp_list)


def returnList(a, b):
    return affine(a, b, [])


def returnInverseElementAPI(a,b):
    list_a = returnList(a, b)
    b_s_1 = 1
    b_s_2 = list_a[len(list_a)-1]
    def returnInverseElementLoop(b_1, b_2, n):
        if(n != len(list_a)):
            b_t_2 = list_a[len(list_a)-n-1]*b_2 + b_1
        else:
            if(n%2 != 0):
                return a-b_2
            return b_2
        b_t_1 = b_2
        n = n + 1
        return returnInverseElementLoop(b_t_1, b_t_2, n)
    return returnInverseElementLoop(b_s_1, b_s_2, 1)

def returnInverseElement(a,b):
    if(a>b):
        return returnInverseElementAPI(a,b)
    else:
        return returnInverseElementAPI(b,a)