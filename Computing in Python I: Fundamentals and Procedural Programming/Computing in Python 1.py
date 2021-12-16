# #(1) type function
# #Put your code here!
# my_integer = 3
# my_decimal = 1.1
# my_string = "haha"
# my_boolean = False
#
#
# #Don't modify these next lines! They're used for grading, and
# #if they aren't present exactly as they appear below, your
# #submission will fail!
# print(type(my_integer))
# print(type(my_decimal))
# print(type(my_string))
# print(type(my_boolean))

# #(2) date library
#
# from datetime import date
#
# #Creates aDate with the value of today's date
# aDate = date.today()
#
# print(aDate)

# #(3) Null value
#
# a = None
# print(a)

# # (4) type function
#
# from datetime import date
# import random
# a = "Hello, world!"
# b = date.today()
# c = random.randint(0,100)
# d = random
#
# #Don't modify anything above this line!
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# # (5) Mixed Type
# a_int = 2
# a_float = 1.1
# a_str = "abc"
# a_true = True
# a_false = False
#
# print(a_int * a_str)
# print(a_float * a_true) #True becomes 1
# print(a_float * a_false) #False becomes 0
# print(a_int * a_true) #True becomes 1
# print(a_false * a_str) #Fasle becomes 0
# print(a_true * a_str) #True becomes 1
# print(3 * a_true * a_str) #True becomes 1
# print(a_float * a_str)

# # (6) assign print to a variable
# d = print(1) #print 1 and assgin None to d
# print(d)

# # (7) max function
# high = max(1, 2, 3, 4, 5)
# print(high)

# (8) how to use %d in print
# quotient = num_1 // num_2
# print("The quotient is %d" % (quotient))
#
# remainder = num_1 % num_2
# print("The remainder is %d" % (remainder))

# # (9) Type Conversion to str
# from datetime import date
# integer_as_string = str(8)
# float_as_string = str(8.2)
# date_as_string = str(date.today())
# boolean_as_string = str(False)
#
# #The lines of code below will test your code.
# #If it works, they will print the four string
# #values, each followed by "<class 'str'>".
# print(integer_as_string, type(integer_as_string))
# print(float_as_string, type(float_as_string))
# print(date_as_string, type(date_as_string))
# print(boolean_as_string, type(boolean_as_string))

# # (10) User Input
# a = input("Give me that shit : ")
# print(a)
# print(a * a) #TypeError. input() always interprets user input as str

# # (11) Reserved Keywords
# import keyword
#
# print(keyword.kwlist)

# # (12) Misused Reserved Keywords
# pass = 1 #syntax error
# def except(num):    #syntax error
#     return

# # (13) Current date and time
# from datetime import date
# import datetime
# todays_date = date.today()
# current_time = datetime.datetime.now()
#
# print(str(todays_date.year) + "/" + str(todays_date.month) + "/" + str(todays_date.day))
# print(str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second))

# # (14) Date
# from datetime import date
# import random
# earlier_date = date(2017, 6, random.randint(1, 25))
# later_date = date(2017, 6, random.randint(earlier_date.day + 1, 28))
#
# days_between = later_date.day - earlier_date.day
# earlier_date = earlier_date
# later_date = later_date
#
# print("There are", days_between, "days between", earlier_date, "and", later_date)

# # (15) Six logical operations
#
# a = True
# b = False
#
# #There are six logical operations to compare two boolean
# #values. They are:
# #
# #  And: True if both are True, False otherwise
# #   Or: True if either is True, False otherwise.
# #  Xor: True if exactly one is True; False if both are True
# #       or both are False ("Exclusive Or")
# # Nand: False if both are True, True otherwise.
# #  Nor: False if either is True, True otherwise.
# # Xnor: False if exactly one is True; True if both are True
# #       or both are False.
# #
#
#
# print("And:", a and b)
# print("Or:", a or b)
# print("Xor:", a and not b or not a and b)
# print("Nand:", not (a and b))
# print("Nor:", not (a or b))
# print("Xnor:", not(a and not b or not a and b))

# # (16) import pi
#
# q1 = 5
# q2 = -10
# r = 5
#
# from math import pi
# e = 8.854 * 10 ** -12
#
# val_1 = (1 / (4 * pi * e))
# val_2 = (q1 * q2) / r
#
# print("The electric potential energy is", round((val_1 * val_2), 2))

# # (17) left to right
# print(9 / 2 // 2) #print 2.0

# # (18) ** and * -> ** first
# print(2 ** 6 * 2) #print 128
# print(2 * 2 ** 6) #print 128

# # (19) Import e
#
# A = 50
# T = 301
# n = 0.5
# Ea = 30
# R = 0.8268
#
# from math import e
#
# #Write your code here!
# print( round(A * T**n * e**(-Ea/(R * T)), 2))
#
# # (20) round()
# print(round(361))
# print(round(1.3))
# print(round(1.2557, 3))

# # (21) 0.1f
#
# my_current_average = 87.1
# survey_completers = 50
# class_size = 100
# bonus = round(survey_completers / class_size, 1)
# average = my_current_average + bonus
# print("After the %.1f point bonus, my average is %f." % (bonus, average))
# print("After the %.1f point bonus, my average is %.1f." % (bonus, average))
# print("After the %.1f point bonus, my average is %.2f." % (bonus, average))

# # (22) Int and Boolean mix
#
# print(2*(True + True))
# print(2*(True + False))
# print(5 * False)
# print(3 + True + False + True)
# print(True + True)
# print(False + True)
# print(True)
# print(False)

# (23) Format()

# txt = "For only {price:.2f} dollars!"
# print(txt)
# print(txt.format(price = 49))
#
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
