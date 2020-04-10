def Encoding(char_list, k1, k2):
    res = []
    for i in char_list:
        res.append((i*k1+k2)%26)
    return res


def Decoding(char_list, k1, k2):
    import app.convert as convert
    res = []
    k_1 = convert.returnInverseElement(k1,26)
    for i in char_list:
        res.append((k_1*(i-k2))%26)
    return res