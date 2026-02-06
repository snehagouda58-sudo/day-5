def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area, perimeter = calc_rectangle(length, width)
print("Area:", area, "Perimeter:", perimeter)



def power(base, exp):
    return base ** exp
def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)
import math_operator
result_power = math_operator.power(6, 3)
numbers = [40, 50, 60, 70]
result_average = math_operator.average(numbers)
print("6^3 =", result_power)
print("Average =", result_average)