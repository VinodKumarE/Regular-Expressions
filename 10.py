import re
wish = "Hello everybody"
res = re.findall(r"\w", wish)
print(res)

print("************************************")

import re
wish = "Hello everybody"
res = re.findall("\w", wish)
print(res)

print("************************************")

import re
wish = "Hello everybody"
res = re.findall("w", wish)
print(res)