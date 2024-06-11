def read_integers_from_file(filename):
    with open(filename, 'r') as file:
        integers = [int(line.strip()) for line in file.readlines()]
    return integers

def filter_even_numbers(integers):
    return [number for number in integers if number % 2 == 0]

def write_filtered_numbers_to_file(filename, integers):
    with open(filename, 'w') as file:
        for number in integers:
            file.write(f'{number}\n')

def main():
    input_filename = 'integers.txt'
    output_filename = 'filtered_numbers.txt'
    
    integers = read_integers_from_file(input_filename)
    filtered_numbers = filter_even_numbers(integers)
    write_filtered_numbers_to_file(output_filename, filtered_numbers)

if __name__ == '__main__':
    main()
