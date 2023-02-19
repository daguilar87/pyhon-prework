# Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(username):
    """Greet user"""
    print("hello_"+username.upper()+"!")

hello_name('username')

#Question 2 
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    """printing odd numbers 1-100"""
    first_odds=list(range(1,100,2))
    print(first_odds)



#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """highest number in list"""
    print("Can you guess my highest number?")
    if a_list>7:
        print("Too High! My number is")
    elif a_list<6:
        print("Too low! My number is")
        
    max_num_in_list=[1,2,3,4,5,6,7]
    
    print(max_num_in_list[-1])
max_num_in_list(1)

#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    leap=False 
    if a_year%400==0:
         leap=True
    elif a_year%4==0 and a_year%100 !=0:
        leap=True
    return leap
a_year=int(input())
print(is_leap_year(a_year))

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    counter=a_list[0]
    for value in a_list:
        if value==counter:
            counter += 1
        elif value != counter:
            print(False)
    print(True)


is_consecutive([1,2,3,4,5,6])

