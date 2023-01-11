>>> MyList = __import__('1-my_list').MyList
>>> d = MyList()
>>> isinstance(d, list)
True
>>> my_list = MyList()
>>> my_list.append(5)
>>> my_list.append(1)
>>> my_list.append(4)
>>> print(my_list)
[5, 1, 4]
>>> my_list.print_sorted()
[1, 4, 5]
>>> print(my_list)
[5, 1, 4]

Test 2: Empty list
>>> c = MyList()
>>> print(c)
[]
>>> c.print_sorted()
[]

Test 2: Empty list
>>> e = MyList()
>>> issubclass(type(e), list)
True

Test 2: Empty list
>>> a = MyList()
>>> a.append(-5)
>>> a.append(-4)
>>> a.append(-10)
>>> print(a)
[-5, -4, -10]
>>> a.print_sorted()
[-10, -5, -4]
>>> print(a)
[-5, -4, -10]

Test 2: Empty list
>>> b = MyList()
>>> b.append(-20)
>>> b.append(-4)
>>> b.append(-10)
>>> print(b)
[-20, -4, -10]
>>> b.print_sorted()
[-20, -10, -4]
