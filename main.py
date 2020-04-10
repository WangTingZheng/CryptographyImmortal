Encoding_list=["c","h","i","n","a"]
Decoding_list = ['u', 'n', 'w', 'p', 'c']


def checkV(convert_list, k1, k2):
    import cryptographyImmortal.action as action
    import cryptographyImmortal.check as check

    k1 = check.isInt(k1)
    k2 = check.isInt(k2)
    if(k1 is False and k2 is False):
        return False
    elif(check.gcd(k1,26) !=1):
        return False
    elif(check.isChar(convert_list) is False):
        return False
    return k1,k2

def EncodingTest(convert_list, k1, k2):
    import cryptographyImmortal.action as action
    import cryptographyImmortal.check as check
    k_list = checkV(convert_list, k1,k2)
    if(k_list is False):
        return False
    k1 = k_list[0]
    k2 = k_list[1]
    if(k1 is False and k2 is False):
        return False
    elif(check.isChar(convert_list) is False):
        return False

    convert_list = check.charToInt(convert_list)
    res_list = action.Encoding(convert_list, k1, k2)
    res_list = check.IntToChar(res_list)
    return (res_list)


def DecodingTest(convert_list, k1, k2):
    import cryptographyImmortal.action as action
    import cryptographyImmortal.check as check

    k1 = check.isInt(k1)
    k2 = check.isInt(k2)
    if(k1 is False and k2 is False):
        return False
    elif(check.gcd(k1,26) !=1):
        return False
    elif(check.isChar(convert_list) is False):
        return False

    convert_list = check.charToInt(convert_list)
    res_list = action.Decoding(convert_list, k1, k2)
    res_list = check.IntToChar(res_list)
    return res_list


print(EncodingTest(Encoding_list, 9,2))
print("=========================")
print(DecodingTest(Decoding_list,9,2))
