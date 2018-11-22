# import re
# Name = input("Enter Name: ")
# result = re.match(r'Rajesh', Name)
# print(result.start())
# print(result.end())


import re
str=input('enter the string: ')
res=re.match(r'Sumanth',str)
print(res.start())
print(res.end())