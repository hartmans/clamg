from . import unpack
from yaml import safe_load

src = '''
obj:
  attr1:
    - item1
    - item2
    - item3
  attr2:
    sub_attr_a: '42'
    sub_attr_b: 'foo'
'''

o = unpack(safe_load(src))

print(o)
