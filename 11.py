import re
wish = "Hello everybody"
res = re.findall(r".", wish)
print(res)

print("************************************")

import re
wish = "Hello everybody"
res = re.findall(".", wish)
print(res)

print("************************************")

import re
wish = "Hello everybody"
res = re.findall(r"\.", wish)
print(res)
