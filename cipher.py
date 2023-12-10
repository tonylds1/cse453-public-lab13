##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, Tony Moraes
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        pass

    def get_author(self):
        # TODO: Return your name
        return "Tony Moraes"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "RC4 (Rivest Cipher 4)"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        s = "https://www.geeksforgeeks.org (06 december, 2021), " \
            "\"What is RC4 Encryption?\', \n   retrieved: " \
            "https://www.geeksforgeeks.org/what-is-rc4-encryption/"
        return s

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
         # The encrypt pseudocode
        pc = "encrypt(plainText, password)\n" \
            "   plaintext = [ord(char) for char in plaintext]\n" \
            "   password = [ord(char) for char in password]\n" \
            "   s_box = substitution_box(password)\n" \
            "   password_stream = stream_generation(s_box)\n" \
            "   ciphertext = ''\n" \
            "   for char in plaintext:\n" \
            "       enc = str(hex(char ^ next(password_stream))).upper()\n" \
            "       ciphertext += enc\n" \
            "   return ciphertext\n\n" 
                
        # The decrypt pseudocode
        pc += "decrypt(cipherText, password)\n" \
            "   ciphertext = ciphertext.split('0X')[1:]\n" \
            "   ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]\n" \
            "   password = [ord(char) for char in password]\n" \
            "   s_box = substitution_box(password)\n" \
            "   password_stream = stream_generation(s_box)\n" \
            "   plaintext = ''\n" \
            "   for char in ciphertext:\n" \
            "       dec = str(chr(char ^ next(password_stream)))\n" \
            "       plaintext += dec\n" \
            "   return plaintext\n\n" 

        # helper routines
        pc += "substitution_box(password):\n" \
            "   s_box = [i for i in range(0, 256)]\n" \
            "   i = 0\n" \
            "   password_size = len(password)\n" \
            "   for j in range(0, 256):\n" \
            "       i = (i + s_box[j] + password[j % password_size]) % 256\n" \
            "       s_box[j], s_box[i] = s_box[i], s_box[j]\n" \
            "   return s_box\n\n"

        pc += "stream_generation(s_box):\n" \
            "   i = 0\n" \
            "   j = 0\n" \
            "   while True:\n" \
            "       i = (1 + i) % 256\n" \
            "       j = (s_box[i] + j) % 256\n" \
            "       s_box[i], s_box[j] = s_box[j], s_box[i]\n" \
            "       yield s_box[(s_box[i] + s_box[j]) % 256]\n\n" 

        return pc

    ##########################################################################
    # ENCRYPT
    # The encrypt function converts the input text and password into lists of ASCII 
    # values, initializes the substitution-box with the password, generates a key stream, 
    # and then XORs each character of the text with the corresponding byte 
    # from the password stream, converting the result to hexadecimal.
    ##########################################################################
    def encrypt(self, plaintext, password):
        plaintext = [ord(char) for char in plaintext]
        password = [ord(char) for char in password]
        s_box = self.substitution_box(password)
        password_stream = self.stream_generation(s_box)
        ciphertext = ''
        for char in plaintext:
            enc = str(hex(char ^ next(password_stream))).upper()
            ciphertext += enc
        
        return ciphertext

    ##########################################################################
    # DECRYPT
    # The decrypt function reverses the process by converting the hexadecimal 
    # ciphertext back to integers, initializing the substitution-box with the 
    # password, generating the password stream, and then XORing each character
    # of the ciphertext with the corresponding byte from the password stream.
    ##########################################################################
    def decrypt(self, ciphertext, password):
        ciphertext = ciphertext.split('0X')[1:]
        ciphertext = [int('0x' + c.lower(), 0) for c in ciphertext]
        password = [ord(char) for char in password]
        s_box = self.substitution_box(password)
        password_stream = self.stream_generation(s_box)
        plaintext = ''
        for char in ciphertext:
            dec = str(chr(char ^ next(password_stream)))
            plaintext += dec

        return plaintext

    ##########################################################################
    # DECRYPT
    # This function create the substitution box and then performs a substitution 
    # algorithm to shuffle it based on the provided key. 
    ##########################################################################
    def substitution_box(self, password):
        s_box = [i for i in range(0, 256)]
        i = 0
        password_size = len(password)
        for j in range(0, 256):
            i = (i + s_box[j] + password[j % password_size]) % 256
            s_box[j], s_box[i] = s_box[i], s_box[j]
        return s_box

    ##########################################################################
    # DECRYPT
    # This function generates a pseudo-random key stream by continuously 
    # shuffling the substitution box
    ##########################################################################
    def stream_generation(self, s_box):
        i = 0
        j = 0
        while True:
            i = (1 + i) % 256
            j = (s_box[i] + j) % 256
            s_box[i], s_box[j] = s_box[j], s_box[i]
            yield s_box[(s_box[i] + s_box[j]) % 256]