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


# quiz question
b = 1
for a in range(1,10,3):
    b+= a + 1
print(b)

x = 50 
y = 10 
z = y if y > x else x 
print(z)