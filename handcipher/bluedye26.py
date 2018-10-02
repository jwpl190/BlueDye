class BlueDye:
    def keysetup(self, key):
        s = range(26)
        k = [0] * len(key)
        keylen = len(key)
        j = 0
        for c, byte in enumerate(key):
            k[c] = (k[c] + (ord(byte) - 65)) % 26
            j = (j + (ord(byte) - 65)) % 26
        for c in range(26):
            k[c % keylen] = (k[c % keylen] + j) % 26
            j = (j + k[c % keylen]) % 26
            s[c], s[j] = s[c], s[j]
        return k, j, s

    def encrypt(self, chars, key):
        ctxt = []
        c = i = 0
        k, j, s = self.keysetup(key)
        keylen = len(k)
        for char in chars:
            k[i] = (k[i] + k[(i + 1) % keylen] + j) % 26
            j = (j + k[i] + c) % 26
            output = (s[j] + k[i]) % 26
            s[c], s[j] = s[j], s[c]
            sub = (output + (ord(char) - 65)) % 26
            ctxt.append(chr(sub + 65))
            c = (c + 1) % 26
            i = (i + 1) % keylen
        return "".join(ctxt)
    
    def decrypt(self, chars, key):
        ctxt = []
        c = i = 0
        k, j, s = self.keysetup(key)
        keylen = len(k)
        for char in chars:
            k[i] = (k[i] + k[(i + 1) % keylen] + j) % 26
            j = (j + k[i] + c) % 26
            output = (s[j] + k[i]) % 26
            s[c], s[j] = s[j], s[c]
            sub = ((ord(char) - 65) - output) % 26
            ctxt.append(chr(sub + 65))
            c = (c + 1) % 26
            i = (i + 1) % keylen
        return "".join(ctxt)
