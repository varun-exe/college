num_list=[]
n=int(input("enter number of elements: "))
for i in range(n):
    num=int(input("enter the elements: "))
    num_list.append(num)
for i in range(1,n):
    picked=num_list[i]
    j=i
    while j>0 and picked<num_list[j-1]:
        num_list[j]=num_list[j-1]
        j-=1
        num_list[j]=picked
print("sorted array is:")
for i in range(n):
    print(num_list[i],end=" ")
