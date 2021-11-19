# # (1) Declaring a Class
#
# class Person:
#
#     def __init__(self):  #when we create a new Person, we want to give some default values to the names and eye color that emphasize that the real values haven’t yet been supplied.
#         self.firstname = ""
#         self.lastname = ""
#         self.eyecolor = ""
#         self.age = -1
#
# jake = Person()
# print(jake.firstname)
# jake.firstname = "jake"
# print(jake.firstname)

# # (2) Declaring a Class 2
#
# class Name:
#     def __init__(self):
#         self.firstname = ""
#         self.lastname = ""
#
# class Person:
#     def __init__(self):
#         self.name = Name()
#         self.eyecolor = ""
#         self.age = -1
#
# jake = Person()
# print(jake.name.firstname)
# jake.name.firstname = "jake"
# print(jake.name.firstname)

# # (3) Constructor
# class Person:
#
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.eyecolor = ""
#         self.age = -1
#
# jake = Person("jake", "youn")
# print(jake.firstname, jake.lastname)

# # (4) Constructor 2
# class Person:
#
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.eyecolor = ""
#         self.age = -1
#
# jake = Person() # Error! Positional Arguments needs to be filled
# print(jake.firstname, jake.lastname)

# # (5) Constructor 3
# class Person:
#
#     def __init__(self, firstname = "", lastname = ""):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.eyecolor = ""
#         self.age = -1
#
# jake = Person() # Optional Argements do not need to be filled!
# print(jake.firstname, jake.lastname)

# # (6) Combining Classes
# #Defines the class Person
# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age
#
# #Defines the class Name
# class Name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# #Creates a person with eyecolor "brown", age 30, and
# #a name with firstname "David", lastname "Joyner",
# myPerson = Person(Name("David", "Joyner"), "brown", 30)
# print(myPerson.name.firstname)
# print(myPerson.name.lastname)
# print(myPerson.eyecolor)
# print(myPerson.age)

# # (7) Instance Assignment
# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age
#
# #Defines the class Name
# class Name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
# myPerson2 = myPerson1
# myPerson2.eyecolor = "blue"
# print(myPerson1.eyecolor) #blue -> Person class is mutable!

# # (8) Instance as Argument
# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age
#
# #Defines the class Name
# class Name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# def capitalizeName(name):
#     name.firstname = name.firstname.upper()
#     name.lastname = name.lastname.upper()
#
# myPerson = Person(Name("David", "Joyner"), "brown", 30)
# capitalizeName(myPerson.name)
# print(myPerson.name.firstname, myPerson.name.lastname) # Name() is mutable -> when passed as argument, the passed instance can be changed

# # (9) Otherwise passing string ....
# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age
#
# #Defines the class Name
# class Name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# def capitalizeString(name):
#     name = name.upper()
#
# myPerson = Person(Name("David", "Joyner"), "brown", 30)
# capitalizeString(myPerson.name.firstname)
# capitalizeString(myPerson.name.lastname)
# print(myPerson.name.firstname, myPerson.name.lastname) # string is not mutable!

# # (10) Making Actual Copies - Fail
# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age
#
# #Defines the class Name
# class Name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
# myPerson2 = Person(myPerson1.name, myPerson1.eyecolor, myPerson1.age)
# myPerson2.name.firstname = "jake"
# myPerson2.age = 29
# print(myPerson1.name.firstname, myPerson2.name.firstname, myPerson1.age, myPerson2.age)

# # (11) Making Actual Copies - Success
# class Person:
#     def __init__(self, name, eyecolor, age):
#         self.name = name
#         self.eyecolor = eyecolor
#         self.age = age
#
# #Defines the class Name
# class Name:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
# myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
# myPerson2 = Person(Name(myPerson1.name.firstname, myPerson1.name.lastname), myPerson1.eyecolor, myPerson1.age)
# myPerson2.name.firstname = "jake"
# myPerson2.age = 29
# print(myPerson1.name.firstname, myPerson2.name.firstname, myPerson1.age, myPerson2.age)

# # (12) Bubble Sort
# def sort_with_bubbles(lst):
#     # Set swap_occurred to True to guarantee the loop runs once
#     swap_occurred = True
#
#     # Run the loop as long as a swap occurred the previous time
#     while swap_occurred:
#
#         # Start off assuming a swap did not occur
#         swap_occurred = False
#
#         # For every item in the list except the last one...
#         for i in range(len(lst) - 1):
#
#             # If the item should swap with the next item...
#             if lst[i] > lst[i + 1]:
#
#                 temp = lst[i]
#                 lst[i] = lst[i + 1]
#                 lst[i + 1] = temp
#                 swap_occurred = True
#
#     return lst
#
# print(sort_with_bubbles([5, 3, 1, 2, 4]))

# # (13) Selection Sort
# def sort_with_select(a_list):
#     # For each index in the list...
#     for i in range(len(a_list)):
#
#         minIndex = i
#         for j in range(i + 1, len(a_list)):
#
#             if a_list[j] <= a_list[minIndex]:
#                 minIndex = j
#
#         minValue = a_list[minIndex]
#         del a_list[minIndex]
#         a_list.insert(i, minValue)
#
#     return a_list
#
# print(sort_with_select([5, 3, 1, 2, 4]))

# # (14) Merge Sort
# def mergesort(lst):
#     if len(lst) <= 1:
#         return lst
#
#     else:
#
#         midpoint = len(lst) // 2
#
#         left = mergesort(lst[:midpoint])
#         right = mergesort(lst[midpoint:])
#
#         newlist = []
#         while len(left) and len(right) > 0:
#
#             if left[0] < right[0]:
#                 newlist.append(left[0])
#                 del left[0]
#
#             else:
#                 newlist.append(right[0])
#                 del right[0]
#
#         newlist.extend(left)
#         newlist.extend(right)
#
#         return newlist
#
# print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))

# # (15) Binary Search
# def binary_search(searchList, searchTerm):
#     searchList.sort()
#
#     min = 0
#     max = len(searchList) - 1
#
#     while min <= max:
#
#         currentMiddle = (min + max) // 2
#
#         if searchList[currentMiddle] == searchTerm:
#             return True
#
#         elif searchTerm < searchList[currentMiddle]:
#             max = currentMiddle - 1
#
#         else:
#             min = currentMiddle + 1
#
#     return False
#
#
# intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
# print("23 is in intlist:", binary_search(intlist, 23))
# print("50 is in intlist:", binary_search(intlist, 50))
#
# strlist = ["David", "Joshua", "Marguerite", "Jackie"]
# print("David is in strlist:", binary_search(strlist, "David"))
# print("Lucy is in strlist:", binary_search(strlist, "Lucy"))
#
# from datetime import date
#
# datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
# print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
# print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))

# # (16) Linked List
# class LinkedListNode:
#     def __init__(self, value, next_node=None):
#         self.value = value
#         self.next_node = next_node
#
#
# # Write your function here!
# def linked_list_search(l, t):
#     while l is not None:
#         if l.value == t:
#             return True
#         l = l.next_node
#     return False

# # (17) Binary Tree Search
# class Node:
#     def __init__(self, value, left = None, right = None):
#         self.value = value
#         self.left = left
#         self.right = right
#
# #Write your binary_tree_search function here!
# def binary_tree_search(r, t):
#     if r is None:
#         return False
#     if t == r.value:
#         return True
#     elif t < r.value:
#         return binary_tree_search(r.left, t)
#     else:
#         return binary_tree_search(r.right, t)
#
# root_node = Node(10)
# root_node.left = Node(5)
# root_node.right = Node(15)
# root_node.left.left = Node(3)
# root_node.left.right = Node(7)
# root_node.right.left = Node(12)
# root_node.right.right = Node(18)
#
# print(binary_tree_search(root_node, 18))
# print(binary_tree_search(root_node, 7))
# print(binary_tree_search(root_node, 15))