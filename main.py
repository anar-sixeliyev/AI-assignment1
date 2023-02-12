def read_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        second_line = int(file.readline().strip())
        first_line_list = [int(x) for x in first_line.split(',')]
        return (first_line_list, second_line)

print(read_file('sample01.txt')) 