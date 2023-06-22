#Write a Python program to find the largest element in a given list.
list=[24,13,2,16,1]
list.sort()
list_len=len(list)
larg_elem=list[list_len-1]
print(list)
print("large is="+str(larg_elem))
