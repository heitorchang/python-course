Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('heichan')
heichan
>>> print('eichan is {} years old'.format(2019-1983))
eichan is 36 years old
>>> name = 'andrea'
>>> name
'andrea'
>>> name.upper()
'ANDREA'
>>> name.title
<built-in method title of str object at 0x036A6860>
>>> name.title()
'Andrea'
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
3
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
7
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
8
enter your guess 
Traceback (most recent call last):
  File "C:/Users/Andre/Desktop/code/number guess.py", line 9, in <module>
    guess = int(input('enter your guess '))
ValueError: invalid literal for int() with base 10: ''
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
5
enter your guess 4
enter your guess 0
>>> 8
8
>>> from random import randint
>>> randint(1, 9)
9
>>> randint(1, 9)
7
>>> randint(1, 9)
7
>>> randint(1, 9)
8
>>> randint(1, 9)
3
>>> randint(1, 9)
7
>>> [randint(1,9)]*8
[8, 8, 8, 8, 8, 8, 8, 8]
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
6
enter your guess 4
enter your guess 5
enter your guess 1
enter your guess 6
congratulations you guessed the number
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
9
enter your guess 9
enter your guess 5
enter your guess 2
enter your guess 4
congratulations you guessed the number
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
6
enter your guess 
Traceback (most recent call last):
  File "C:/Users/Andre/Desktop/code/number guess.py", line 9, in <module>
    guess = int(input('enter your guess '))
ValueError: invalid literal for int() with base 10: ''
>>> 
============ RESTART: C:/Users/Andre/Desktop/code/number guess.py ============
8
enter your guess 1
enter your guess 1
enter your guess 1
enter your guess 1
enter your guess 1
enter your guess 1
enter your guess 1
enter your guess 1
congratulations you guessed the number
>>> 1
1
>>> type(9)
<class 'int'>
>>> type('9')
<class 'str'>
>>> '9'+9
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    '9'+9
TypeError: can only concatenate str (not "int") to str
>>> '10'+'1'
'101'
>>> 10+1
11
>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> 2.7
2.7
>>> type(2.5)
<class 'float'>
>>> 
>>> name = bunda
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    name = bunda
NameError: name 'bunda' is not defined
>>> name = 'bunda'
>>> name
'bunda'
>>> name + name
'bundabunda'
>>> name * 4
'bundabundabundabunda'
>>> u = 'nelson'
>>> u
'nelson'
>>> u + ' is a ' + bunda
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    u + ' is a ' + bunda
NameError: name 'bunda' is not defined
>>> u + ' is a ' + name
'nelson is a bunda'
>>> type(u + ' is a ' + name)
<class 'str'>
>>> type(' is')
<class 'str'>
>>> u
'nelson'
>>> type(u)
<class 'str'>
>>> u=4
>>> u + ' is a ' + name
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    u + ' is a ' + name
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 'nelson'
'nelson'
>>> 4
4
>>> a=4
>>> b=4
>>> a+b
8
>>> b=5
>>> b
5
>>> a
4
>>> print(a)
4
>>> a
4
>>> 
============= RESTART: C:/Users/Andre/Desktop/code/dictionary.py =============
>>> bunda
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    bunda
NameError: name 'bunda' is not defined
>>> translate('bunda')
'tush'
>>> type(dictionary)
<class 'dict'>
>>> dictionary
{'bunda': 'tush', 'mobu': 'potato', 'yaya': 'coconut'}
>>> dictionary = d
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dictionary = d
NameError: name 'd' is not defined
>>> d = dictionary
>>> d['pudi'] = 'glasses'
>>> translate('pudi')
'glasses'
>>> d
{'bunda': 'tush', 'mobu': 'potato', 'yaya': 'coconut', 'pudi': 'glasses'}
>>> d is dictionary
True
>>> d == dictionary
True
>>> dictionary == d
True
>>> dictionary is d
True
>>> :=
