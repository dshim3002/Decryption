# download the reference text
# and clean the data
# (remove punctuations and lower cases)
def text():
    # ref = {}
    # define puctuation
    punc = '''!()-[]{};:'",<>./?@#$%^&*_~/'''
    f = open("./reference.txt", "r")
    f2 = open("./ref2.txt", "w")
    temp = ""
    while True:
        letter = f.read(1).lower()
        # at end of the file,
        # break out of while loop
        if letter == "":
            break
        # remove punctuation
        elif letter in punc:
            letter = ""
        # substitute "\n" to a space
        elif letter == "\n":
            letter = " "
        # if more than one space,
        # skip to the next step
        if letter == " ":
            if temp == " ":
                continue
        temp = letter
        f2.write(letter)
    f.close()
    f2.close()


# create a dictionary with letter pairs
# from the reference text
def dict(ref):
    dict = {}
    for i in range(len(ref)):
        # for two consecutive letters in the reference text
        # set is as a key
        # if the key does not already exist in the dictionary,
        # put it into the dictionary
        # if it exists, add 1 to the count
        key = ref[i:i+2]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] += 1
    return(dict)
