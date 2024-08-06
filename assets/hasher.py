import hashlib,base64,os
defaultHash = "c4ca4238a0b923820dcc509a6f75849b"

def hasher(stri :str):
    k = stri.encode('utf-8')
    string = hashlib.md5(stri.encode("utf-8")).hexdigest()
    return string



def cget():
    if os.path.exists("hash.txt"):
        with open("hash.txt","r") as geth:
            s = decipher(geth.read().strip())
            print(s)
            if s != '':
                
                return s
            else:
                with open('hash.txt','w') as gets:
                    gets.write(cipher(defaultHash))
                    return defaultHash
    else:
        with open('hash.txt','w') as gets:
            gets.write(cipher(defaultHash))
            return defaultHash
def check(hash:str):
    
    if hash == "":
        return None
    elif hashlib.md5(hash.encode('utf-8')).hexdigest() == cget():# You can set your OWN HASH here
        return True
    else:
        return False
         
# Ciphers a String   
def cipher(code:str):
    # What The Hell IS THIS~!
    text = code.encode('utf-8')
    encode1 =base64.b32encode(text)
    encode2 = base64.b64encode(encode1)
    string = encode2.decode()
    encode3 = ' '.join(format(ord(c), '08b') for c in string) # changes to binary
    final = base64.b32encode(encode3.encode('utf-8'))
    return final.decode()
def decipher(code :str):
# Deciphers a String 
    text = code.encode('utf-8')
    decoded = base64.b32decode(text)
    binary_values = decoded.decode().split(' ')
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values] # Deciphers From Binary to 
    decoded2 =''.join(ascii_characters)
    decoded3 = base64.b64decode(decoded2)
    final = base64.b32decode(decoded3)
    return final.decode()
if __name__ == "__main__":
    cget()
   