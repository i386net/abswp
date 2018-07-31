table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose'],
              ['hp', 'lg', 'apple', 'samsung']]


def print_table(input_list):
    # initialize the list "col_widths" with zeroes equal to the length of the input list
    col_widths = [0] * len(input_list)

    # iterate over the input list to find the longest word in each inner list
    # if its larger than the current value, set it as the new value
    for i in range(len(input_list)):
        for j in range(len(input_list[i])):
            if len(input_list[i][j]) > col_widths[i]:
                col_widths[i] = len(input_list[i][j])

    # assuming each inner list is the same length as the first, iterate over the input list
    # printing the x value from each inner list, right justifed to its corresponding value
    # in col_widths
    for x in range(len(input_list[0])):
        for y in range(len(input_list)):
            print(input_list[y][x].rjust(col_widths[y]), end=' ')
        print('')


print_table(table_data)
