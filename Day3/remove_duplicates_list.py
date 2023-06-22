
#Write a Python program to remove duplicates from a list
list= [1,3,4,5,6,9,3]
new_list=[]

for num in list:
	if num not in new_list:
		new_list.append(num)
print(new_list)

