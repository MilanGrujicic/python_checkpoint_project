import math

def start_calculator():
    print('''
    ==================
    Area Calculator 📐
    ==================
        
        1) Triangle
        2) Rectangle
        3) Square
        4) Circle
        5) Quit
    ''')

def calculate_area_triangle():
    base = float(input('Base (m): '))
    height = float(input('Height (m): '))
    area = (base * height) / 2
    print(f'The area of the triangle with base {base}m and height {height}m is {area}m²')

def calculate_area_rectangle():
    length = float(input('Length (m): '))
    width = float(input('Width (m): '))
    area = (length * width)
    print(f'The area of the rectangle with length {length}m and width {width}m is {area}m²')

def calculate_area_square():
    side = float(input('Side (m): '))
    area = math.pow(side, 2)
    print(f'The area of the square with sides {side}m is {area}m²')

def calculate_area_circle():
    radius = float(input('Radius (m): '))
    area = math.pi * math.pow(radius, 2)
    print(f'The area of the square with radius {radius}m is {area:.2f}m²')

while True:
    start_calculator()
    user_input = int(input('Which shape: '))
    if user_input == 1:
        calculate_area_triangle()
    elif user_input == 2:
        calculate_area_rectangle()
    elif user_input == 3:
        calculate_area_square()
    elif user_input == 4:
        calculate_area_circle()
    elif user_input == 5:
        print('Bye bye.👋')
        break
    else:
        print('Wrong input please select one of the options below')