import cryptographyImmortal.action as action

Encoding_list = ["c", "h", "i", "n", "a"]
Decoding_list = ['u', 'n', 'w', 'p', 'c']

print(action.encoding_or_decoding(Encoding_list, 9, 2, "encoding"))
print("=========================")
print(action.encoding_or_decoding(Decoding_list, 9, 2, "decoding"))
