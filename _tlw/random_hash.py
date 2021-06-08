"""Note: this requires bcrypt to be installed"""
import bcrypt
password = input("Enter a password: ")
bpassword = password.encode()
#https://pypi.org/project/bcrypt/
hashed = bcrypt.hashpw(bpassword,bcrypt.gensalt())
print(hashed)
if bcrypt.checkpw(bpassword, hashed):
  print("It Matches!")
else:
  print("It Does not Match :(")
