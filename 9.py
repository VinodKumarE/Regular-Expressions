import re
wish = "Hello everyone"
res = re.findall(r"\W", wish)
print(res)

print("************************************")

import re
wish = "Hello everyone"
res = re.findall("\W", wish)
print(res)

print("************************************")

import re
wish = "Hello everyone"
res = re.findall("W", wish)
print(res)