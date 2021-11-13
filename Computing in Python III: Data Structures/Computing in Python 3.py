# # (1) append
# s = []
# s.append(1)
# s.append("a")
# print(s)

# # (2) upper
# s = "abc"
# print(s.upper())
# print(s)

# # (3) reassigning immutable data types & id() (memory address)
# i = 1
# print(id(i))
# i = 1
# print(id(i))
# i = 3
# print(id(i))
# print(hex(id(i)))

# # (4) list alias / reassigning
# l1 = [1, 2, 3]
# l2 = l1
# print(l1, l2)
# print(id(l1), id(l2))
# l2.append(4)
# print(l1, l2)
# print(id(l1), id(l2))
# l2 = [1, 2]
# print(l1, l2)
# print(id(l1), id(l2))

# # (5) invalid string declaration
# s = ""abcd""
# s = ''abcd''
# s = "'"abc"'" # to use " and ' together, triple " or tripple ' is needed
#s3 = """"'abc'"""" # it does not print "'abc'"

# # (6) valid string declarations
# s1 = "'abc'"
# s2 = '"abc"'
# s3 = """'"abc"'"""
# s4 = '''"'abc'"'''
# s5 = ''''ello, "world"!'''

# # (7) invalid new line character in string
# s = "abc
# def"

# # (8) valid new line character in string
# s = "abc\ndef"
# print(s)

# # (9) valid new line with triple '
# s = '''abc
# def\nghi'''
# print(s)

# # (10) valid new line with triple "
# s = """abc
# def\nghi"""
# print(s)

# # (11) string is immutable
# s = "abcde"
# print(s[4])
# s[4] = 'E'

# # (12) in / not in
# s = "abcde"
# print('ab' in s)
# print('ac' not in s)

# # (13) find()
# s = "abcdeabcda"
# print(s.find('b')) # index of first b is 1
# print(s.find('f')) # f not on s
# print(s.find('cd')) # cd starts at index 2
# print(s.find('b', 1)) #index of first b from index 1
# print(s.find('b', 2, 6)) # print index of b from index 2 to 5 (6 is not included)
# print(s.find('b', 1, 7)) # print the first index of b from 1 to 6
# print(s.count('a')) # number of count of a in s

# # (14) split()
# s = "This is Jake. I am learning python coding.        I will be a full stack data scientist."
# print(s.split())
# print(s.split(" "))
# print(s.split("."))

# # (15) Imagine you have a string stored in the variable myString, but you don't know how long it is.
# # You want to create a slice starting on the 5th character, and including every other character after that.
# # Which of the following lines of code would successfully generate a slice of the string starting with
# # the 5th character and including every other character after that?
# myString = "I am ground"
#
# print(myString[4::2])
# print(myString[::2][2:])

# # (16) Remove character from string using replace()
# s = "123#123%#56765$$"
# s.replace('#', '')
# s.replace('$', '')
# s.replace('%', '')
# print(s)
# s = "123#123%#56765$$"
# s = s.replace('#', '')
# s = s.replace('$', '')
# s = s.replace('%', '')
# print(s)

# # (17) tuple declaration
# t1 = ('a', 1, True)
# t2 = 'a', 1, True # parentheses is optional
#
# print(t1, t2)
# print(t1[2], t2[2])

# # (18) tuple slicing
# t = (1,2,3,4,5,6,7)
# print(t[-1:1:-1])

# # (19) tuple unpacking
# t = (1 , True, "Hello", 1.5)
# a, b, c, d = t
# print(a, b, c, d)
# (a, c, b, d) = t # can use parentheses as well
# print(a, b, c, d)

# # (20) a function return multiple variable with tuple
#
# def returnTuple(integer, divisor):
#     q = integer // divisor
#     r = integer % divisor
#     return (q, r)
#
# (q, r) = returnTuple(11, 3)
# print(q, r)

# # (21) nested tuple
# t = ((1, 2, 3), (4, 5, 6,))
# print(t[1][2])

# # (22) tuple unpacking also works for list
# l = [1, 2, 3]
# a, b, c = l
# print(a, b, c)

# # (23) insert()
# l = [1, 2, 3]
# l.insert(1, 4)
# print(l)

# # (24) copy()
# l1 = [1, 2, 3]
# l2 = l1.copy()
# l2[1] = 4
# print(l1, l2)

# # (25) del
# l = [1, 2, 3, 4, 5]
# del l[2]
# print(l)
# del l[1:3]
# print(l)
# try:
#     del l
#     print(l)
# except:
#     print("error")

# # (26) Iterating over loop and tuple
# t = (1, 2, 3)
# for n in t:
#     print(n)
# l = (1, 2, 3)
# for n in l:
#     print(n)
#
# # (27) Write file
# outputFile = open("testFile.txt", 'w')
# outputFile.write("Hello")
# outputFile.write("World")
# print(outputFile) # cannot read
# outputFile.close() # HelloWorld saved

# # (28) write only string
# outputFile = open("testFile.txt", 'w')
# outputFile.write(1) # write() cannot save integer to file 1 has to be coverted to string
# outputFile.close()

# #(29) write list
# outputFile = open("testFile.txt", 'w')
# l = ["a", "b", "c", "d"]
# for al in l:
#     outputFile.write(al)
# outputFile.close()
# # abcd

# #(30) write list 2
# outputFile = open("testFile.txt", 'w')
# l = ["a", "b", "c", "d"]
# for al in l:
#     outputFile.write(al + "\n")
# outputFile.close()
# # a
# # b
# # c
# # d

# #(31) write list 3
# outputFile = open("testFile.txt", 'w')
# l = ["a", "b", "c", "d"]
# outputFile.writelines(l) #write all items in list
# outputFile.close()
# #abcd

# #(32) write list 4
# outputFile = open("testFile.txt", 'w')
# l = ["a", "b", "c", "d"]
# outputFile.write("\n".join(l))
# outputFile.close()
# # a
# # b
# # c
# # d

# # (33) write 5
# outputFile = open("testFile.txt", 'w')
# print("Hello", file = outputFile)
# print("Beautiful", outputFile) # This line just print Beautiful on console
# print("World", file = outputFile) # When using print to write, line break automatically added at the end

# # (34) end and sep
# # end and sep are optional parameters of Python. The end parameter basically prints after all the output objects
# # present in one output statement have been returned. the sep parameter differentiates between the objects.
# a=2
# b='abc'
# print(a,b,sep=',') #2,abc
# print(a,b,end=',') #2 abc,

# # (35) append mode
# outputFile = open("testFile.txt", 'a')
# outputFile.write("Hello ")
# outputFile.write("World")

# # (36) append with print
# outputFile = open("testFile.txt", 'a')
# print("Hello", file = outputFile)
# print("Beautiful", outputFile) # This line just print Beautiful on console
# print("World", file = outputFile) # When using print to write, line break automatically added at the end

# # (37) print does not work when reading
# outPutFile = open("testFile.txt", 'r')
# print(outPutFile) # not printing text in the file

# # (38) readline
# outputFile = open("testFile.txt", 'r')
# print(outputFile.readline())
# print(outputFile.readline())
# print(outputFile.readline())
# print(outputFile.readline())

# # (39) readline with strip
# outputFile = open("testFile.txt", 'r')
# print(outputFile.readline().strip())
# print(outputFile.readline().strip())
# print(outputFile.readline().strip())
# print(outputFile.readline().strip())

# # (40) int() strips automatically
# a = "1\n"
# b =  "2\n"
# print(int(a))
# print(int(b))

# # (41) read to list
# outputFile = open("testFile.txt", 'r')
# l = []
# for line in outputFile:
#     l.append(line.strip())
# print(l)
# outputFile.close()

# # (42) save and load function
# def save(filename, inList):
#     outputFile = open(filename, 'w')
#     for item in inList:
#         print(item, file = outputFile)
#     outputFile.close()
#
# def load(filename):
#     inputFile = open(filename, 'r')
#     inList = []
#
#     for line in inputFile:
#         inList.append(line.strip())
#     inputFile.close()
#     return inList

# # (43) write integer to file with print()
# outputFile = open("testFile.txt", 'a')
# outputFile.write("*")
# print(1, file = outputFile) # when using print 1 automatically converted to string
# outputFile.write("*")

# # (44) output file creation
# file_name = "CreateNewFile"
# outputFile = open(file_name, 'w') # If there is no file with the name "CreateNewFile" in the directory, python creates a new file with the same name.
# outputFile.write("A file has been created.")

# # (45) if you put a string that contains something that looks like a tuple into ast.literal_eval(),
# # then it will convert it to a tuple. For example, this code:
#
# # import ast
# # my_tuple = ast.literal_eval("('Rogue One', 530, 2017)")
# #
# # ...will create the tuple ('Rogue One', 530, 2017) from the string "('Rogue One', 530, 2017)". This is useful because
# # in the previous exercise, we printed lines like "('Rogue One', 530, 2017)" to our file. When we read them,
# # Python will initially interpret them as strings.
# movie_list = [('Rogue One', 530, 2017), ('Finding Dory', 486, 2017), ('Captain America: Civil War', 408, 2017)]
# output_file = open("movies.txt", "w")
# for movie in movie_list:
#     print(movie, file = output_file) #print tuple as a string "('Rogue One', 530, 2017)"
# output_file.close()
#
# import ast
# movie_list = []
# input_file = open("movies.txt", "r")
# for line in input_file:
#     line_as_tuple = ast.literal_eval(line)
#     movie_list.append(line_as_tuple)
# input_file.close()

# # (46) open default mode
# def angry_file_finder(s):
#     input_file = open(s) # default mode is 'r'
#     for line in input_file:
#         if "!" not in line:
#             return False
#     input_file.close()
#     return True

# # (47) read()
# # The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
# inputFile = open("testFile.txt")
# print(inputFile.read()) # print whole text in the file

# # (48) read(-1)
# # The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
# inputFile = open("testFile.txt")
# print(inputFile.read(-1)) # print whole text in the file

# # (49) read(10)
# # The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
# inputFile = open("testFile.txt")
# print(inputFile.read(13)) # line break 포함해서 텍스트 13개 출력함

# # (50) readlines (not readline...)
# inputFile = open("testFile.txt")
# print(inputFile.readlines()) # When called on a file object, this will return a list of all the lines in the file.
# #  <for line in inputFile:> -> Python runs this as <for line in inputFile.readlines():>

# # (51) with open (file object closed automatically)
# with open("testFile.txt") as f:
#     print(f.readlines())

# # (52) with open newline = ""
# with open("newlineTest.txt", "w", newline= "") as f:
#     f.write("1")
#     f.write("2")
#     f.write("3")

# # (53) with open newline default
# with open("newlineTest.txt", "w") as f:
#     f.write("1")
#     f.write("2")
#     f.write("3")

# # (54) with open newline = None
# with open("newlineTest.txt", "w", newline= None) as f:
#     f.write("1")
#     f.write("2")
#     f.write("3")

# 52 ~ 54 what difference?

# # (55) Positional Arguments Specified by an Iterable / Keyword Arguments
# term_list = [3, 5]
# print(complex(3, 5)) #Positional Arguments
# print(complex(*term_list)) #Iterable Input (list)
# print(complex(real=3, imag=5)) # Keyword Arguments
# print(complex(imag=5, real=3)) # Keyword Arguments

# # (56) Keyword Arguments Specified by a Dictionary
# # keyword_dict = {'keyword1': value1, 'keyword2': value2}
# # function(**keyword_dict)
# keyword_dict = {'real': 3, 'imag': 5}
# complex(**keyword_dict)

# # (57)
# print(complex(3, 5, real=3, img=5)) # Error
# # Question : Keyword Arguments become Positional Arguments when used without Keyword?

# # (58) Try more cases
# print(complex(3, imag=5)) # works
# print(complex(real=3, 5)) # Error positional argument follows keyword argument

# # (59) Let's do experiment
#
# def test(a = 1, b = 2, c = 3, d = 4):
#     print(a, b, c, d)
#
# test()
# test(1)
# test(1, 2)
# test(1,)
# test(a = 1)
# test(b = 2)
# test(c = 3, a = 1)
# test(c = 3, a = 1, d = 4, b = 2)
# test(1, c = 3, d = 4)
# test(1)
# test(1, 2)
# # test(1, b = 2, 3, 4) #error positional argument follows keyword argument
# # test(a = 1, 2, 3, 4) #error positional argument follows keyword argument
# # test(1, a = 1) #error positional argument follows keyword argument

# # (60) More experiment
# def test1(a, b, c = 3, d = 4):
#     print(a, b, c, d)
#
# def test2(a = 1, b): #error non-default argument follows default argument
#     print(a, b)
#
# def test3(a, b = 1, c): #error non-default argument follows default argument
#     print(a, b, c)
#
# test1(1, 2)
# test1(1, 2,)
# test1(1, 2, , ) #syntax error

# # (61) with open close properly?
# with open("movies.txt") as f:
#     print(f.readline())
# print(f.readline()) #error -> file closed after with open block

# # (62) partition() -> split to 3 strings
# t = "Hello World !!".partition('o')
# print(t)

# # (63) tuple()
# print(tuple([1, 2, 3])) -> convert list to tuple
# print(tuple({1 : 'a', 2 : 'b', 'c' : 3})) -> print keys

# # (64) join with tuple
# print(" ".join(("1", "string", "3", "True")))

# # (65) convert tuple to string -> not covert each element to string but covert the whole tuple to string
# print(" ".join(str((1, 1.1, True))))

# # (66) Dictionary
# d = {'a' : 1, 'b' : 2, 'c' : 3}
# print(d)
# # d.append(4) # 'dict' object has no attribute 'append'
# d['d'] = 4
# print(d)
# d['c'] = 5
# print(d)
# del d['d']
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# for (key, value) in d.items():
#     print(key, value)

# # (67) Count of Words
# aString ="Hello! This is a randon string. This program will count the numer of words which exist in this string."
# aString = aString.replace('!', "")
# aString = aString.replace('.', "")
# aString = aString.lower()
# wordsList = aString.split()
# print(wordsList)
# counts = {}
#
# for word in wordsList:
#     if word in counts.keys():
#         counts[word] += 1
#     else:
#         counts[word] = 1
#
# print(counts)

# # (68) People sitting on the table
# peopleTable = {"Jake" : 1, "Teddy" : 2, "Kobe" : 2, "Angie" : 1}
#
# for i in range(1,3):
#     print("The guests who sit at table", i, "is")
#     for (name, table) in peopleTable.items():
#         if table == i:
#             print(name, end=" ")
#     print("\n")

# # (69) Dictionaries and Lists
# classes = {"History" : ["Jake", "Angie"], "Math" : ["Jake", "Teddy"]}
# print(classes["Math"][1])

# # (70) Dictionaries as objects
# info = {"Jake" : {"phone" : "4087241311", "address" : "Los Angeles 90025", "Martial Status" : "Married"}}
# print(info["Jake"]["phone"])

# # (71) tuple equal?
# t1 = (1, 3, 2, 5, 4)
# t2 = (1, 2, 3, 4, 5)
# t3 = (1, 2, 3, 4, 5)
# print(t1 == t2) # order matters!
# print(t2 == t3) # True

# # (72) sum() with a list
# l = [1, 2, 3, 4, 5]
# print(sum(l) / len(l))