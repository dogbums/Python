# A program that inputs the number of rows and columns then outputs a grid of asterisks in the correct arrangement

# rows = int(input("Input number of rows: "))
# columns = int(input("Input number of columns: "))

# columns = (f"* " * columns)

# print ((f"{columns}\n") * rows)

rows = int(input("Input number of rows: "))
columns = int(input("Input number of columns: "))

for x in range(0, rows):
    for y in range(0, columns):
        print("*")





