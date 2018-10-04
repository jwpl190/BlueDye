#ifndef bluedye_h__
#define bluedye_h__

unsigned char * crypt(unsigned char *data, unsigned char *key, unsigned char *nonce, long datalen);

//unsigned char * kdf(unsigned char *password, unsigned char *key, unsigned char *salt, int iterations, int keylen);

unsigned char * bluedye_random (unsigned char *buf, int num_bytes);

#endif 
