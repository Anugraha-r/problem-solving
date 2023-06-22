#Write a Python program to check if a list is sorted in ascending order.
list=[4,5,2,8,6]
list.sort()
print("sorted order="+str(list))
for i in list:
    if list[i]<list[i+1]:
        print("list is in ascending order")
        break
   