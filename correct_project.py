# Function to read nymbers from file. Takes in the filename as parameter
def read_numbers_from_file(filename):
    # 'open' opens the filename. 'With' also closes the file. 'R' means reading
    with open(filename, 'r') as file:
        # creates a list of numbers extracted from each line in the file?
        #  stripping any whitespace and converting each line to a float.
        numbers = [float(line.strip()) for line in file.readlines()]
        # Returns the list of numbers
    return numbers

# Function to calculate the average
def calculate_average(numbers):
    #  returnes mean
    return sum(numbers) / len(numbers)
#  function to update the file name with the average

def write_average_to_file(filename, average):
    # With closes the file after, open opens the file, 'w' means write
    with open(filename, 'w') as file:
        # write method updates 
        file.write(f'The average is: {average:.2f}')

# defining main function
def main():
    # variables to hold filenames
    input_filename = 'numbers.txt'
    output_filename = 'average.txt'
    # var numbers = list of numbers from the file
    numbers = read_numbers_from_file(input_filename)
    # var average = mean average from the files
    average = calculate_average(numbers)
    # updates the file with the mean average 
    write_average_to_file(output_filename, average)

# runs function 'main' if __name__ = '__main__'
if __name__ == '__main__':
    main()
