def return_a_in_affine(a, b, temp_list):
    """
    使用辗转相除法，拿到a,b列的式子中的每一个除数c并转化为一个list，接到temp_list后面, a必须大于b
    公式是ax=dmod(b) 或者 a = b*c + d
    :param a: 整数，总数中的已知量
    :param b: 整数，被除数
    :param temp_list: 一个任意的list
    :return: list，一个原来的list加上所有c的集合
    """
    c = a // b
    d = a % b
    if d == 0:
        return temp_list
    else:
        temp_list.append(c)
    a = b
    b = d
    return return_a_in_affine(a, b, temp_list)


def return_list(a, b):
    """
    使用辗转相除法，拿到a,b列的式子中的每一个除数c并转化为一个list，接到temp_list后面, a不用必须大于b
    公式是ax=dmod(b) 或者 a = b*c + d
    :param a: 整数，总数中的已知量
    :param b: 整数，被除数
    :return: list，所有c的集合
    """
    if a > b:
        return return_a_in_affine(a, b, [])
    else:
        return_a_in_affine(b, a, [])


def return_inverse_element_temp(a, b):
    """
    返回逆元，即aa-1=1mod(b),返回a-1，a必须大于b
    :param a: 整型，所要求逆元的整数
    :param b: 整型，模数，被除数
    :return: 整型，逆元
    """
    list_a = return_list(a, b)
    b_s_1 = 1
    b_s_2 = list_a[len(list_a) - 1]

    def return_inverse_element_loop(b_1, b_2, n):
        if n != len(list_a):
            b_t_2 = list_a[len(list_a) - n - 1] * b_2 + b_1
        else:
            if n % 2 != 0:
                return a - b_2
            return b_2
        b_t_1 = b_2
        n = n + 1
        return return_inverse_element_loop(b_t_1, b_t_2, n)

    return return_inverse_element_loop(b_s_1, b_s_2, 1)


def return_inverse_element(a, b):
    """
    返回逆元，即aa-1=1mod(b),返回a-1，a不必须大于b
    :param a: 整型，所要求逆元的整数
    :param b: 整型，模数，被除数
    :return: 整型，逆元
    """
    if a > b:
        return return_inverse_element_temp(a, b)
    else:
        return return_inverse_element_temp(b, a)
