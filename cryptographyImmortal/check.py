"""
@date: 2020-4-10
@author: WangTingZheng
@feature: 这里定义了一些输入检查函数
"""


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


def check_list(inf_list):
    """
    检查用户输入的明文或密文空间是否合法
    :param inf_list: 字符list，输入的密文或明文空间，每一个元素存一个字母，字母只能是小写的，从左往右
    :return: 如果合法，返回True，否则返回False
    """
    for i in inf_list:
        if type(i) is not str:  # 如果有元素不是字符型的，不合法
            print("[错误]：输入的明文空间或者密文空间有不是字符的元素")
            return False
        elif len(i) != 1:  # 如果一个元素不止有一个字符的，不合法
            print("[错误]：输入的明文空间或者密文空间有不是单个字符的元素")
            return False
        elif ord(i) < 97 or ord(i) > 122:  # 如果字符不是小写字母，不合法
            print("[错误]：输入的明文空间或者明文空间有不是小写字母的元素")
            return False
    return True


def check_key(a):
    """
    检查密钥空间是否合法
    :param a: 整型变量，要检查的密钥空间的其中一个
    :return: 如果合法，返回mod(26)后的密钥（整型变量），否则返回False
    """
    if type(a) is not int:  # 如果密钥不是整型，不合法
        print("[错误]：输入的密钥空间有不是整数的密钥")
        return False
    return a % 26  # 如果合法，则返回mod（26)的密钥


def check_key_all(convert_list, k1, k2):
    """
    检查所有输入值函数
    :param convert_list: 字符list，需要检查的明文/密文空间
    :param k1: 整型变量，密钥空间中的k1
    :param k2: 整型变量，密钥空间中的k2
    :return: 如果全合法，则返回由mod（26)后k1,k2组成的整型list，否则，返回False
    """
    k1 = check_key(k1)
    k2 = check_key(k2)
    if k1 is False and k2 is False:
        return False
    elif gcd(k1, 26) != 1:
        print("[错误]：密钥k1不符合仿射密码要求，与26的最大公约数不是1")
        return False
    elif check_list(convert_list) is False:
        return False
    return k1, k2
