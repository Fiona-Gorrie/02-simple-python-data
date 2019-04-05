def calculate_rectangle_area(height, width):    
    rectangle_area = height * width 
    return rectangle_area

def calculate_area_of_square(side):
    square_area = side**2
    return square_area

def calculate_total_plus_tip_per_person(total_bill, tip_percent, number_of_people):
    total_plus_tip = total_bill + (total_bill * tip_percent)
    total_plus_tip_per_person = total_plus_tip / number_of_people
    return total_plus_tip_per_person

def fahrenheit_to_celcius(degrees):
    degrees_in_celcius = (degrees - 32) * (5/9) 
    return degrees_in_celcius

def calculate_the_remainder(num1, num2):
    remainder = num1%num2
    return remainder
