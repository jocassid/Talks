
from java.util import ArrayList

import sys

arr = ArrayList()
arr.add(1)
arr.add(2)

print("ArrayList contains %s elements" % arr.size())

for i in arr:
    print(i)

print(dir(arr))

print(sys.version)
print(sys.version_info)


