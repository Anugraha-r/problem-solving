#Given two lists, write a Python program to find the common elements between them
a=[1,2,3,4]
b=[4,5,2,7]
cmn_ele_lis=[]
for i in a:
    for j in b:
        if i==j:
             cmn_ele_lis.append(i)
print(cmn_ele_lis)
        