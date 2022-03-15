def encode(plain_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    plain, cipher = list(plain), list(cipher)
    key = dict(zip(plain, cipher))
    del(plain)
    cipher = ""
    count = 0
    plain_text = plain_text.lower()
    for char in plain_text:
        if char.isalnum():
            if count == 5:
                cipher += ' '
                count = 0
            if char.isdigit():
                cipher += char
            else:
                cipher += key[char]
            count += 1          
    return cipher

def decode(ciphered_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    plain, cipher = list(plain), list(cipher)
    key = dict(zip(cipher, plain))
    del(cipher)
    plain = ""
    for char in ciphered_text:
        if char in key.keys():
            plain += key[char]
        if char.isdigit():
            plain += char
    return plain
