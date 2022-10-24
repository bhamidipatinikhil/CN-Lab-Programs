from DesAlgorithm import *




lock = "top_secret"
text= "Hello wo"
d = des()
r = d.encrypt(lock,text)
r2 = d.decrypt(lock,r)
print("Ciphered: %r" %r)
print("Deciphered: ", r2)