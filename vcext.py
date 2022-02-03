import string

def number_to_letter(number):
    return chr(int(repr(number).replace("'",''))%256)

def letter_to_number(char):
    return ord(char)

def encode_char(char,nkey):
    cipher = letter_to_number(char) + letter_to_number(nkey) % 256
    return number_to_letter(cipher)

def decode_char(char,nkey):
    plainchar = letter_to_number(char) - letter_to_number(nkey) % 256
    return number_to_letter(plainchar)

def create_key(file,k):
    k = k.replace(" ",'')
    text = file
    key = ''
    i = 0
    for char in text:
        ki = i % len(k)
        key = key + k[ki]
        i = i + 1
    return key

def encode_text(file,k):
    plaintext = ''
    for x in file:
        if x not in string.ascii_letters:
            continue
        plaintext = plaintext + x

    cipher = ''
    key = create_key(file,k)
    i = 0
    for char in plaintext:  
        cipher = cipher + encode_char(char, key[i])
        i = i + 1
    return cipher

def decode_text(file,k):
    ciphertext = file
    plain = ''
    key = create_key(file,k)
    i = 0
    for char in ciphertext:
        plain = plain + decode_char(char, key[i])
        i = i + 1
    return plain