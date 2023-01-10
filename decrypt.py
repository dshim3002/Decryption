import numpy as np
import string

d = "abcdefghijklmnopqrstuvwxyz"


# swap the randomly selected letters in key d
# to derive d prime
def swap(d):
    # final list to store dprime
    # since str assignment is not supported by Python
    # we create a separate list
    dprime = []
    # create an empty string
    # to return the final dprime output
    str = ""
    # append decryption key d into the list
    for i in range(len(d)):
        dprime.append(d[i])
    # assign two random numbers
    # these are within the range
    # of the length of d
    rand_a = np.random.randint(0, len(dprime))
    rand_b = np.random.randint(0, len(dprime))
    # store the first letter
    # (from the first random index value)
    # into temp (so that we would not lose it)
    temp = dprime[rand_a]
    # replace the first letter to the second letter
    dprime[rand_a] = dprime[rand_b]
    # replace the second letter to the first letter
    dprime[rand_b] = temp
    # after successful swap,
    # change to string format
    for i in range(len(dprime)):
        str += dprime[i]
    # return the final output
    return str


# put string decryption key "d" into a list
def dlist(d):
    # create a dictionary to store decryption keys
    dlist = {}
    # put d (key) into a dictionary
    chars = tuple(string.ascii_lowercase + '')
    dlist = dict(zip(chars, tuple(d)))
    return dlist


# put an encrypted text
# into a string format
def encrypt():
    # create an empty string
    # to store encrypted text from .txt file
    encrypt = ""
    # open .txt file in a read format
    f = open("./some_text_encrypt.txt", "r")
    # for every line in the file
    # add the line to the empty string, encrypt
    for line in f:
        encrypt += line
    f.close()
    # return the output
    return(encrypt)


# decrypt an encrypted text
# based on a decryption key, d
def decrypt(enc, d):
    # create an empty string
    # to store decrypted text
    # using the decryption key, d
    decrypt = ""
    # change d into a dictionary format
    # to easily access the corresponding decryption value
    dkey = dlist(d)
    # decrypt the encrypted text
    for i in range(len(enc)):
        # if not space (letter),
        # get value (decrypted letter)
        # from the dictionary
        if enc[i] != " ":
            # every time in the loop
            # create an empty string
            # to appropriately call the keys
            # (since all keys are in str format)
            str = ""
            # put each letter in encrypted file
            # into a string format
            val = str + enc[i]
            # find value from the dictionary
            valplus = dkey[val]
            # append to the final decrypted text
            decrypt += valplus
        else:
            # if space, append space
            decrypt += " "
    # return the decrypted text
    return decrypt


# return the score of the decrypted text
def score(decrypt, dict):
    # initially set score = 0
    score = 0
    # check how many times a pair in the decrypted text
    # appear in the dictionary
    for i in range(len(decrypt)):
        key = decrypt[i:i+2]
        if key in dict:
            score += np.log(dict[key])
    return score
