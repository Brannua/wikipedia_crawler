# wikipedia_crawler

> A demo to practise my python skill learning on udacity.

### A problem solver

```
repeat:

    try it the slow way to understand what you are trying to achieve
    do some learning

    break up the problem into steps
    choose dataStructures、controlFlows、...
    write down your pseudo-code

    write code & test code
    remember to look up documentation
```

### Some notes

Learn from [udacity](https://www.udacity.com/), teacher: [Juno Lee](https://www.linkedin.com/in/junoleelj).

本课程包含（视频、文档、测验、代码练习）所以这里只记录我认为重要的东西

代码风格指南：[PEP8](https://www.python.org/dev/peps/pep-0008/)

### 算术运算符

加减乘除和 % 都没什么好说的

取幂用的是 `**`，而非 ^，在 python 中，^ 是按位 XOR

`//` 相除后向下取整到最接近的整数，**Notice it rounds down even if the answer is negative !**

![20230218100433](https://aliyun-oss-lpj.oss-cn-qingdao.aliyuncs.com/images/by-clipboard/20230218100433.png)

### 变量

推荐的命名方式：`views_per_day`

`del` 是 python 中的保留字

---

python 不用写 ; 和 {}

### 浮点数

A float is a real number that uses a decimal point to allow numbers with fractional values.

**Even if one integer divides another exactly, the result will be a float !**

![20230218115408](https://aliyun-oss-lpj.oss-cn-qingdao.aliyuncs.com/images/by-clipboard/20230218115408.png)

---

In python, every object you encounter will have a type. An object's type defines which operators and functions will work on that object and how they work.

![20230218120150](https://aliyun-oss-lpj.oss-cn-qingdao.aliyuncs.com/images/by-clipboard/20230218120150.png)

---

To make an **int**, just give a whole number without a decimal point.

![20230218120645](https://aliyun-oss-lpj.oss-cn-qingdao.aliyuncs.com/images/by-clipboard/20230218120645.png)

To make a **float**, **include a decimal point !**

If the number itself is actually a whole number, that's okay, you don't even have to put anything after the decimal point.

![20230218120913](https://aliyun-oss-lpj.oss-cn-qingdao.aliyuncs.com/images/by-clipboard/20230218120913.png)

---

Floating-point numbers are approximations.

    This is necessary because floats can represent an enormous range of numbers.

    So, in order to fit numbers in computer memory, python must use approximations.

![20230218123012](https://aliyun-oss-lpj.oss-cn-qingdao.aliyuncs.com/images/by-clipboard/20230218123012.png)

![20230218123535](https://aliyun-oss-lpj.oss-cn-qingdao.aliyuncs.com/images/by-clipboard/20230218123535.png)

### 布尔数据类型

True: 1、False: 0

### 逻辑运算符

and、or、not

### some notes

> Different types have different properties, and when you're designing on computer program,
>
> you'll need to choose the types for your data based on how you're going to use them.

For example, if you want to use a number as a part of a sentence, it'll be easiest if that number is a string, because there are specially designed functions for working with each data type.

### some notes

3 techniques for operating on values: operators、functions、methods

operators 和 functions 只是长得不同，但其实二者的本质是一样的

methods are related to functions, but unlike functions, **methods are associated with specific types of objects !**

more frankly speaking, **there are different methods depending on the type of data you're working with !**

### some notes

```python
name = "Jack"
result = "Hello " + name
result_2 = "Hello {}".format(name)
```

### some notes

函数可以没有输入(no arguments)，也可以没有输出(eg: print, default return value is 'None')

Python 不允许函数修改不在函数作用域内的变量，这个原则仅适用于整数和字符串，列表、字典、集合、类中可以在子程序（子函数）中通过修改局部变量达到修改全局变量的目的。
