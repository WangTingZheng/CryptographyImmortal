def gcd(a, b):
    """
    求两个整数的最大公约数, 输入的a必须大于b
    :param a: 整型变量，其中一个数
    :param b: 整型变量，另一个数
    :return: 整型变量，a和b的最大公约数
    """
    if a % b == 0:
        return b
    return gcd(b, a % b)


def return_gcd(a, b):
    """
    返回a与b的最大公约数，不需要考虑a和b的大小关系
    :param a: 整型变量，其中一个数
    :param b: 整型变量，另一个数
    :return: 整型变量，a和b的最大公约数
    """
    if a > b:
        return gcd(a, b)
    else:
        return gcd(b, a)


def char_to_int(char_list):
    """
    把字符密文/明文空间list转化为整数list，规则是a对应0，z对应25
    :param char_list: 要转化的字符密文/明文空间list
    :return: 转化好的整型密文/明文空间list
    """
    res = []
    for i in char_list:
        res.append(ord(i) - 97)
    return res


def int_to_char(char_list):
    """
    把整型密文/明文空间list转化为字符list，规则是0对应a，25对应z
    :param char_list: 要转化的整型密文/明文空间list
    :return: 转化好的字符密文/明文空间list
    """
    res = []
    for i in char_list:
        res.append(chr(i + 97))
    return res