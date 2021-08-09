# To check two string are anagrams of eachother

# anagram of string is another string that contains the same character,
# only the order of character is different.
# lenght should be same:


# taking string from user
str1 = input("Enter first string")
str2 = input("Enter second string")

def anagram(str1,str2):
    if len(str1) != len(str2):
        return 0

    else:
        for i in range(0,len(str1)):
            if str1[i] not in str2:
                return 0
        return 1

if anagram(str1, str2):
    print("They are anagrams to each other")
else:
    print("They are not anagrams to each other")
