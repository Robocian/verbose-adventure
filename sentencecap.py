sequence = input("Type a few sentences: ")

for i in range(len(sequence)):
    sequence[0].title()
    if sequence[i] == ".":
        next_letter = i + 2
        sequence[next_letter].title()

print(sequence)
