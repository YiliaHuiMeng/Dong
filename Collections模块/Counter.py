#!/usr/bin/env python3
from collections import Counter
import re
path = '/usr/lib/python3.4/LICENSE.txt'
word = re.findall('\w+',open(path).read().lower())
print(Counter(word).most_common(10))
c = Counter(a=4,b=2,c=0,d=2)
print(c.elements())
print(Counter('abracadabra').most_common(3))
