import numpy as np


# reading the ciphertext into cipher_text
with open('Ciphertext.txt') as f:
    cipher_text = f.read()

f.close()

#freq analysis by passing in the cipher:
def freq_analysis(cipher):
    freqs = {}
    
    for i in cipher:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1

    most_freq = max(freqs, key = freqs.get)

    return most_freq


#create chunks by passing in text:
def chunking(text):
    chunks = {}
    i = 0


    for x in range(0, len(text), 6):
        chunks[i] = text[x:x+6]
        i += 1

    #print(chunks)

    return chunks

#finding the key
def find_key(chunks):

    #first we group together the first letters of each chunk

    #a list of the chars in each pos of all chunks. pos1,pos2...pos6
    keychars = [''] * 6

    #we have 6 characters in each chunk, we will split them up in into 6 strings, string 1 has 1st char of each chunk, string 2 has 2nd and so on
    for i in range(len(chunks)):
        for j in range(len(chunks[i])):
            keychars[j] = keychars[j] + chunks[i][j]

    keyoffset = {}

    for i in range(6):
        keyoffset[i] = ( ( ord(freq_analysis(keychars[i])) - ord('e') + 26 ) % 26 ) + ord('a')

    #print(keyoffset)

    secretKey = ''

    for i in range(6):
        secretKey = secretKey + chr(keyoffset[i])

    print("The key is: ")
    print(secretKey)

    return secretKey

def decipher(secretKey, chunks):
    
    plain = ''

    for h in range(len(chunks)):
        temp = ''
        for i in range(len(chunks[h])):
            dum = ( (ord(chunks[h][i]) - ord(secretKey[i]) + 26) % 26) + ord('a')

            temp = temp + chr(dum)
    
        plain = plain + temp

    print("The plain text is:")        
    print(plain)


chunked = chunking(cipher_text)
secret_key = find_key(chunked)
decipher(secret_key, chunked)


#print(split)
