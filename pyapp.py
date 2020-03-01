
from pprint import pprint

with open("input_Q1a.txt") as f, open("output_Q1a.txt", "w") as w:
    for i, line in enumerate(f):
        print(i, line)
        for j in line:
            print(j)
        w.write("{:04d} {}".format(i + 1, line.upper()))