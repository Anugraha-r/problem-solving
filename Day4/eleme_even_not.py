#Given a list of numbers, write a Python program to check if all the elements are even.
list=[2,4,7,6]
new_list=[]
for i in list:
    if (i%2==0):
        new_list.append(i)
    else:
        print("not all numbers are even")
    