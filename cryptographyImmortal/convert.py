"""
@date: 2020-4-10
@author: WangTingZheng
@feature: 这里定义了一些有关转换的函数
"""


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