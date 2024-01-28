def fizzbuzz(x, y, z):
    result = []
    for i in range(1, 21):
        if i % x == 0 and i % y == 0:
            result.append("FizzBuzz")
        elif i % x == 0:
            result.append("Fizz")
        elif i % y == 0:
            result.append("Buzz")
        else:
            result.append(str(i * z))
    return result

input_file = "listH3-1.py"
output_file = "output.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        numbers = list(map(int, line.strip().split()))
        result = fizzbuzz(*numbers)
        result_str = ' '.join(result) + '\n'
        outfile.write(result_str)
