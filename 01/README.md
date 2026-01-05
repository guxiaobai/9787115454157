# 第 1 章 Python数据模型

|本期版本|上期版本 
|:---:|:---:
`Sun Jan  4 23:13:11 CST 2026` | -


## 1.3 如何使用特殊方法

* 特殊方法的存在是为了被 Python 解释器调用的， 你自己并不需要调用它们
* [doctest 用法简介 | Yunfeng's Simple Blog](https://vra.github.io/2021/02/02/doctest-intro/)


**1.3.2 字符串表示形式**

* 有一个内置的函数叫 repr ，它能把一个对象用字符串的形式表达出来以便辨认，这 就是“字符串表示形式”
* repr 就是通过 __repr__ 这个特殊方法来得到一个对象的字符串 表示形式的
* 和 __str__ 的区别在于， 后者是在 str() 函数被使用， 或是在用 一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。print函数

**1.3.3 　自定义的布尔值**

* bool(x) 的背后是调用 x.__bool__() 的结果
* 如果不存在 __ bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()




## 1.6 延伸阅读



* <https://docs.python.org/3/reference/datamodel.html>


## Ref

- [Python 中 __name__ 有什么用](https://www.freecod