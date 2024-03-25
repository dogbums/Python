# A program that inputs the number of rows and columns then outputs a grid of asterisks in the correct arrangement

# rows = int(input("Input number of rows: "))
# columns = int(input("Input number of columns: "))

# columns = (f"* " * columns)

# print ((f"{columns}\n") * rows)

rows = int(input("Input number of rows: "))
columns = int(input("Input number of columns: "))

for x in range(rows):
    for y in range(columns):
        print("*", end="")  # Print stars on the same line.
    print()  # Move to the next line after each row is printed.





