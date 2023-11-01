import re
def is_phone_number(s):
    phone=r"\d{3}[-]{1}\d{3}[-]{1}\d{4}"
    if re.match(phone,s):
        print(f"{s} is a phone number")
    else:
        print(f"{s} is not a phone number")

def is_email(e):
    email=r"[\w-]+@+[\w-]+.com\b"
    if re.match(email,e):
        print(f"{e} is an email id")
    else:
        print(f"{e} is not an email id")



file=open("../web/samp.txt", "r")
for line in file:
    for word in line.split():
        is_phone_number(word)
        is_email(word)
file.close()
