import re
Machine = "This is a Robot"
output = re.split(r's', Machine, maxsplit=1)
print(output)
