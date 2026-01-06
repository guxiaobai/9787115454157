"""
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)
"""


# 1.2.1 模拟数值类型
class Vector:

  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return 'Vector(%r, %r)' % (self.x, self.y)

  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)