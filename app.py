import re
import hashlib 
import random 
import string 

print("===== Secure Password Analyzer =====")

password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[0-9]", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

    password_hash = hashlib.sha256(password.encode()).hexdigest()
print("SHA-256 Hash:", password_hash)

characters = string.ascii_letters + string.digits + "!@#$%^&*"

generated_password = ""

for i in range(12):
    generated_password += random.choice(characters)

print("Suggested Strong Password:", generated_password)