import os

try:
   pass_file = open("10-million-password-list-top-1000000.txt", "r")
except:
   print("Password file not opened")
   quit()

for password in pass_file:
    password = password.replace("\n","")
    cmd = "unzip -P " + password + " secret.zip"
    print(cmd)

    os.system(cmd)
