line=30*"-"
equal=90*"="

print('Hello Python')
print(equal)
# 4.2
name='John'
name
# height
# 4.3
print('\n#4.3')
print(line)
my_var=1
print(str(my_var) + ' is ' + str(type(my_var)))
my_var=0.0
print(str(my_var) + ' is ' + str(type(my_var)))
my_var=1,2,3
print(str(my_var) + ' is ' + str(type(my_var)))
my_var='abc'
print(str(my_var) + ' is ' + str(type(my_var)))
my_var=['a',2,'b',1]
print(str(my_var) + ' is ' + str(type(my_var)))
my_var={1,2,3}
print(str(my_var) + ' is ' + str(type(my_var)))
my_var={1:'a',2:'b'}
print(str(my_var) + ' is ' + str(type(my_var)))
my_var=range(20)
print(str(my_var) + ' is ' + str(type(my_var)))
print(equal)
# 5.2
print('\n#5.2')
print(line)
a=int(25)
print(str(a) + ' is ' + str(type(a)))
a=float(a)
print(str(a) + ' is ' + str(type(a)))

my_var = '123'
my_var = int(my_var)
print(type(my_var))

# my_var = [1,2,3]
# my_var = int(my_var)
# print(type(my_var))
# ERROR

my_var = '123'
my_var = list(my_var)
print(type(my_var))
print(equal)

# 6.3
print('\n#6.3')
print(line)

a = 123
b = 'a'
# a < b
# ERROR
print(a is b)
print(a != b)
print(equal)

# 7.1
print('\n#7.1')
print(line)

print(bool(1))
print(bool(0))
print(equal)

# 7.2
print('\n#7.2')
print(line)
print(bool('abc'))
print(bool([1,2,3]))
print(bool(''))

print(line)

print("bool('') is " + str(bool('')))
print(bool('0'))
print('bool([0]) is ' + str(bool([0])))
print(bool({}))
print(bool('None'))
print(bool(0.1))
print(bool(['']))
print(equal)

# 8.3
print('#8.3')
print(line)
print('New' + 'York')
print(['New'] + ['York'])
print(('New',)+('York',))
print(equal)

# 8.4
print('\n#8.4')
print(line)

print('=' * 20)
print('hello' * 2 + 'world' * 2)
print(['a'] * 3 + ['b'])
print(('a') * 3 + ('b'))
print(('a',) * 3 + ('b',))
print(equal)

# 8.6
print('\n#8.6')
print(line)
print('012345[2:5] is ' + '012345'[2:5])
print(['a','b','c','d','e'][1:2])
print(('a','b','c','d','e')[1:2])
print([0,1,2,3,4,5][:4])
print([0,1,2,3,4,5][2:])
print([0,1,2,3,4,5][:])
print([0,1,2,3,4,5][0:])
print([0,1,2,3,4,5][0:6])
print([0,1,2,3,4,5][:0])
print(equal)

# 8.7
print('\n#8.7')
print(line)
# sequence[start:stop:step]
print('0123456789'[1:8:2])
print('0123456789'[::2])
print(equal)

# 8.8
print('\n#8.8')
print(line)
print('name' in 'first name')
# print(1 in 12) ERROR
print(1 in [3,2,1])
print([3,2,1] in [3,2,1])
# print(1 in '12') ERROR
print(equal)

# 8.9
print('\n#8.9')
print(line)
print(len([0,1,2,3,4,5]))
print(len('abcfed'))
print(len(['a','b','c','d','e']))
print(len(('a','b','c','d','e')))
print(line)
print(len(('abcde')))
print(len(('abcde',)))
print(len('First Name'))
print(len([1,2,[3,4,5]]))
print(equal)

# 8.11
print('\n#8.11')
print(line)
# print('it's free') ERROR
print(ord('r'))

print(line)
print(14 == 14 and (15 < 6 and (1 < 0 or 25 > 24)))
print(14 == 14 and 15 < 6 and 1 < 0 or 25 > 24)
print(not not True or False and not True)
print(all(['0','0','0'])*3)
print(bool(bool())*True)


# 12.2
print('\n#12.2')
# abs(number)
# abs(-12)-> 12, abs(12.0) -> 12.0

# round(number[,ndigits rounding to])
# round(-12)-> -12, round(12.12,1) -> 12.1, round(12.12) -> 12
print(round(12.151,2))

# divmod(number1, number2)
# divmod(7,3) -> (2,1)
# Returns a tuple of (number1 // number2, number1 % number2) - result of floor division and remainder

# print(abs('name')) - ERROR
# print(abs((23,'a', 321))) - ERROR
# print(abs([213,32])) - ERROR
# print(abs({'name':'John','age': 32})) - ERROR
# print(abs({'a','b','c'))) - ERROR
# print(round('first name')) - ERROR
print('23452//35 = ' + str(23452//35))
print('23452%35 = ' + str(23452%35))

# 12.4
print('\n#12.4')
# >>> my_list = [1,2,3,4]
# >>> all(my_list)
# True
# >>> my_list = [0,1,2,3,4]
# >>> all(my_list)
# False
# >>> my_list = [1,2,3,4, '']
# >>> all(my_list)
# False

# >>> my_list = [1,2,3,4]
# >>> any(my_list)
# True
# >>> my_list = [1,'',0, '']
# >>> any(my_list)
# True
# >>> my_list = ['',0, '']
# >>> any(my_list)
# False
# >>> my_list = []
# >>> any(my_list)
# False

# 12.5
print('\n#12.5')
# >>> s='AbbcabbA'
# >>> s.count('a')
# 1

# 12.6
print('\n#12.6')
# range(stop)
# range(start, stop)
# range(start,stop,step)

r1=range(10)
print('range(10) is ' + str(r1))

r2=tuple(range(10))
print('tuple(range(10)) is ' + str(r2))

r2=list(range(10))
print('list(range(10)) is ' + str(r2))

r2=tuple(range(5,10))
print('tuple(range(5,10)) is ' + str(r2))

r2=tuple(range(5,10,2))
print('r2=tuple(range(5,10,2)) is ' + str(r2))

r3=list(range(5,1))
print('list(range(5,1)) is ' + str(r3))

r3=list(range(0))
print('list(range(0)) is ' + str(r3))

r3=list(range(3,9,-1))
print('list(range(3,9,-1)) is ' + str(r3))

r3=list(range(10,0,-1))
print('list(range(10,0,-1)) is ' + str(r3))

r3=list(range(0,10,3))
print('list(range(0,10,3)) is ' + str(r3))

r3=list(range(10,0,-2))
print('list(range(10,0,-2)) is ' + str(r3))

# r3=list(range(1,10,0))
# print('list(range(1,10,0)) is ' + str(r3))
# ERROR

# r3 = range(10)
# list(r3+r3)
# print('Concatenation r3 = range(10) and results list(r3+r3) is ' + str(r3))
# # ERROR

# r3=r3 * 2
# print('Repetition r3=r3 * 2 is ' + str(r3))
# ERROR

r3=range(10)[5]
print('Indexing r3=range(10)[5] is ' + str(r3))

r3=range(10)[2:6]
print('Slicing r3=range(10)[2:6] is ' + str(r3))

r3=6 in range(10)
print('Membership r3=6 in range(10) is ' + str(r3))

# r3=range([1,2,3])
# print('Conversion r3=range([1,2,3]) is ' + str(r3))
# ERROR

# 12.7
print('\n#12.7')
# list.sort(key=None,reverse=False)
# lst = ['a',1,'3',''] #cannot order strings and ints
# r4=lst.sort()
# print('r4=lst.sort() is ' + str(r4))
# ERROR

# sorted() built-in function
# sorted(iterable, key=None, reverse=None)

a = [1,9,2,6,3,5,8]
r1=sorted(a)
print('a = [1,9,2,6,3,5,8], r1=sorted(a) is ' + str(r1))
print(a)

# 12.8
print('\n#12.8')

print('\nstr.join(iterable)')
r1=', '.join(['1','2','3'])
print("r1=', '.join(['1','2','3']) is " + str(r1))

print('\nstr.split(sep=None, maxsplit=-1)')
r1='1 2 3'.split()
print("r1='1 2 3'.split() is " + str(r1))
r1='1,2,3'.split(',')
print("r1='1,2,3'.split(',') is " + str(r1))

print('\nstr.splitlines([keepends])')
r1='This is the first line\nThis is the second line'.splitlines()
print("r1='This is the first line\nThis is the second line'.splitlines() is " + str(r1))

print('\nstr.partition(separator)')
r1='Big&Small'.partition('&')
print("r1='Big&Small'.partition('&') is " + str(r1))
r1='up-to-date'.partition('-')
print("r1='up-to-date'.partition('-') is " + str(r1))
r1='up*to*date*cu'.partition('-')
print("r1='up*to*date*cu'.partition('-') is " + str(r1))

# 12.9
print('\n#12.9')

print('\nstr.replace(what,forwhat)')
r1='Race'.replace('R','F')
print("r1='Race'.replace('R','F') is " + str(r1))

r1='Race'.replace('b','c')
print("r1='Race'.replace('b','c') is " + str(r1))

print('\nstr.strip(chars)')
r1=' too many spaces '.strip()
print("r1=' too many spaces '.strip() is " + str(r1))
r1='www.engeto.com'.strip('.cmow')
print("r1='www.engeto.com'.strip('.cmow') is " + str(r1))
r1='www.engeto.com'.strip('.cmowe')
print("r1='www.engeto.com'.strip('.cmowe') is " + str(r1))
r1='Entire line\n'.strip('n')
print("r1='Entire line\\n'.strip('n') is " + str(r1))
r1='Entire line\n'.strip('\n')
print("r1='Entire line\\n'.strip('\\n') is " + str(r1))

print('\nstr.lstrip(chars)')
r1="www.engeto.com".lstrip('.cmow')
print('''r1="www.engeto.com".lstrip('.cmow') is ''' + str(r1))
r1='\tEntire line\n'.lstrip()
print("r1='\\tEntire line\\n'.lstrip() is " + str(r1))
r1=' too many spaces '.lstrip()
print("r1=' too many spaces '.lstrip() is " + str(r1))
print('\nstr.rstrip(chars)')
r1="www.engeto.com".rstrip('.cmow')
print('''r1="www.engeto.com".rstrip('.cmow') is ''' + str(r1))

print('\n#12.10')
print('\nstr.startswith(substr[,start[,end]])')
# str.startswith(substr[,start[,end]])
#     substr - Substring or sigle character we are looking for
#     start - Integer specifying the index at which we want the check to begin
#     end - Integer specifying the index at which we want the check to end

r1='Python'.startswith('Py')
print("r1='Python'.startswith('Py') is " + str(r1))
r1='Python'.startswith('t',2)
print("r1='Python'.startswith('t',2) is " + str(r1))

print('\nstr.endswith(substr[,start[,end]])')
r1='Python'.endswith('on')
print("r1='Python'.endswith('on') is " + str(r1))
r1='Python'.endswith('n',5)
print("r1='Python'.endswith('on') is " + str(r1))

print('\nstr.find(sub[, start[, end]])')
r1='anamgram'.find('a')
print("r1='anamgram'.find('a') index is " + str(r1))
r1='anamgram'.find('a',1)
print("r1='anamgram'.find('a',1) index is " + str(r1))
r1='anamgram'.find('m')
print("r1='anamgram'.find('m') index is " + str(r1))
r1='anamgram'.find('h')
print("r1='anamgram'.find('h') index is " + str(r1))

print('\nstr.rfind(substr[,start[,end]])')
r1='anagram'.rfind('a')
print("r1='anagram'.rfind('a') index is " + str(r1))
r1='anagram'.rfind('a',3)
print("r1='anagram'.rfind('a',3) index is " + str(r1))
r1='anagram'.rfind('a',5)
print("r1='anagram'.rfind('a',5) index is " + str(r1))
r1='anagram'.rfind('a',6)
print("r1='anagram'.rfind('a',6) index is " + str(r1))

print('\n#12.11')

print('\nstr.upper()')
r1='abc'.upper()
print("r1='abc'.upper() is " + str(r1))

print('\nstr.lower()')
r1='Mr. Jones PhD.'.lower()
print("r1='Mr. Jones PhD.'.lower() is " + str(r1))

print('\nstr.isupper()')
r1='Mr. Jones PhD.'.isupper()
print("r1='Mr. Jones PhD.'.lower() is " + str(r1))
r1='NAME'.isupper()
print("r1='NAME'.isupper() is " + str(r1))

print('\nstr.islower()')
r1='Mr. Jones PhD.'.islower()
print("r1='Mr. Jones PhD.'.islower() is " + str(r1))

print('\nstr.title()')
r1='first name'.title()
print("r1='first name'.title() is " + str(r1))
r1='123word'.title()
print("r1='123word'.title() is " + str(r1))
r1="They've returned".title()
print("r1='They've returned'.title() is " + str(r1))

print('\nstr.istitle()')
r1='Mr. Jones PhD.'.istitle()
print("r1='Mr. Jones PhD.'.istitle() is " + str(r1))
r1='Mr. Jones Phd.'.istitle()
print("r1='Mr. Jones Phd.'.istitle() is " + str(r1))

print('\nstr.swapcase()')
r1='Mr. Jones PhD.'.swapcase()
print("r1='Mr. Jones PhD.'.swapcase() is " + str(r1))

print('\n#12.12')
print('\nstr.isalpha()')
r1='abc'.isalpha()
print("r1='abc'.isalpha() is " + str(r1))
r1='abc-de'.isalpha()
print("r1='abc-de'.isalpha() is " + str(r1))
r1='abc123'.isalpha()
print("r1='abc123'.isalpha() is " + str(r1))
r1=''.isalpha()
print("r1=''.isalpha() is " + str(r1))

print('\nstr.isdecimal()')
r1='765234'.isdecimal()
print("r1='765234'.isdecimal() is " + str(r1))

print('\nstr.isalnum()')
r1='Z312'.isalnum()
print("r1='Z312'.isalnum() is " + str(r1))

    # c.isalpha()
    # c.isdecimal()
    # c.isdigit()
    # c.isnumeric()

print('\nstr.isspace()')
# Returns True if all the characters inside the string are space characters:
# ' '- space '\t' - tab '\n' - newline '\r' - carriage return '\x0b' - vertical tab '\f' - form feed)

print('\x0b')
print('\tabc')

r1=" ".isspace()
print('''r1=" ".isspace() is ''' + str(r1))

print('\nstr.isdigit()')
r1="\u00B2".isdigit()
print('''r1="\u00B2".isdigit() is ''' + str(r1))
r1='765234'.isdigit()
print(''''765234'.isdigit() is ''' + str(r1))

print('\nstr.isnumeric()')
r1="\u00B2".isnumeric()
print('''r1="\u00B2".isnumeric() is ''' + str(r1))
r1="\u2165".isnumeric()
print('''r="\u2165".isnumeric() is ''' + str(r1))
r1='1+1'.isnumeric()
print('''r='1+1'.isnumeric() is ''' + str(r1))
r1="\u00BC".isnumeric()
print('''r1="\u00BC".isnumeric() is ''' + str(r1))
r1="\u2165".isnumeric()
print('''r1="\u2165".isnumeric() is ''' + str(r1))

print('\n#12.13')
print('\nstr.center(result_length[,padding_char])')
    # result_length - Length of returned centered string
    # padding_char- String that is filled inside the string for padding the original string from right and left side

r1='First Name'.center(14,'-')
print("r1='First Name'.center(14,'-') is " + str(r1))

r1='First Name'.center(7,'-')
print("r1='First Name'.center(7,'-') is " + str(r1))

print('\nstr.ljust(result_length[,padding_char])')
    # result_length - Length of returned result string
    # padding_char- String that is filled in as padding for original string from right side

r1='Name'.ljust(8,'+')
print("r1='Name'.ljust(8,'+') is " + str(r1))
r1='Name'.ljust(4,'+')
print("r1='Name'.ljust(4,'+') is " + str(r1))

print('\nstr.rjust(result_length[,padding_char])')
    # result_length - Length of returned result string
    # padding_char- String that is filled in as padding for original string from left side

r1='Name'.rjust(4,'+')
print("r1='Name'.rjust(4,'+') is " + str(r1))
r1='Name'.rjust(8,'+')
print("r1='Name'.rjust(8,'+') is " + str(r1))

print('\nstr.zfill(result_length)')
# result_length - Length of returned result string
# New right justified string padded with zeroes
# (zfill = zero fill). The difference compared to rjust is that if minus '-' or plus '+' sign is used at the beginning of the original string, then this symbol is kept at its position ('+0065'). Padding is done using only '0' character. The original string is returned if width is less than or equal to len(s).
r1='+ab'.zfill(5)
print("r1='+ab'.zfill(5) is " + str(r1))
r1='-65'.zfill(6)
print("r1='-65'.zfill(6) is " + str(r1))
