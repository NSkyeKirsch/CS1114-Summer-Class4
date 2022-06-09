a_list = []

mixed_list = [1, 2, 'a', 'string', 3.45]

list_of_schools = [['NYU', 'Columbia', 'Yale'], [1, 2, 3]]

tuple_dude = (3, 4)

# =========================

another_list = list("Hello New York")  # can't do this with ints, only strings
print(another_list)  # every character was separated into items
print()

# =========================

heroes = ["Spiderman", "Batman", "Superman", "CatWoman", "Ms. Marvel", "She-Hulk"]

print("heroes before:", heroes)

heroes[1] = 'Black Widow'

print("heroes after:", heroes)

heroes[2] = ["Thor", "Jane"]

print("after after:", heroes)

# heroes[4] = 'Iron Man'  <---- do not do this because [4] is out of scope! Must use .append() or other method
print()

heroes[:2] = "Someone else"  # indexes 0-1 are overwritten by "Someone else"
print(heroes)
print()

heroes = ['Spiderman', 'Black Widow', ['Thor', 'Jane'], 'CatWoman', 'Ms. Marvel', 'She-Hulk']

heroes[2:4] = ["Nick Fury"]  # "Nick Fury" replaces both ['Thor', 'Jane'] and 'CatWoman'
print(heroes)
print()

heroes = ['Spiderman', 'Black Widow', ['Thor', 'Jane'], 'CatWoman', 'Ms. Marvel', 'She-Hulk']

print(heroes[2][heroes[2].index("Thor")])  # find 'Thor' in the sublist and print
print()

# =========================

numbers = [['NYU', 'Columbia', 'CUNY'], ['BC', 'BU', 'Tufts'], ['Penn', 'Drexel', 'Temple']]
print(list_of_schools)

list_of_schools.append(['UCLA', 'USC', 'CalTech', 'LMU'])  # adds ONE element to the end of the list
print(list_of_schools)

list_of_schools.extend(['UChicago', 'Northwestern'])  # extend takes in a list, opens it, and appends each item
print(list_of_schools)

# =========================

# you can use + and * with lists

captains = ['Kirk', 'Picard']
other_crew = ['Number 1', 'Data', 'Wesley']

list_a = captains + other_crew
print(list_a)

list_b = captains * 5
print(list_b)

comparison_result = [1, 3, 5] < [1, 3, 3]
print(comparison_result)
print()

# you can use >, <, <=, >=, ==, != operators on lists

# list membership - boolean operand - in
if 'Kirk' in list_a:
    print("Long live Kirk")
else:
    print("RIP")

print()

# List slicing

a_list = [1, 2, 'a', 'nyu', 3.1415927, True, "red", 21]

new_list = a_list[:]
print(new_list)

new_list = a_list[1:5]
print(new_list)

new_list = a_list[1:8:3]
print(new_list)

new_list = a_list[-1:0:-2]
print(new_list)



