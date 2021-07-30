# You have three friends that you asked to go to a restaurant with you, 
# but the only table sits two. Write a python function that returns true 
# if only one of your friends wants to stay but false if more than one of your 
# friends wants to stay or if none of your friends want to stay.

# All three inputs are booleans
def canIStay(friend1, friend2, friend3):
    if (friend1 == True and friend2 == False and friend3 == False):
        return True
    elif (friend1 == False and friend2 == True and friend3 == False):
        return True
    elif (friend1 == False and friend2 == False and friend3 == True):
        return True
    else:
        return False
stay = canIStay(True,False,False)
if stay == True:
    print("You can take a sit")
else:
    print("Only one sit is available")



# You have three sizes of drinks at your store, small, medium and big. 
# But one of your employees likes to switch the prices around. 
# Write a function that returns true if the smallest price is with the smallest drink 
# and if the largest price is with the largest drink.

# Each of the variables is an integer for the price of the drink
def areDrinkPricesCorrect(small, medium, big):
    if (small < medium and small < big):
        if medium < big:
            return True
        else:
            return False
    else:
        return False

print(areDrinkPricesCorrect(1,2,5))


# Return an array containing the numbers from 1 to N, where N is the parametered value.

# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead
# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# N will never be less than 1.

# Method calling example:

# fizzbuzz(3) -->  [1, 2, "Fizz"]


def fizzbuzz(n):
    if n > 0:
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz",end = " ")
            elif i % 3 == 0:
                print("Fizz", end = " ")
            elif i % 5 == 0:
                print("Buzz", end = " ")
            else:
                print(i,end = " ")
fizzbuzz(20)