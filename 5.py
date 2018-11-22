import regex
Name = input("Enter Name : ")
result = regex.findall(r"vinod", Name)
print(result)