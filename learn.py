# python dictionaries, nesting
# dictionaries are used to group together and tag related pieces of information
# it is a key value kind of thing.
programming_dictionary = {
    "bug":"An error in a program that prevents the program from running as expected",
    "function":"a piece of code that you can call over and over again",
    "loop":"the action of doing something over and over again"
}
# to access elements in a dictionary
print(programming_dictionary["bug"])
print(programming_dictionary["function"])
# the data types for the keys of a dictionary should be a string

# what if we wanted to add a piece of data to our dictionary
programming_dictionary["parameter"] = "placeholder for the real data that is supposed to be passed into a function"
print(programming_dictionary)

# to wipe an existing dictionary
# programming_dictionary = {}

# looping through a dictionary
for key in programming_dictionary:
    print(key)#prints the keys
    print(programming_dictionary[key])

# coding challenge
# grading exercise
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# convert scores above into grades and put them into a new dictionary
student_grades = {}
for student in student_scores:
    # score = student_scores[student]
    if student_scores[student] > 91:
        student_grades[student] = "outstanding"
    elif student_scores[student] >= 81 and student_scores[student] < 91:
        student_grades[student] = "exceeds expectation"
    elif student_scores[student] > 71 and student_scores[student] < 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] <= 70:
        student_grades[student] = "fail"
print(student_grades)

# NESTING LISTS AND DICTIONARIES
# we can use a list as a value for a key or even another dictionary as a valur for a key in the dictionary, we can also place dictionaries inside a list
capitals = {
    "france":"Paris",
    "Germany":"Berlin"
}
travel_log = {
    "france":["Paris", "Lille", "Dijon"],
    "Kenya": ["Busia", "Kisumu", "Kirinyaga"]
}
# we can also nest a list in a list
nested_list = ["a", "b", ["c", "d"]]

# nesting dictionaries inside of dictionaries
travel_log = {
    "france": {
        "cities_visited":["Paris", "Lille", "Dijon"],
        "number of visits": 3
    }
}
# we can also nest dictionaries inside a list
[{"name":"dennis", "age": 22}, {"name":"sumbra", "age": 24}, {"name":"kelvin", "age": 42}]

# coding challenge
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countriesto be added to the travel_log. 👇
def add_new_country(name, no_of_visits, cities):
    new_country = {}
    new_country["country"] = name
    new_country["visits"] = no_of_visits
    new_country["cities"] = cities
    travel_log.append(new_country)

add_new_country("Texas", 5, ["tennese", "jeffersonville"])
print(travel_log)
