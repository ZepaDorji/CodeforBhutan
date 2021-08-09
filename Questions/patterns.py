# x pattern

def xpattern(row):
    for i in range(row):
        for j in range(row):
            if i == j or i + j == row-1:
                print("*",end = " ")
            else:
                print(" ", end= " ")
        print()
xpattern(5)