import fileinput

input_lines = []
# Get lines from stdin
# for line in fileinput.input():
#     input_lines.append(line)
# Or get lines from string for the initial test.
input_lines_str = """
3
0 1
1 0
1 1
"""
input_lines = [line.strip() for line in input_lines_str.split('\n') if line.strip()]
num_input = int(input_lines[0].split()[0])
for line in input_lines[1:num_input+1]:
  print(line.strip())