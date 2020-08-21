Python 3.8.2 (default, Jul 16 2020, 14:00:26) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> fruit = 'banana'
>>> letter = fruit[1]
>>> print(letter)
a
>>> letter = fruit[0]
>>> print(letter)
b
>>> letter = fruit[1.5]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    letter = fruit[1.5]
TypeError: string indices must be integers
>>> fruit = 'banana'
>>> len(fruit)
6
>>> length = len(fruit)
>>> last = fruit[length]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    last = fruit[length]
IndexError: string index out of range
>>> last = fruit[length-1]
>>> print(last)
a
>>> fruit = 'banana'
>>> fruit[0]+fruit[2]
'bn'
>>> index = 0
>>> while index < len(fruit)
SyntaxError: invalid syntax
>>> while index < len(fruit):
	letter = fruit[index]
	print(letter)
	index = index + 1

	
b
a
n
a
n
a
>>> numbers = []
>>> numbers.append(1)
>>> numbers
[1]
>>> numbers.append(32)
>>> numbers.append(100)
>>> numbers
[1, 32, 100]
>>> vaardi = ['a','ab','abc']
>>> vaardi
['a', 'ab', 'abc']
>>> vaardu_garumi = []
>>> vaardu_garumi.append(len(vaardi[0]))
>>> vaardu_garumi.append(len(vaardi[1]))
>>> vaardu_garumi.append(len(vaardi[4]))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    vaardu_garumi.append(len(vaardi[4]))
IndexError: list index out of range
>>> vaardu_garumi.append(len(vaardi[2]))
>>> vaardu_garumi.append(len(vaardi[3]))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    vaardu_garumi.append(len(vaardi[3]))
IndexError: list index out of range
>>> vaardu_garumi
[1, 2, 3]
>>> ['a', 'ab', 'abc','aaaaaa']
['a', 'ab', 'abc', 'aaaaaa']
>>> vaardu_garumi.append(len(vaardi[4]))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    vaardu_garumi.append(len(vaardi[4]))
IndexError: list index out of range
>>> vaardi
['a', 'ab', 'abc']
>>> vaardi = ['a','ab','abc','aaaaaaaaa']
>>> vaardi
['a', 'ab', 'abc', 'aaaaaaaaa']
>>> vaardu_garumi.append(len(vaardi[4]))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    vaardu_garumi.append(len(vaardi[4]))
IndexError: list index out of range
>>> vaardu_garumi.append(len(vaardi[4]))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    vaardu_garumi.append(len(vaardi[4]))
IndexError: list index out of range
>>> vaardi
['a', 'ab', 'abc', 'aaaaaaaaa']
>>> vaardu_garumi.append(len(vaardi[3]))
>>> vaardu_garumi.append(len(vaardi[4]))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    vaardu_garumi.append(len(vaardi[4]))
IndexError: list index out of range
>>> vaardi
['a', 'ab', 'abc', 'aaaaaaaaa']
>>> vaardu_garumi
[1, 2, 3, 9]
>>> for char in fruit:
	print(char)

	
b
a
n
a
n
a
>>> s = 'Monty Python'
>>> print(s[0:5])
Monty
>>> print(s[6:12])
Python
>>> fruit = 'banana'
>>> fruit[:3]
'ban'
>>> fruit[3:]
'ana'
>>> greeting = 'Hello, world!'
>>> greeting[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    greeting[0] = 'J'
TypeError: 'str' object does not support item assignment
>>> new_greeting = 'J' + greeting[1:]
>>> print(new_greeting)
Jello, world!
>>> word = 'banana'
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
print(count)
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == 'a':
		count = count + 1
    print(count)
    
SyntaxError: unindent does not match any outer indentation level
>>> for letter == 'a':
	
SyntaxError: invalid syntax
>>> for letter in word: 'a':
	
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == 'a':
		count = count + 1
	print(count)

	
0
1
1
2
2
3
>>> for letter in word:
	if letter == 'a':
		count = count + 1
		print(count)

		
4
5
6
>>> word
'banana'
>>> count
6
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
		print(count)

		
1
2
3
>>> for letter in word:
	if letter == 'a':
		count = count + 1
	print(count)

	
3
4
4
5
5
6
>>> for letter in word:
	if letter == 'a':
		count = count + 1
print(count)
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == 'a':
		count = count + 1
    print(count)
    
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
		print(count)

		
7
8
9
>>> count = 0
>>> for letter in word:
	if letter == 'a':
		count = count + 1
    print(count)
    
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
	print(count)

	
0
1
1
2
2
3
>>> count = 0
>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False
>>> if word == 'banana':
	print('All right, bananas.')

	
All right, bananas.
>>> for letter in word:
	if letter == 'a':
		count = count + 1
    print(count)
    
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
print(count)
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == 'a':
		count = count + 1
 print(count)
 
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
  print(count)
  
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
   print(count)
   
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
    print(count)
    
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
	print(count)

	
0
1
1
2
2
3
>>> for letter in word:
	if letter == 'a':
		count = count + 1print(count)
		
SyntaxError: invalid syntax
>>> for letter in word:
	if letter == 'a':
		count = count + 1
    print(count)
    
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
     print(count)
     
SyntaxError: unindent does not match any outer indentation level
>>> for letter in word:
	if letter == 'a':
		count = count + 1
      print(count)
      
SyntaxError: unindent does not match any outer indentation level
>>> 