import regex
PinNo = input("Enter Number : ")
Access = regex.match(r"5421", PinNo)
if Access == "5421":
    print("Access Granted", Access)
else:
    print("Access Not Granted")
