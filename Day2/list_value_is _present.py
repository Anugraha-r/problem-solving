#Write a Python program to check if a given value is present in a list.

list=[2,10,12,8,5]
given_value=1
for i in list:
    if given_value==i:
        print("value is present")
    else:
        print("not present")
        break