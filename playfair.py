from base64 import encode
import string

def number_to_letter(number):
    return string.ascii_letters[number]

def letter_to_number(char):
    letter = dict(zip(string.ascii_letters,[(ord(c)%32)-1 for c in string.ascii_letters]))
    return letter[char]

def create_key(k):
    k = k.lower()
    k = k.replace(" ",'')
    key = ''
    for char in k:
        if char not in key and char != 'j':
            key = key + char
    for i in range(26):
        if number_to_letter(i) not in key and number_to_letter(i) != 'j':
            key = key + number_to_letter(i)
    keyblock = [[('') for i in range(5)]for j in range(5)]
    x = 0
    for i in range(5):
        for j in range(5):
            keyblock[i][j] = keyblock[i][j] + key[x]
            x = x + 1
    return keyblock

def create_plain(text):
    text = text.replace(" ",'')
    tempplain = []
    plain = ''
    tempchar = ''
    for i in range(len(text)):
        if text[i] == text[i-1]:
            text = text[:i] + 'x' + text[i:]
    if len(text) % 2 == 1:
        text = text + 'x'

    for i in range(0, len(text), 2):
        tempchar = text[i] + text[i+1]
        tempplain.append(tempchar)

    for char in tempplain:
        plain = plain + str(char)

    return plain

def encode_char_plain(text, keyblock):
    i1 = 0
    j1 = 0
    i2 = 0
    j2 = 0
    for i in range(5):
        for j in range(5):
            if(keyblock[i][j] == text[0]):
                i1 = i
                j1 = j
            if(keyblock[i][j] == text[1]):
                i2 = i
                j2 = j
    
    if (i1 == i2):
        j1 = j1+1
        j2 = j2+1
        if (j1==5):
            j1 = 0
        if (j2==5):
            j2 = 0
    elif (j1 == j2):
        i1 = i1+1
        i2 = i2+1
        if (i1==5):
            i1 = 0
        if (i2==5):
            i2 = 0
    elif (i1 != i2 and j1!= j2):
        x1 = i1
        y1 = j2
        x2 = i2
        y2 = j1
        #======
        i1 = x1
        j1 = y1
        i2 = x2
        j2 = y2
    
    char1 = keyblock[i1][j1]
    char2 = keyblock[i2][j2]

    return (char1) + (char2)

def decode_char_cipher(text, keyblock):
    i1 = 0
    j1 = 0
    i2 = 0
    j2 = 0
    for i in range(5):
        for j in range(5):
            if(keyblock[i][j] == text[0]):
                i1 = i
                j1 = j
            if(keyblock[i][j] == text[1]):
                i2 = i
                j2 = j

    if (i1 == i2):
        j1 = j1-1
        j2 = j2-1
        if (j1== (-1)):
            j1 = 4
        if (j2== (-1)):
            j2 = 4
    elif (j1 == j2):
        i1 = i1-1
        i2 = i2-1
        if (i1== (-1)):
            i1 = 4
        if (i2== (-1)):
            i2 = 4
    elif (i1 != i2 and j1!= j2):
        x1 = i1
        y1 = j2
        x2 = i2
        y2 = j1
        #======
        i1 = x1
        j1 = y1
        i2 = x2
        j2 = y2
    
    char1 = keyblock[i1][j1]
    char2 = keyblock[i2][j2]

    return (char1) + (char2)

def encode_text(text,keyblock):
    text = text.lower()
    plaintext = create_plain(text)
    ciphertext = ''
    k = 0
    for i in range(0, len(plaintext), 2):
        k = k + 2
        if i == len(plaintext)-1 :
            ciphertext = ciphertext + encode_char_plain(plaintext[i]+plaintext[i+1],keyblock)
        elif k == 4:
            ciphertext = ciphertext + encode_char_plain(plaintext[i]+plaintext[i+1],keyblock) + " "
            k = 0
        else:
            ciphertext = ciphertext + encode_char_plain(plaintext[i]+plaintext[i+1],keyblock)
    return ciphertext.upper()

def decode_text(text,keyblock):
    ciphertext = text.replace(" ",'').lower()
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        plaintext = plaintext + decode_char_cipher(ciphertext[i]+ciphertext[i+1],keyblock)
    plaintext = plaintext.replace("x",'')
    return plaintext.upper()

keyblock = create_key("JALAN GANESHA SEPULUH")

fileplaintext = open('ciphertext.txt','r')
plaintext = fileplaintext.read()

print(decode_text(plaintext,keyblock))
