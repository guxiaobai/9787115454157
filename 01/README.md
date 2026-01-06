# 第 1 章 Python数据模型

|本期版本|上期版本 
|:---:|:---:
`Tue Jan  6 11:42:39 CST 2026` | -

- Python 最好的品质之一是一致性。
- Python风格(Pythonic)
- 特殊方法的名字以两个下划线开头，以两个下划线结尾

## 1.1 一摞 Python 风格的纸牌


## 1.2 如何使用特殊方法

* 特殊方法的存在是为了被 Python 解释器调用的， 你自己并不需要调用它们
* [doctest 用法简介 | Yunfeng's Simple Blog](https://vra.github.io/2021/02/02/doctest-intro/)


**1.2.2 字符串表示形式**

* 有一个内置的函数叫 `repr` ，它能把一个对象用字符串的形式表达出来以便辨认，这 就是“字符串表示形式”
* repr 就是通过 __repr__ 这个特殊方法来得到一个对象的字符串 表示形式的
* 和 __str__ 的区别在于， 后者是在 str() 函数被使用， 或是在用 print函数 一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。

> __repr__ 是更好的选择，因为如果一个对象没有__str__函数，而Python又需要调用的它的时候，解释器会用__repr__作为替代

**1.2.4 　自定义的布尔值**

* 会调用bool(x), 这个函数只能返回True或者False
* bool(x) 的背后是调用 x.__bool__() 的结果
* 如果不存在 __ bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()
* 有一节 “Built-in Types" (<https://docs.python.org/3/library/stdtypes.html#truth-value-testing>)，其中规定了真值检验的标准

## 1.3 特殊方法一览

语言参考手册中的 `Data Model` <https://docs.python.org/3/reference/datamodel.html>


## Ref

- [Python 中 __name__ 有什么用](https://www.freecod