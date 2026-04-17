#Task 1
def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                count += 1
    return count

#Task 2
def find_keyword_lines(filename, keyword):
    line_numbers = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                line_numbers.append(i)
    return line_numbers

#Task 3
def convert_to_uppercase(filename):
    with open(filename, 'r') as file:
        content = file.read()
    with open('output.txt', 'w') as output:
        output.write(content.upper())

#Task 4
def average_score(filename):
    total = 0
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')  # split into name and score
            total += int(score)
            count += 1
    return total / count if count > 0 else 0