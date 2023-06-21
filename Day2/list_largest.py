#Write a Python program to find the largest element in a given list
list=[2,10,12,8,5]
temp=0
for i in list:
    for j in list:
        if i>j:
            temp=i
            i=j
            j=temp
        