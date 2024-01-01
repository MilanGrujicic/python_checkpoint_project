import math

def start():
    print('''
    ================
    Area Calculator
    ================
        
        1) Triangle
        2) Rectangle
        3) Square
        4) Circle
        5) Quit
    ''')

def area_triangle():
    base = float(input('Base: '))
    height = float(input('Height: '))
    area = (base * height) / 2
    print(f'The area is {area}')

def area_rectangle():
    length = float(input('Length: '))
    width = float(input('Width: '))
    area = (length * width) / 2
    print(f'The area is {area}')

def area_square():
    side = float(input('Side: '))
    area = math.pow(side, 2)
    print(f'The area is {area}')

def area_circle():
    radius = float(input('Radius: '))
    area = math.pi * math.pow(radius, 2)
    print(f'The area is {area}')

while True:
    start()
    user_input = int(input('Which shape: '))
    if user_input == 1:
        area_triangle()
    elif user_input == 2:
        area_rectangle()
    elif user_input == 3:
        area_square()
    elif user_input == 4:
        area_circle()
    elif user_input == 5:
        break
    else:
        print('Wrong input please select one of the options below')