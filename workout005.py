#!/usr.bin/python
# coding UTF-8
"""coding like a python
   LIst Comprehension
"""

my_list1 = [n+1 for n in range(0, 3)]
print(my_list1)  # [1, 2, 3]

# old fashion another coding
my_list2 = []
for n in range(0, 3):
    my_list2.append(n+1)
print(my_list2)

