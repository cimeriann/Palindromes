# Palindromic numbers
# A palindrome is a word that reads the same way forwards and backwards.(E.g Tenet, 101101)
# Write a function that prints out all Palindromic numbers less than a given input,
# and returns the total number —of palindromes— found!
# E.G: f(500) would print all Palindromic numbers less than 500,
# as well as the total number of palindromes less than 500.
# int objects are not iterable

def myfunc(x):
    # mylist = []
    num = 0
    for i in range(x):
        # for num in str(i):
        string = str(i)
        if string[::-1] == string[0:]:
            if len(string)>1:
                num+=1
                print(string)
                # mylist.append(string)
    # print(mylist)
    print('there are ',str(num),' numbers less than ', str(x))
    # print('There are ', str(len(mylist)), ' palindromes less than ',str(x))

myfunc(50000000)