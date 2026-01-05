'''
用于演示 namedtuple 的使用

namedtuple是tuple的擴展，因為namedtuple在使用上可以透過類似讀取欄位(field)名稱的方式，
來取用tuple不同的item資料，所以有時候namedtuple就很適合用來代替tuple儲存資料


## Ref
 - [使用collections中的namedtuple來操作簡單的物件結構 | Drake's](https://qiubite31.github.io/2017/03/02/%E4%BD%BF%E7%94%A8collections%E4%B8%AD%E7%9A%84namedtuple%E4%BE%86%E6%93%8D%E4%BD%9C%E7%B0%A1%E5%96%AE%E7%9A%84%E7%89%A9%E4%BB%B6%E7%B5%90%E6%A7%8B/)
 - <https://docs.python.org/3/library/collections.html>

'''
from collections import namedtuple


# namedtuple是tuple的擴展，因為namedtuple在使用上可以透過類似讀取欄位(field)名稱的方式，
# 來取用tuple不同的item資料，所以有時候namedtuple就很適合用來代替tuple儲存資料

Point = namedtuple('Point', 'x,y')

s1 = Point(12, 15)

print(s1[0])
print(s1.y)
