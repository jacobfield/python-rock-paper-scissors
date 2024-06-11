# file should extract a list of odd numbers from the file, and add them to another file.
# There is an error, in that it extracts a list of even numbers instead of odd


#  function to read intefers from file. Takes in filename
def read_integers_from_file(filename):
    #  opens and closes filename for reading
    with open(filename, 'r') as file:
        #  strips the integers from the file and saves to var integers
        integers = [int(line.strip()) for line in file.readlines()]
    # returns the list of intefers
    return integers

# function to filter the even numbers from the list
def filter_even_numbers(integers):
    # for loop that returns current number from list if the number is even
    #  - This overwrites integers
    # Bug is here - it filters out odd numbers, not evens
    return [number for number in integers if number % 2 == 0]

# function to write to the file, just the even nums
def write_filtered_numbers_to_file(filename, integers):
    # opens and closes the file, and writes to it
    with open(filename, 'w') as file:
        #  for each number in integers list
        for number in integers:
            # write that number
            file.write(f'{number}\n')

# main funciton
def main():
    # variables to save filenames
    input_filename = 'integers.txt'
    output_filename = 'filtered_numbers.txt'
    # calling the intefers function
    integers = read_integers_from_file(input_filename)
    # calling the filtered_numbers function
    filtered_numbers = filter_even_numbers(integers)
    # calling the filtered numbers to the file
    write_filtered_numbers_to_file(output_filename, filtered_numbers)
# conditionally running the function
if __name__ == '__main__':
    main()
