# Statistical-Computing

Markov chain Monte Carlo (MCMC) samplers are algorithms that enable you to sample values from a probability distribution that is only known up to a normalization constant. In this project, I implemented MCMC sampler for decrypting encrypted text as described in this publication: J. Chen and J. S. Rosenthal, Decrypting classical cipher text using Markov chain Monte Carlo, Statistics and Computing 22, 397–413, 2012.

Specifically, in this Github there are three main components: data_clean.py, decrypt.py, and mcmc.py

### Steps to implement mcmc decrytion methodology:
1. Run mcmc.py file with relevant reference text and decryption key (for testing, they are provided in this Github repository). The mcmc.py file consists of all required information to execute the process (all previous data cleaning and decryption will be done automatically through the imported functions from data_clean.py, decrypt.py). The user only has to download the entire repository and run the mcmc.py file.

The detailed information for the files in this Github is as follows: 

### data_clean.py
In this file, we import the any .txt file (e.g., excerpts from English literature) and clean it so that it would be easy to process in the system (get rid of punctuations, turn all letters to lowercase, etc.)

### decrypt.py
Decrypt.py allows you to decrypt the cleaned text file with the provided decryption key (which is derived from mcmc.py)

### mcmc.py
Based on the reference text we imported, mcmc.py trains the program so that it can find the ideal decryption key that adheres to the NLP (Natural Language Processing). Once we determine the most effective decryption key, we apply it to the sample text (also provided in the repository). Finally we acquire a decrypted text, which turns out to be an excerpt from "Alice in Wonderland"

*Disclaimer: The user may have to run mcmc.py file twice or more to allow the system to be trained properly.
