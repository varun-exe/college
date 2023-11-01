def is_phone_number(s):
    # Check if the string has the correct length
    if len(s) != 12:
        print(f"{s} is not a phone number!")
        return
    flag=0
    for i in range(0,3):
        if not s[i].isdigit():
            flag=1
    for i in range(4,7):
        if not s[i].isdigit():
            flag=1
    for i in range(8,12):
        if not s[i].isdigit():
            flag=1
    if not s[3]=='-' and not s[7]=='-':
        flag=1
    if flag==1:
        print(f"{s} is not a phone number!")
    else:
        print(f"{s} is a phone number!")

ph=input("enter phone number: ")
is_phone_number(ph)

