# BlueDye Cipher
BlueDye was designed to overcome the weaknesses in the RedDye cipher.  It uses the same keystream generator as RedDye and maintains two states, one for the keystream and the other for a 256 byte substition array.  Because of the addition of the 256 byte substition array it resembles the RC4 construction a bit.

The RedDye key stream generator was tested under dieharder and NIST STS and did not fail.  Since the RedDye generator cannot be distinguished from a random output it was selected to combine with BlueDye's 256 substition array to create BlueDye which also passes the same testing.

The keysetup starts by operating on each byte of the key, adding each byte to the key array and suming all of the bytes mod 256 to give us "j".  Then for 768 rounds the substitution state is shuffled by swapping a counter and j.  If a nonce is used then the process is repeated one more time.

Key generator operates using the following equation to encrypt and decrypt:

k[i] = (k[i] + k[(i + 1) % keylen] + j) % 256
j = (j + k[i] + c) % 256
swap(s[c], s[j])
output = s[j] ^ k[i]

The output is XOR'd with the input byte.  i is a second counter that operates mod the key length.  In the case that the key is 2048 bits in length no second counter is necessary and performance is boosted.

# Cryptanalysis

BlueDye's output cannot be distinguished from a truly random source.  There is no known attack vector against the cipher.  BlueDye holds its ground under known plaintext attack situations.

# BlueDye as a Hand Cipher
(implemented in python as RedDye26)

BlueDye run as a hand cipher is a little time consuming because one has to maintain the 26 character state at all times.  This can be represented by half a deck of cards or written on paper.  In this example we'll use half a deck of cards(26 cards).

First one arranges the deck of cards in order from 0 to 25.  This will represent letters A to Z, respectively.  For this example, we'll use the word TESTING as the key and HELPMESOS as the message.  Convert TESTING to numbers.

19, 4, 18, 19, 8, 13, 6

Then you sum all the characters in the key to give you "j".

19 + 4 + 18 + 19 + 8 + 13 + 6 mod 26 = 9

Next, for 26 iterations you perform the following algorithm:

key[c] = key[c] + j
j = (j + key[c] + c)
then you swap the counter (c) card with the j card.

The resulting 26 letter state will be:

[6, 5, 23, 10, 2, 18, 7, 12, 15, 11, 0, 14, 19, 25, 4, 8, 17, 22, 20, 9, 21, 24, 3, 16, 13, 1]

and j will be 20

Encryption:

To encrypt a single letter one uses the following algorithm.  First line, modifies the key, the second modifies j, and the third creates the output letter which is added to the input letter.  The counter i is mod keylength and counter c is mod 26.

key[i] = (k[i] + k[(i + 1) % keylength] + j) % 26
j = (j + k[i] + c) % 26
output = (s[j] + k[i]) % 26
swap(s[c] and s[j])
result = (input +  output) % 26
c = (c + 1) % 26
i = (i + 1) % keylength

First we convert our message to numbers
H E L P M E S O S
7 4 11 15 12 4 18 14 18

Then we run each letter through the encryption algorithm.

RESULT

TIDXHCLRHD

Decryption:

Decryption is performed exactly the same as encryption except this time output is subtracted from intput.

result = (input - output) % 26

