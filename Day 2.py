# Day 2: 30 Days of python programming
# Level 1
first_name = 'Mahmoud'
last_name = 'Said'
full_name = 'Mahmoud Said Ahmad'
country = 'Nigeria'
city = 'Kano'
age = 16
year = 2023
is_married = False
is_true = True
is_light = False
a, b, c, d = 4, "amir", 3.14, True

# level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(len(first_name))

print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

radius = 30
radius = int(input("Enter the radius: "))
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print('area of circle =', area_of_circle)
print('circumference of circle =', circum_of_circle)


# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
First_name = str(input('enter first name: '))
Last_name = str(input('enter last name: '))
Country = str(input('enter country: '))
Age = int(input('enter age: '))
print(First_name, Last_name, Country, Age)
help('keywords')
