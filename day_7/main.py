from collections import defaultdict

filepath = []
sizes = defaultdict(int)
total = 0

file = open("input.txt")

# parse input commands
for line in file:

    # change directories
    if line.startswith('$ cd'):
        directory = line.split()[-1]

        # go to the previous directory
        if directory == '..':
            filepath.pop()

        # add directory to filepath
        else:
            filepath.append(directory)

    elif line.startswith('$ ls'):
        continue

    # parse ls output for sizes
    else:
        size, _ = line.split()

        if size.isdigit():
            size = int(size)
            for i in range(len(filepath)):
                sizes['/'.join(filepath[:i + 1])] += size

for key, value in sizes.items():
    if value <= 100_000:
        total += value

print(total)

#part 2

total_space = 70000000
update_size = 30000000
used_space = sizes['/']
free_space = total_space - used_space
space_needed = update_size - free_space

# find eligible directories to delete
options = []
for key, value in sizes.items():
    if value > space_needed:
        options.append(value)

# print answer
print(min(options))
