"""
@date: 2020-4-10
@author: WangTingZheng
@feature: 这里定义了一些加密/解密的函数
"""

import cryptographyImmortal.convert as convert
import cryptographyImmortal.check as check
import cryptographyImmortal.affine as affine


def encoding(char_list, k1, k2):
    """
    加密函数，不带字母与整数之间的转化
    :param char_list: 整型list，明文空间，由字母明文空间转化而来
    :param k1: 整型，密钥中的k1
    :param k2: 整型，密钥中的k2
    :return: 整型list，加密之后的整数密文空间，可转化为字母密文空间
    """
    res = []
    for i in char_list:
        res.append((i * k1 + k2) % 26)  # 根据仿射密码加密公式编写
    return res


def decoding(char_list, k1, k2):
    """
    解密函数，不带字母与整数之间的转化
    :param char_list: 整型list，密文空间，由字母密文空间转化而来
    :param k1: 整型，密钥中的k1
    :param k2: 整型，密钥中的k2
    :return: 整型list，解密之后的整数明文空间，可转化为字母明文空间
    """
    res = []
    k_1 = affine.return_inverse_element(k1, 26)
    for i in char_list:
        res.append((k_1 * (i - k2)) % 26)  # 根据仿射密码解密公式编写
    return res


def encoding_or_decoding(convert_list, k1, k2, mode):
    """
       完整的加密函数，包含了检查、转化功能
       :param convert_list: 字符list，明文空间，list每个元素是一个字母，从左往右
       :param k1: 整型，密钥中的k1
       :param k2: 整型，密钥中的k2
       :param mode: 字符串, 模式选择, 可以传入"encoding"和”decoding", 如果有其它传入，终止变换并报错
       :return: 字符list，加密之后的密文空间，list每一个元素是一个字母，从左往右
       """
    k_list = check.check_key_all(convert_list, k1, k2)  # 检查明/密文空间、密钥是否合法
    if k_list is False:
        return False
    k1 = k_list[0]
    k2 = k_list[1]
    if k1 is False and k2 is False:
        return False

    convert__int_list = convert.char_to_int(convert_list)  # 把字母明文空间转化为整数明文空间
    if mode == "encoding":
        res_int_list = encoding(convert__int_list, k1, k2)  # 加密整数明文空间
    elif mode == "decoding":
        res_int_list = decoding(convert__int_list, k1, k2)  # 加密整数明文空间
    else:
        print("mode参数错误，请输入\"encoding\"或者\"\decoding\"")
        return False
    res_char_list = convert.int_to_char(res_int_list)  # 把加密完的整数密文空间转化为字符密文空间
    return res_char_list
