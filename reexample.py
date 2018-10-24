import re

s2 = "+91-6123456789"
# s2 = "6123456789"

r2 = re.compile("^(\+91-)?([6-9][0-9]{9})$")

m = re.search(r2,s2)
if m:
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
else:
    print("Invalid number")
