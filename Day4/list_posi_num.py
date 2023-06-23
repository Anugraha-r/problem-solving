#Write a Python program that takes a list of numbers as input and returns a new list containing only the positive numbers.
list=[2,3,4,6,8]
pos_list=[]
for i in list:
    if (i%2==0):
        pos_list.append(i)
print(pos_list)

