
file_path=  "file_name"

with open(file_path, "r") as f:
    first_line= f.readline().strip()
    second_line=f.readline().strip()
    #save line one in variable in 1 and 2

print(first_line)
print(second_line)

mutations= 0

for i in range(len(first_line)):
    if first_line[i] != second_line[i]:
        mutations+=1


print(mutations)

