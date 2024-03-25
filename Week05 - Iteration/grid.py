# A program that inputs the number of rows and columns then outputs a grid of asterisks in the correct arrangement

rows = int(input("Input number of rows: "))
columns = int(input("Input number of columns: "))

columns = (f"* " * columns)

print ((f"{columns}\n") * rows)