# multiplication tables up to 10 x 10

for table in range(1, 11):
    print(table, "times table", end='')
    for multiplier in range(1, 11):
        print(" {:>3} ".format(table * multiplier), end='')
    else:
        print()
