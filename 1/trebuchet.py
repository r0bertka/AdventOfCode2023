import re

def load_data(file_path):
    data = []
    with open(file_path) as file:
        for line in file:
            data.append(line.split('\n')[0])
        return data

def find_numbers(string):
    numbers = re.findall(r'[1-9]', string)
    return numbers[0], numbers[-1]

def extract_relevant_digits(data):
    digits = []
    for string in data:
        digits.append(find_numbers(string))
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
relevant_digits = extract_relevant_digits(data)
list_of_numbers = concatenate_digits_to_numbers(relevant_digits)
sum = calculate_calibration_value(list_of_numbers)
print(sum)