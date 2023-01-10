import numpy as np
from decrypt import swap, encrypt, decrypt, score
from data_clean import dict

# prepare by calling encrypted text
# from the some_text_encrypt.txt file
enc = encrypt()
# initialize decryption key, d
d = "abcdefghijklmnopqrstuvwxyz"

# prepare the reference text
# from ref2.txt (from the book)
ref2 = ""
f = open("./ref2.txt", "r")
for line in f:
    ref2 += line
f.close()

# derive reference dictionary
# from ref2
dict = dict(ref2)


# use Markov chain to derive
# optimal decryption key
def mcmc(d, p):
    # set iteration to happen
    # 10,000 times
    iter = 10000
    # run while loop to derive
    # the optimal decyption key
    # for 10,000 times
    while iter != 0:
        # create a random variable
        # from the uniform distribution
        # to add randomness in comparison
        # between d and dprime
        u = np.random.uniform()
        # create dprime using
        # pre-defined swap function
        dprime = swap(d)
        # caculate score with
        # current decryption key, d
        d_score = score(decrypt(enc, d), dict)
        # caculate score with
        # modified(swapped) decryption key, dprime
        dp_score = score(decrypt(enc, dprime), dict)
        # compare the scores and choose final d
        if u < np.exp(p*(dp_score - d_score)):
            d = dprime
        iter -= 1
    # return the final decryption key, d
    return d


# derive optimal decryption key
# with p = 0.5
d_fin = mcmc(d, 0.5)
print(d_fin)

# finally, decrypt the text
final = decrypt(enc, d_fin)
# print the output
print(final)
