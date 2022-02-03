import string

def number_to_letter(number):
    return string.ascii_letters[number]

def letter_to_number(char):
    letter = dict(zip(string.ascii_letters,[(ord(c)%32)-1 for c in string.ascii_letters]))
    return letter[char]

def encode_char(char,nkey):
    cipher = letter_to_number(char) + letter_to_number(nkey) % 26
    return number_to_letter(cipher)

def decode_char(char,nkey):
    plainchar = letter_to_number(char) - letter_to_number(nkey) % 26
    return number_to_letter(plainchar)

def create_key(file,k):
    text = file.replace(" ",'')
    k = k.replace(" ",'')
    key = ''
    i = 0
    for char in text:
        ki = i % len(k)
        key = key + k[ki]
        i = i + 1
    return key.upper()

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
        if (i % 5 == 0 and i != 0):
            cipher = cipher + " " + encode_char(char, key[i])
        else:
            cipher = cipher + encode_char(char, key[i])
        i = i + 1
    return cipher.upper()

def decode_text(file,k):
    ciphertext = file.replace(" ",'')
    plain = ''
    key = create_key(file,k)
    i = 0
    for char in ciphertext:
        plain = plain + decode_char(char, key[i])
        i = i + 1
    return plain.upper()

#fileplain = open('plaintext.txt','r+').read()

#print(encode_text(fileplain,'reza'))