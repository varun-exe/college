filename=input("enter the filename: ")
file=open(filename,"r")
n=int(input("enter number of lines to be displayed: "))
for i in range(n):
    line=file.readline();
    print(line)

file.seek(0)
word=input("enter the word to be searched: ")
count=0;
for line in file:
    if word in line:
        count+=1
print(f"the word {word} appears {count} times!")
