import rsa

publicKey, privateKey = rsa.newkeys(1024) 

def WriteKeyToFile(fileName, mode, key, fileType):
   with open(fileName, mode) as f:
    f.write(key.save_pkcs1(fileType))

WriteKeyToFile("public.pem", "wb", publicKey, "PEM")
WriteKeyToFile("private.pem", "wb", privateKey, "PEM")