# Python Variables

#   As Python is dynamically typed, we cannot implicitly state 
#   the type of the variable while declaration / initialization

x = 1 

#   Proof that Python is a dynamic typed language
#   Here the variable x was initially of type integer
#   But after it was assigned with a float value, the type dynamically changed to float

x = 1
print(type(x), x)

x = 1.0
print(type(x), x)
