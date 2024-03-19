rows = int(input("Input number of rows: "))
columns = int(input("Input number of columns: "))

columns = int(f"* {columns * columns}")
rows = int(f"* {rows * rows}")

lines = rows


for (rows) in lines:
    print ((f"{columns} \n") * rows)