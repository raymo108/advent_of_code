with open('input.txt', 'r') as elf_list:
    # call readlines() to return a list containing each line in the file as a list of strings
    lines = elf_list.readlines()

    # removes the given characters from the beginning and the end of the original string. Removes the \n character in string
    calories = [entry.strip() for entry in lines]


elf_sums = []
current_sum = 0
for entry in calories:
    if entry != '':
        current_sum += int(entry)
    elif entry == '':
        elf_sums.append(current_sum)
        current_sum = 0
elf_sums.append(current_sum)

print(max(elf_sums))
#sort the list in reverse order (Descending)
elf_sums.sort(reverse=True)
# add the 3 top total calories in the list
three_sums = elf_sums[0] + elf_sums[1] + elf_sums[2]
print(three_sums)
