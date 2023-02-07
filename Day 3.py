Age = 12
Height = 1.65
complex = (1 + 1j)

base = int(input('enter a base number of a triangle   '))
h = int(input('enter a height number of a triangle   '))
area = 0.5 * base * h
print('The area of the triangle is ', area)

a = int(input('enter side a  '))
b = int(input('enter side b  '))
c = int(input('enter side c  '))
perimeter = a + b + c
print('The perimeter of the triangle is ', perimeter)

length = int(input('enter a length number of a rectangle   '))
width = int(input('enter a base number of a width   '))
Area = length * width
Perimeter = 2 * (length + width)
print('Area of rectangle =  ', Area)
print('Perimeter of rectangle =  ', Perimeter)

radius = int(input('enter a radius number of a circle  '))
area_circle = 3.142 * radius * radius
circumference = 2 * 3.142 * radius
print('Area of circle =  ', area_circle)
print('circumference of circle =  ', circumference)

x1 = int(input('enter a x-intercept of a circle  '))
x2 = int(input('enter a x2-intercept of a circle  '))
y1 = (2 * x1) - 2
y2 = (2 * x2) - 2
m = (y2-y1)/(x2-x1)

print(len('python'))
print(len('dragon'))
print('python' is 'dragon')
print('on' in 'dragon' and 'on' in 'python')
print('jargon' in 'I hope this course is not full of jargon')

value = len('python')
print(float(value))
print(str(value))

num = int(input('enter a number  '))
print(num % 2 is 0)
print(7 // 3 is 2.7)

print(type('10') is type(10))
print(9.8 is 10)

hours = int(input('enter the number of hours:  '))
rate = int(input('enter the rate per hour:  '))
print(hours * rate)

years = int(input('enter the number of years:  '))
print(years * 365 * 24 * 60 * 60)
