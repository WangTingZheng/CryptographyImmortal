def isChar(inf_list):
    for i in inf_list:
        if(type(i) is not str):
            return False
        elif(ord(i)< 97 or ord(i) > 122):
            return False
    return True

def isInt(a):
    if(type(a) is not int):
        return False
    return a%26

def gcd(a,b):
    if(a%b==0):
        return b
    return gcd(b,a%b)

def returnGcd(a,b):
    if(a>b):
        return gcd(a, b)
    else:
        return gcd(b,a)

def charToInt(char_list):
    res = []
    for i in char_list:
        res.append(ord(i)-97)
    return res

def IntToChar(char_list):
    res = []
    for i in char_list:
        res.append(chr(i+97))
    return res


