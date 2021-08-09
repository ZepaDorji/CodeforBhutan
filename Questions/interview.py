# if x is even used  x/2 
# if x is odd then 3x + 1

def GetSteps(num):
    stoping_time = 0
    new_num = 0

    while new_num != 1:
        if num % 2 == 0:
            new_num = num / 2
            stoping_time = stoping_time + 1
            num = new_num

        else:
            new_num = 3 * num + 1
            stoping_time = stoping_time + 1
            num = new_num 
    return stoping_time
total_step = GetSteps(10)
print(total_step)