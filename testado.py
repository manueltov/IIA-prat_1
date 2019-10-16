Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> x = 10
>>> print(x*2)
20
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello 
 World!
>>> x = 10
>>> type x
SyntaxError: invalid syntax
>>> type (x)
<class 'int'>
>>> x = False
>>> type(x)
<class 'bool'>
>>> x = 1.0
>>> type(x)
<class 'float'>
>>> x = "Hello"
>>> type(x)
<class 'str'>
>>> x = 'a'
>>> type(x)
<class 'str'>
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello 
 World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello 
 World!
Hello 
 World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello 
 World!
Hello 
 World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
Hello World!
Hello World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
Hello World!
Hello World!
>>> x = 00011010
SyntaxError: invalid token
>>> a&b
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a&b
NameError: name 'a' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
Hello World!
Hello World!
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
Hello World!
Hello World!
>>> listinha
[0, 1, 2, 7, 8, 4, 3]
>>> listinha**2
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    listinha**2
TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
>>> listinha ++ listinha
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    listinha ++ listinha
TypeError: bad operand type for unary +: 'list'
>>> listinha + listinha
[0, 1, 2, 7, 8, 4, 3, 0, 1, 2, 7, 8, 4, 3]
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
Hello World!
Hello World
>>> frase
'Hello World'
>>> frase + listinha
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    frase + listinha
TypeError: must be str, not list
>>> frase[2]
'l'
>>> frase[6]
'W'
>>> len(frase)
11
>>> 
============== RESTART: /home/ALUNOSFC/fc49522/Desktop/hello.py ==============
Hello World!
Hello World!
Hello World
>>> group
['Bob', 23, 'George', 72, 'Myriam', 29]
>>> type(group)
<class 'list'>
>>> <class 'list'>
SyntaxError: invalid syntax
>>> frase * 4
'Hello WorldHello WorldHello WorldHello World'
>>> (frase + " ") * 4
'Hello World Hello World Hello World Hello World '
>>> (frase + "\n") *4
'Hello World\nHello World\nHello World\nHello World\n'
>>> frase + " \n"
'Hello World \n'
>>> frase + ' \n'
'Hello World \n'
>>> x = ["a","b","c"]
>>> x
['a', 'b', 'c']
>>> y = [x]*4
>>> y
[['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
>>> y = x*4
>>> t
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t
NameError: name 't' is not defined
>>> z = [1, 2, 3]
>>> z * 4
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> [z]*4
[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
>>> z = z *4
>>> z
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> z = [1, 2, 3]
>>> z = [z] * 4
>>> z
[[1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
>>> z[0][0] = 9
>>> z
[[9, 2, 3], [9, 2, 3], [9, 2, 3], [9, 2, 3]]
>>> x = input ("Escreva numero int: ")
Escreva numero int: 22
>>> x
'22'
>>> y = int(x) //2
>>> y
11
>>> print (" {1} corresponde a metade de {0}".format(x, y))
 11 corresponde a metade de 22
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/ALUNOSFC/fc49522/Desktop/hello.py', 'frase': 'Hello World', 'listinha': [0, 1, 2, 7, 8, 4, 3], 'group': ['Bob', 23, 'George', 72, 'Myriam', 29], 'x': '22', 'y': 11, 'z': [[9, 2, 3], [9, 2, 3], [9, 2, 3], [9, 2, 3]]}
>>> s = "  SOU O MAIOR!  "
>>> S
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> s
'  SOU O MAIOR!  '
>>> s.center(20)
'    SOU O MAIOR!    '
>>> s.center(100)
'                                            SOU O MAIOR!                                            '
>>> s.center()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.center()
TypeError: center() takes at least 1 argument (0 given)
>>> 
>>> 
>>> 
>>> s.center(100,"*")
'******************************************  SOU O MAIOR!  ******************************************'
>>> 
