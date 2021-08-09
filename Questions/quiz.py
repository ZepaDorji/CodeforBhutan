# try to answers the following questions withous running the programm
# Q1
b = 1
for a in range(1,10,3):
    b+= a + 1
print(b)

#Q2
x = 50 
y = 10 
z = y if y > x else x 
print(z)

#Q3
x = y = z = 300
print(x,y,z)

#Q4
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break

#Q5
print("python" '3')

#Q6
x = "Python is Greate"
y = x.upper().lower().upper()
print(y)

#Q7
def length(a,b):
    return a(b)
print(length(len,"python"))


#Q8
x = ['1','2','3']
y = x[1] + x[2]
print(y)