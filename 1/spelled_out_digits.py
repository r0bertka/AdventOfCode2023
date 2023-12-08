import re
import numpy as np

def load_data(file_path):
    data = []
    with open(file_path) as file:
        for line in file:
            data.append(line.split('\n')[0])
        return data

def replace_spelled_out_digits(string):
    patterns = np.array([('one', 'one1one'),
                         ('two', 'two2two'),
                         ('three', 'three3three'),
                         ('four', 'four4four'),
                         ('five', 'five5five'),
                         ('six', 'six6six'),
                         ('seven', 'seven7seven'),
                         ('eight', 'eight8eight'),
                         ('nine', 'nine9nine')])
    for (spelled_out_digit, digit) in patterns:
        if string.find(spelled_out_digit) != -1:
            string = string.replace(spelled_out_digit, digit)
    return string

def find_numbers(string):
    numbers = re.findall(r'[1-9]', replace_spelled_out_digits(string))
    if numbers:
        return numbers[0], numbers[-1]
    else:
        print('DÄÄÄÄT')
        return '0', '0'

def extract_relevant_digits(data):
    digits = []
    for string in data:
        digits.append(find_numbers((string)))
    return digits

def concatenate_digits_to_numbers(digit_tuples):
    numbers = []
    for tuple in digit_tuples:
        numbers.append(int(tuple[0] + tuple[1]))
    return numbers

def calculate_calibration_value(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


data = load_data('input.txt')
print(data)
digits = extract_relevant_digits(data)
print(digits)
numbers = concatenate_digits_to_numbers(digits)
print(numbers)
sum = calculate_calibration_value(numbers)
print(sum)