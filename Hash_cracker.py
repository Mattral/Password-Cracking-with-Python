import os
import hashlib

input_hash = input("Enter md5 hash of victim: ")

try:
   pass_file = open("10-million-password-list-top-1000000.txt", "r")
except:
   print("Password file not opened")
   quit()

for password in pass_file:
   password = password.replace("\n","")
   enc = password.encode('utf-8')
   digest = hashlib.md5(enc.strip()).hexdigest()

   print("password " + password + " = " + digest)

   if input_hash == digest:
       print("password is found")
       print("password is " + password)
       break
