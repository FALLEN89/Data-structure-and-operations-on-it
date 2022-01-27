'''
Operation on arrays using python
list in python = arr[] in other languages
'''
#indexing
new_list=[1, 2, 3]
result= new_list[0]
#loops for arrays
if 1 in new_list:print(True)

for i in new_list:
    if i==1:
        print(True)
    break
#insertanddelete
numbers=[]
print(len(numbers))
numbers.insert(0,23)
numbers.append(89)
numbers.__delitem__(0)
print(len(numbers))
print(numbers)
