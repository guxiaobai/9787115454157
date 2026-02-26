'''
for 循环知道如何获取元组中单独的每一项，这叫“拆包”
'''

traveler_ids = [('usa', '31'), ('BRA', 'CE')]

for country, _ in traveler_ids:
  print(country)