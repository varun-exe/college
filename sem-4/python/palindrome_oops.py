class palindrome_checker:
    def __init__(self,value):
        self.value=value
    def is_palindrome(self):
        pass

class strcheck(palindrome_checker):
    def is_palindrome(self):
        pal_str=''.join(self.value.split()).lower()
        return pal_str==pal_str[::-1]

class intcheck(palindrome_checker):
    def is_palindrome(self):
        int_str=str(self.value)
        return int_str==int_str[::-1]

a=input("enter string or integer")
if a.isdigit():
    res=intcheck(int(a))
else:
    res=strcheck(a)

if res.is_palindrome():
    print(f"{a} is a palindrome")
else:
    print(f"{a} is not a palindrome")
