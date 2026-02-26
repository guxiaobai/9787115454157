symbols = '$%^&*'
# 如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围 起来
tuple(ord(symbol) for symbol in symbols)


# 利用生成器表达式实现了一个笛卡尔积
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
  