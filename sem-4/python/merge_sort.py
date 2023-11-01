def mergesort(nlist):
    print("splitting", nlist)
    if len(nlist) > 1:
        mid = (len(nlist) // 2)
        left = nlist[:mid]
        right = nlist[mid:]
        mergesort(left)
        mergesort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nlist[k] = left[i]
                i = i + 1
            else:
                nlist[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            nlist[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            nlist[k] = right[j]
            j = j + 1
            k = k + 1
        print("merging", nlist)


nlist = []
n = int(input("enter number of elements: "))
for i in range(n):
    ele = int(input("enter the elements :"))
    nlist.append(ele)
mergesort(nlist)
print(nlist)
