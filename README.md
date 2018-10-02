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
(see also implementation in python)


