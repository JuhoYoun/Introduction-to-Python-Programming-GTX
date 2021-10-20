# # (1) isdigit()
#
# myNumericString = "12345"
# myNonNumericString = "ABCDE"
#
# #Checks if myNumericString is purely numeric
# if myNumericString.isdigit():
#     print("The first string is numerical.")
# else:
#     print("The first string is non-numerical.")
# #Checks if myNonNumericString is purely numeric
# if myNonNumericString.isdigit():
#     print("The second string is numerical.")
# else:
#     print("The second string is non-numerical.")

# # (2) for each loop
# listOfNumbers = [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
# sum = 0
#
# #Runs this loop once for each item, assigning the current
# #item to the variable 'currentNumber'
# for currentNumber in listOfNumbers:
#     sum += currentNumber
# #Divides sum by the number of items in the list
# print(sum / len(listOfNumbers))

# # (3) randint
# import random
# print(random.randint(0, 10))

# # (4) Range
# for x in range(3):
#     print("Looped!")
# for i in "hey":
#     print("Looped!")
# for a in [10, 9, 8]:
#     print("Looped!")
# for num in range(10, 1, -3):
#     print("Looped!")

# # (5) Triangle
# for i in range(5, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print("")
#
# i = 5
# while i > 0:
#     j = i
#     while j > 0:
#         print(j, end=" ")
#         j -= 1
#     i -= 1
#     print("")
# # In Python 3. x, the end=' ' is used to place a space after the displayed string instead of a newline.

# # (6) substring
# # https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/
# string = "freeCodeCamp"
# print(string[0:5])
#
# string = "freeCodeCamp"
# print(string[2:6])
#
# string = "freeCodeCamp"
# print(string[-1])
#
# string = "freeCodeCamp"
# print(string[-5:])
#
# string = "freeCodeCamp"
# print(string[1:-4])
#
# str = “freeCodeCamp”
#
# print str[-5:-2] # prints ‘eCa’
# print str[-1:-2] # prints ‘’ (empty string)
#
# string = "freeCodeCamp"
# print(string[::2])

# # (7) Escaping
# print('It\'s a tie.') # \'

# # (8) ord() and chr()
# start_character = "A"
# end_character = "Z"
#
# counter = ord(start_character)
#
# for i in range(ord(start_character), ord(end_character) + 1):
#     print(chr(i))

# (9) Escape Codes: \b, \t, \n, \a, \r https://www.w3schools.com/python/gloss_python_escape_characters.asp

# # (10) variable outside of function
# def greeting(input_name):
#     return "Hi " + a_name + "!"
#
# a_name = "David"
# message = greeting(a_name)
# print(message)

# # (11) global key word
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)

# # (12) Key parameter
# #Defines the function "currencyAmount"
# def currencyAmount(amount, currency = "USD"):
#     if currency == "JPY":
#         return "¥" + str(amount)
#     elif currency == "USD":
#         return "$" + str(amount)
#     elif currency == "GBP":
#         return "£" + str(amount)
#     else:
#         return str(amount)
#
# #Prints the output of currencyAmount(5)
# print(currencyAmount(5))
# #Prints the output of currencyAmount(5, currency = "GBP")
# print(currencyAmount(5, "GBP"))
# print(currencyAmount(5, currency = "GBP"))

# # (13) intertool module
# def is_prime(n):
#     from itertools import count, islice
#     return n > 1 and all(n % i for i in islice(count(2), int(n**0.5)-1))
#
# print(sum_of_primes(6))
# print(sum_of_primes(7))
# print(sum_of_primes(8))
# print(sum_of_primes(11))

# # (14) Try / Except
# try:
#     my_var = 1 / 0
#     print("An error occurred!")
# except:
#     pass
# print("Done!")
#
# # Line 2 causes an error, but line 2 is indented under a try block. So, the error is caught,
# # and the program can keep running. So, it reaches and runs line 6.
# # Note that this is not the right way to use a try block!

# # (15) Try / Except 2
#
# try:
#     my_var = 1 / 0
#     print("No error occurred!")
# except:
#     print("An error occurred!")
# print("Done!")
#
# # The line that causes the error is inside a try block, so the program jumps to the except block.
# # Then, it runs the code inside the except block (line 4) before continuing to line 5.
# # Note that this is the correct way to use a try block!

# # (16) Try / Except 3
#
# try:
#     my_var = 1 / 1
#     print("No error occurred!")
# except:
#     print("An error occurred!")
# print("Done!")
#
# # No errors occur inside the try block, so the except block is never run.
# # This is the correct way to use an except block!

# # (17) Catching a Specific Error
# try:
#     print(1 / 0)
#     print("No error occurred!")
# except ZeroDivisionError:
#     print("An error occurred!")
# print("Done!")

# # (18) Catching a Specific Error 2
# try:
#     print(1 / 0)
#     print("No error occurred!")
# except NameError:
#     print("An error occurred!")
# print("Done!")

# Line 2 causes an error, but line 2 is indented under a try block.
# So, the error is caught, and the program jumps to the except block.
# The error caused by line 2 is a ZeroDivisionError, but line 4 only handles NameErrors.
# So, this type of error isn't handled by the except block.
# Because the error therefore isn't caught, the error message is printed.

# # (19) Catching Multiple Specific Errors
# try:
#     print(1 / 0)
#     print("No error occurred!")
# except NameError:
#     print("A NameError occurred!")
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred!")
# print("Done!")

# # (20) Catching Multiple Specific Errors
# try:
#     print(undeclared_variable)     #This line causes a NameError
#     print(1 / 0)                   #This line causes a ZeroDivisionError
#     print("No error occurred!")
# except NameError:
#     print("A NameError occurred!")
# except ZeroDivisionError:
#     print("A ZeroDivisionError occurred!")
# print("Done!")
#
# # Two errors occur inside the try block, but the code only runs until it encounters the first one:
# # as soon as it encounters the first, it jumps over the rest of the try block and starts to check
# # the except blocks. So, the NameError on line 2 will cause its except block to run instead of
# # the ZeroDivisionError.

# # (21) except Exception as
# try:
#     asdsd
# except Exception as e:
#     print(e)

# # (22) try except as Exception
# try:
#     print("Converting into interger")
#     print("stirng " + 1 + my_string)
#     myint = int(my_string)
#     print(myint)
#     print(1/0)
# except (ValueError, TypeError) as error:
#     print(error)
#     print("Value error or type error occured")
# except Exception as error:
#     print(error)
#     print("Some other type of error occured")
# print("Done!")

# # (23) try except as Exception 2
# try:
#     print("Converting into interger")
#     print("stirng " + 1 + my_string)
#     myint = int(my_string)
#     print(myint)
#     print(1/0)
# except Exception as error:
#     print(error)
#     print("Some other type of error occured")
# except (ValueError, TypeError) as error:
#     print(error)
#     print("Value error or type error occured")
#
# print("Done!")

# # (23) try except as Exception Else
# my_string = 1
# try:
#     print("Converting into interger")
#     myint = int(my_string)
#     print(myint)
# except Exception as error:
#     print(error)
#     print("Some other type of error occured")
# except (ValueError, TypeError) as error:
#     print(error)
#     print("Value error or type error occured")
# else:
#     print("No error occured") # Try block does not have error -> go to else after try
#
# print("Done!")

# # (24) When error not catched
# my_other_var = 1
# try:
#     result = 10 // my_var
#     print(result)
# except (ZeroDivisionError, TypeError):
#     print("An expected error occurred!")
# else:
#     print("No errors occurred!")
# finally:
#     print("Closing down...")
# print("Done!")

# # (25) index()
# words = ["dog", "sparrow", "cat", "frog"]
#
# for word in words:
#     try:
#         print(word.index("o"))
#     except:
#         print("Not found")

# # (26) error handling in function
# def find_pressure(moles, temp, volume, R=0.082057):
#     try:
#         return moles * R * temp / volume
#     except ZeroDivisionError:
#         return "Volume must be greater than 0."
#
# test_n = 10
# test_T = 298
# test_V = 0
# test_R = 62.364 #Torr!
# print("Result:", find_pressure(test_n, test_T, test_V, R = test_R))

# # (27) Invalid index
# a_list = [1, 2, 3, 4, 5]
# list_index = 7
#
# print("Accessing index...")
# try:
#     result = a_list[list_index]
#     print("Value at index:", result)
# except IndexError:
#     print("Invalid index!!")
# except:
#     print("Unknown error!")
# finally:
#     print("Done!")

# # (28) count()
# s = "a2323a1232a422a"
# print(s.count('a'))
