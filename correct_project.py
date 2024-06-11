def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [float(line.strip()) for line in file.readlines()]
    return numbers

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def write_average_to_file(filename, average):
    with open(filename, 'w') as file:
        file.write(f'The average is: {average:.2f}')

def main():
    input_filename = 'numbers.txt'
    output_filename = 'average.txt'
    
    numbers = read_numbers_from_file(input_filename)
    average = calculate_average(numbers)
    write_average_to_file(output_filename, average)

if __name__ == '__main__':
    main()
