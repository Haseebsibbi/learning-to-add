
'''def subtract(a,b):
    print(a-b)
    return a-b # if ther is no return keyword in a function then in out put none is retured
result = subtract(5,3)
print(result)'''

''' def multiplexer(word: str, time: int) ->str : # here ->str represents the return type like it is going to return an string 
    return word * time
result = multiplexer("Cat\n",10)
print(result)
print(multiplexer("Dog\t", 5))
print(type("cat")) '''


'''def length(sentence:str ):
    if len(sentence) > 7:
        print("Length of string is more", True)
    else :
        print("opps! Sorry ", False)
    return str
print(length("Hee"))'''

'''length_string = "python"
print(length_string[2*2])
print(len(length_string))
print(length_string[5])
print(length_string)'''


'''def same_first_and_last_letter(t_string):
    if len(t_string) >=1:
        if t_string[0] == t_string[-1]:
            print("Congrats ", True)
        else:
            print(False)
    else:
        print("Length must be greator than one ")
print(same_first_and_last_letter("fdsf")) '''



'''def first_three_characters(t_string:str):
    alphabet = "abcdefghij"
    print(alphabet[-6:])
    return t_string
first_three_characters("Here is the string variable")'''

# print("hello \t \"this is double slash test\"")   # how to print string in double quations
#print("here \'is the single \'")

'''a = 34
b = 333
c = 90
sum = (a \
       + b\
       +c)
print(a,
      b,
      c)
drive_adress = r"c:\G\mn"
print(drive_adress)'''

'''t_string = " this is a book"
print("is" in t_string)
print("is" not in t_string)'''

#index of method

'''google = "google chrome"
print(google.find("e"))
print(google.find("l"))
print(google.find("o", 5))
print("Index of r is ", google.index("r"))'''


'''str1 = "this is really a string example....wow!!!"
str2 = "a"

print (str1.rfind(str2))

print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))

print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))'''


#startwith and endswith

'''t_string = "Good morning france"
print(t_string.startswith("G"))
print(t_string.endswith("france"))'''

# count method
'''t_string = "world is more beautiful than it self"
print(t_string.count("world"))
print()
print(t_string.count("l"))
print(t_string.count("z"))
print(t_string.count("i") + t_string.count("f"))'''

#couting vowels

'''t_string = "hello i am from pakistan and you "
a = str(t_string.count("a"))
print(a," occurs a")
e = str(t_string.count("e"))
print(e," occurs e")
i = str(t_string.count("i"))
print(i," occurs i")
o = str(t_string.count("o"))
print(o," occurs o")
u = str(t_string.count("u"))
print(u," occurs u")
sum = int(a) + int(e) + int(i) + int(o) + int(u)
print("Sum of vowels ", sum)'''

'''stroy = "once upon a time. i lived "
print(stroy.capitalize())
print(stroy.title())
print(stroy.upper())
print("THIS IS A TEST STRING".lower())
print("AbCDeFgH".swapcase())
print("THIS IS A TEST STRING".lower().title())
print("hello".isupper())
print("HELLO ".isupper())
print("hello!@#$".islower())
print("this is alphabets".isalpha())
print("All Is Well".istitle())
print("23423".isnumeric())
print("is all num")
print("sdfsda2324".isalnum())
print("if there is space bw num and sen")
print("sdfsd 234".isalnum())
print("is there space or not ")
print(" ".isspace())'''

#remove space

'''remove_space = "        this is space string    "
print(remove_space.rstrip())
print()
t_string = "this is spave string            "
print(t_string.lstrip())
google =  "www.google.com"
print(google.lstrip("www")) #removing the characters from left side of the string

print(google.rstrip("com"))

kill_space = "      this kill the spave             "
print(kill_space.strip())
name = "my name is rehman and first name is muhammad"
print(name.strip(""))'''

#replace method

'''replace_space = "92 303 972 771"
print(replace_space.replace(" ","-"))


fancy_cleanup = "       this is a space string      "
print(fancy_cleanup.strip().replace("g", "z").replace(" ", "!"))'''

#format method

'''call_names = ("{} wants to go {} {}" )
print(call_names.format("Haseeb","Canada","USA"))

call_names = ("{2} wants to go {0} {1}" )
print(call_names.format("Haseeb","Canada","USA"))

call_names = ("{Name:} wants to go {North_USA} {South_USA}" )
print(call_names.format(Name="Haseeb",North_USA= "Canada",South_USA="USA"))'''


'''friends = ("{first} and {second} or {third}")
first = input("Entrer first name :")
second = input("Enter second name :")
third = input("enter third name :")
print(friends.format(first= first, second= second, third= third))'''

'''name = "bushra "
adjective = "Saif"
noun = "Love"
p_string = (f"{name} is my {noun} and her father name is {adjective}")  #this is the same code as i have done before
print(p_string)'''

#simple to use format method

#print(f"2 + 2 is {2+2}")

# equilty and non equality operator

'''admin = False
handsome = True
print(2 > 4)
print(4 > 3)
result = 45< 90
print(result)

print("this" == "this") #string comparision
print("not equal" == "equal")
print("haseeb " != "rehman")'''


# about 0 and 1
'''if 1:
     print("this is new test")
if 3:
    print("this also reuw ")
if 0:
    print("this is not going to print")
if "hello":
    print("this is also true")'''


'''def even_or_odd(number):
   #num = int(input("Enter a number :"))
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")
    return "End of program"
print(even_or_odd(24))'''


#and keyward
'''if 89 < 900 and "rain" == "rain":
    print("this is truw")
if "haseeb " =="haseeb " or 45 < 4:
    print("one of statement is true so ")'''

#nested if


'''food1 = input("Enter the food item 1:")
food2 = input("Enter 2nd food item 2:")

if food1 =="pizza":
    if food2 == "naan":

        print("pizza and shuwarma ")
    else:
        print("not a good choice")
else:
    print("i am vegetrain ")'''

#problem  of dividing by 3, 4

'''def divie_three_four(number):
    if (number % 3 ==0) and (number % 4 == 0):
        print("Congrats !")
        return True
    else:
        return False
print(divie_three_four(12))'''

#problem

'''def string_theory(t_string):
    if (len(t_string) > 4) and (t_string[0]=="H"):
        return True
    else:
        return False
print(string_theory("Hello"))'''

#
''''i = 0
while (i<10):
    print(i, end=' ')
    i += 1
print(" ")
word = "HELLO"
for character in word:
  print(character)

for i in range(1,11):
    print(i, end=" ")
    i +=1'''


'''print("Here's a simple multiplication table using loops:")
for i in range(1, 11):
    print(i, end = " ")
print()
for i in range(1,11):
    print(i*2, end = " ")
print()
for i in range(1, 11):
    print(i*3, end=" ")
print()
for i in range(1,11):
    print(i*4, end=" ")
print()
for i in range(1,11):
    print(i*5, end=" ")
print()'''

###### same problem in nested loop
'''print("Here's a simple multiplication table using nested loops:")
for i in range(1,11):
    for j in range(1,11):
        print(j*i, end=" ")
    print()'''

##########

'''print("Exponent calculator")
print("===================")
a = int(input("Enter the base: "))
n = int(input("Enter the exponent: "))
result = a
for i in range(n - 1):
    result = result * a

print("Result: %d" % (result))
print("Thank you for using our exponent calculator")'''


# while statement

'''count = 0
while count <= 5:
    print(count)
    count += 1
print(count)'''

#example
'''invalid_number = True
while invalid_number:
    user_input = int(input("Please enter a number greator than 10 :"))
    if user_input >= 10:
        print(f"You enter {user_input} :")
        invalid_number = False
    else:
        print("Try again")'''


'''If the number is divisible by 3, print "Fizz" instead of the number.

If the number is divisible by 5, print "Buzz" instead of the number.

If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

If the number is not divisible by either 3 or 5, just print the number.'''

'''def FizzBuzz():
    user = int(input("Please enter a number :"))
    if (user % 3 == 0) and (user % 5 == 0) :
        print(f"{user} FizzBuzz")
    elif user % 3 == 0 :
        print(f"{user} Fizz")
    elif user % 5 == 0:
        print(f"{user} Buzz")
    elif (user % 3 != 0) and (user % 5 != 0):
        print(f"{user} Not Valid ")
    else:
        print("Haseeb Rehman")
print(FizzBuzz())'''

#recurssion

'''def coun_down(number):
    user = number
    while user >= 0:
        print(user)
        user -= 1
print(coun_down(5))'''

'''def count_down(number):
    if number <=0:
        return 
    print(number)
    count_down(number-1)
print(count_down(5))'''

#reverse string
'''def reverse_string(t_string):
    start_index = 0
    last_index = len(t_string) -1
    alter_string = ""
    while last_index >= start_index:
        #alter_string = alter_string + str(last_index)
        alter_string += t_string[last_index]
        last_index -=1
    return alter_string
print(reverse_string("haseeb"))'''

'''def reverse(user_string):
    if len(user_string) <= 0:
        return user_string

    return user_string[-1] + reverse(user_string[0:-1])
print(reverse("Hello"))'''

# Define a factorial function that accepts a single number

# A factorial represents the product of all numbers up to, and including, that number. For example, 5 factorial is 5 * 4 * 3 * 2 * 1 = 120

# Return the factorial from your function. You should NOT use any kind of loops. Instead, utilize recursion. Your function MUST call itself.

# factorial(1) => 1
# factorial(2) => 2
# factorial(3) => 6
# factorial(4) => 24
# factorial(5) => 120
'''def factorial(number):
    if (number == 1) or (number==0):
        return 1
    else:
        return number *  factorial(number-1)
print(factorial(0))'''

# in and out in list
'''eating_time = ["breakfast", "lunch", "dinner"]
print("breakfast" in eating_time)
print("dinner" in eating_time)
print("snacks " not in eating_time )
print("breakfast" not in eating_time)'''

'''browsers = ["Chrome", "mozila", "opera "]
#print(browsers[2])
print(browsers[-1])
print(browsers[-2][2]) # show you the character
print(browsers[-2])'''


'''def first_and_last():
    abc = ["a", "b", "c"]
    return (abc[0]+abc[2])

print(first_and_last())'''

# Define a function product_of_even_indices that accepts a list of numbers.
# The list will always have 6 total elements.
# The function should return the product (multiplied total) of all numbers at at even index (0, 2, 4).
#
# product_of_even_indices([1, 2, 3, 4, 5, 6]) # 15
# product_of_even_indices([3, 4, 3, 5, 3, 6]) # 27
##################################################################################################################
# Declare a nested_extraction function that accepts a list of lists and an index position.

# The function should use the index as the basis of finding both the nested list
# and the element from that list with the given index position

# You can assume the number of lists will always be equal to
# the number of elements within each of them.

# nl = [[3, 4, 5], [7, 8, 9], [10, 11, 12]]
# nested_extraction(nl, 0) => # 3
# nested_extraction(nl, 1) => # 8
# nested_extraction(nl, 2) => # 12
#####################################################################################################################
'''dinner = " this time i am reading "

for read in dinner:
    print(read)'''
'''numbers = [1,2,3,4,5,6,7,8]
#for no in numbers:
    # print(no,"\t",no * no)
total = 0
for sum in numbers:
    total = total + sum
print(total)'''

'''movie = ["ajay","amir","govinda"]
for name in movie:
    print(len(name))
print(name)
print()'''

# Define a sum_of_lengths function that accepts a list of strings.

# The function should return the sum of the string lengths.

# sum_of_lengths(["Hello", "Bob"]) => 8
# sum_of_lengths(["Nonsense"])     => 8
# sum_of_lengths(["Nonsense", "or", "confidence"]) => 20

'''sum_of_lengths = ["Hello", "Baby"]
sum = 0
for length_sum in sum_of_lengths:
    sum = (len(length_sum))
    sum = str(sum) + length_sum
    print(sum)'''
############################################################################################################
# pig latin game
'''user_data = input("Pig Latin ! ")
print(user_data)
last_letter = user_data[0]
new_string = user_data[1:] + last_letter + "ay"
print(new_string)'''

'''user_input = input(" Enter a word ")
if len(user_input) > 0 and user_input.isalpha():
    print(user_input)
else:
    print("Empty ")'''

'''values = [2,3,4,5,6,78,9]
other_values = [23,343,6,7,90,88]
def odd_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 ==1 :
            total += number
    return total
print(odd_sum(values))
print(odd_sum(other_values))'''

'''def greatest_number(numbers):
       greatest = numbers[0]
       for number in numbers:
           if number > greatest:
              greatest = number
        return greatest
print(greatest_number([1,2,4]))
print(greatest_number([1,2,4,5,9,6]))
print(greatest_number([-90,-34,-33,-1]))'''

# reverse the list
'''magic_reverse = ["hockey","football","cricket","soces"]
print(magic_reverse[::-1])
#for character in magic_reverse[::-1]:
    #print(character ,"have the number of elements", len(character))
   # print(f"{character} have the number of {len(character)} elements ")
for character in reversed(magic_reverse):
    print(f"{character} have the number of {len(character)} elements ")'''
# enmurate function

'''errands = ["breakfast","lunch","college","dinner"]
print(enumerate(errands))
for index, errand in enumerate(errands):
    print(f"{errand} is priority of the day {index}")'''
'''friends = ["bushra","babar","hamza","sheraz"]
#for index, friend in enumerate(friends):
for index, friend in enumerate(friends ,100):
    #print(f"{index} {friend} is my friend :")
    print(f"{index +1} {friend} is my friend :")'''

#Define an in_list function that accepts a list of strings and a separate string.

# Return the index where the string exists in the list. If the string does not exist, return -1.

# Do NOT use the find or index methods.

# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1
##############################################################################################################
# Define a sum_of_values_and_indices function that accepts a list of numbers.
# It should return the sum of all of the elements along with their index values.
#
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 6

#####################################################################################################################

#for numbers in range(5):
    #print(numbers)

#for numbers in range(1, 11):
 #   print(numbers)
'''for numbers in range(5,100,10):
    print(numbers)
print(32 in [1,2,3,4,5,6,7])'''

# break keyward


'''def search(values, target):
    found = False
    for value in values:
        print(value)
        if target == value:
            found=True
            break
    return found
print(search([1,2,3,4,5,6,7],5))'''

'''def sum_of_values(values):
    sum = 0
    for addition in values:
        if addition>0:
            sum +=addition
    return sum
print(sum_of_values([-1,2,3]))'''

'''def sum_of_values(values):
    sum = 0
    for addition in values:
        if addition<0:
            continue
        sum +=addition
    return sum
print(sum_of_values([-1,2,3]))'''

########################################################################################
# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# length_match(["cat", "dog", "kangaroo", "mouse"], 3)) => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5)) => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4)) => 0
# length_match([], 5)) => 0
###############################################################################
# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# sum_from(1, 2)   # 1 + 2 => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5 => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8 => 35
# sum_from(9, 12)  # 9 + 10 + 11 + 12 => 42
#######################################################################################
# Declare a function same_index_values that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# same_values([1, 2, 3], [3, 2, 1]) => [1]
# same_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]) => [1, 3]
###################################################################################################



import math
#print(math.sqrt(25))
#from math import *

#def maximum(first, second):

 #   return max(first,second)
#print(maximum(34,44))

'''def plane_ride_cost(city):
    if city =="paris":
        return 899
    elif city =="Dijon":
        return 33
    elif city =="london":
        return 33333
    else:
        return 0

def rental_car_cost (days):
    day_cost = 40
    total_cost = day_cost * days
    if days >=7:
        total_cost -=50
    elif days>=3:
        total_cost -=20
    return total_cost


def trip_cost (city, days , spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + spending_money
print(trip_cost("paris", 7,900))'''

###########################################################################################################
# Declare a length_match function that accepts a list of strings and an integer.
# It should return a count of the number of strings whose length is equal to the number.
#
# length_match(["cat", "dog", "kangaroo", "mouse"], 3)) => 2
# length_match(["cat", "dog", "kangaroo", "mouse"], 5)) => 1
# length_match(["cat", "dog", "kangaroo", "mouse"], 4)) => 0
# length_match([], 5)) => 0


###########################################################################################################
# Declare a sum_from function that accepts two numbers as arguments.
# The second number will always be greater than the first number.
# The function should return the sum of all numbers from the first number to the second number (inclusive).
#
# sum_from(1, 2)   # 1 + 2 => 3
# sum_from(1, 5)   # 1 + 2 + 3 + 4 + 5 => 15
# sum_from(3, 8)   # 3 + 4 + 5 + 6 + 7 + 8 => 35
# sum_from(9, 12)  # 9 + 10 + 11 + 12 => 42

###########################################################################################################
# Declare a function same_index_values that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# same_values([1, 2, 3], [3, 2, 1]) => [1]
# same_values(["a", "b", "c", "d"], ["c", "b", "a", "d"]) => [1, 3]

###########################################################################################################
'''import sys
#print(sys.argv)
#print(type(sys.argv))
arg = "hello this is"
total_length = 0
for arg in sys.argv[1:]:
    total_length + = len(arg)'''

'''colors = ["red ","green ","blue ","white "]
print(colors)
colors[1] = "yellow "
print(colors)
print()
colors[2:3] = ["Gold","silver"]
print(colors)
colors[-1] = "orange"
print(colors)'''
#####################################################################################################333333
# Given the great_directors list below, overwrite the “Steven Spielberg” string with a string of “Michael Bay”.
'''great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]


# Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]


# Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]


# Given the tech_companies list below, overwrite the Microsoft, Blueberry, and IBM strings
# with the strings “Facebook” and “Apple”. Use list slicing syntax.
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]
great_directors [1] = "Michael Bay"
print(great_directors)'''


#append method
'''countries = ["pak", " aus", "new", " canada "]
print(countries)
print(len(countries))

countries.append("India")
print(countries)
print(len(countries))

countries.append("ban")
print(countries)
print(len(countries))

countries.append("china")
print(countries)
print(len(countries))'''


'''powerball_number = [2,4,6,8,10,12]
def squares(numbers):
    sqr = []
    for number in numbers:
        sqr.append(number**2)
    return sqr
print(squares(powerball_number))'''


'''powerball_number = [2,4,6,8,10,12]
def convert_float(powerball_list):
    floating = []
    for  num in powerball_list:

        floating.append(float(num))
    return floating
print(convert_float(powerball_number))'''

'''powerball_number = [2,4,6,8,13,12]

def even_odd(numbers):
    even = []
    for num in numbers:
        if num%2==0:
            even.append(True)
        else:
            even.append(False)
    return even
print(even_odd(powerball_number))'''

# Define an only_evens function that accepts a list of numbers.
#
# It should return a new list consisting of only the even numbers from the original list.
#
# only_evens([4, 8, 15, 16, 23, 42]) => [4, 8, 16, 42]
# only_evens([1, 3, 5]) => []
# only_evens([])        => []

'''even_list = [3,5,34,55,66,77,88]
def only_evens(numbers):
    even = []
    for num in numbers:
        if num%2 == 0:
            even.append(num)
    return even
print(only_evens(even_list))'''

# Define a long_strings function that accepts a list of strings.
#
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# long_strings(["Hello", "Goodbye", "Sam"] => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"] => []
# long_strings([] => []

'''t_string = ["amber","bushra","nimra","rafia","maham"]
def long_strings(girls):
    five_length_string = []
    for new_list in girls:
        if len(new_list)> 5:
            five_length_string.append(new_list)
    return five_length_string
print(long_strings(t_string))'''

'''old_string = ["amber","bushra","nimra","rafia","maham"]
old_string.extend(["ali","rehmna"])
print(old_string)
new_string = ["time pass","sincere","true love",]
old_string.extend(new_string)
print(old_string)'''

#insert

'''new_year = ["paris","london","japan"]
print(new_year)
new_year.insert(0,"pakistan")
new_year.insert(3,"china")
new_year.insert(4,"USA")
print(new_year)'''
# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]
#########################################################################################################


'''new_year = ["paris","london","japan"]
last_action = new_year.pop(2)
print(last_action)
print(new_year)
negative_test = new_year.pop(-1)
print(new_year)
print(negative_test)'''

'''new_year = ["paris","london","japan","china","pakistan","india"]
#del new_year[-1] #can delete more than values as pop deletes only one value
print(new_year)
print()
del new_year[1::2]
print(new_year)'''

'''new_year = ["paris","london","japan","china","pakistan","india"]
new_year.remove("india")
print(new_year)
print()
new_year.clear()'''

################################################################################################################3
# Declare a push_or_pop function that accepts a list of numbers
# Build up and return a new list by iterating over the list of numbers
# If a number is greater than 5, add it to the end of the new list
# If a number is less than or equal to 5, remove the last element added to the new list
# Assume the order of numbers in the argument will never require removing from an empty list
#
# push_or_pop([10]) => [10]
# push_or_pop([10, 4]) => []
# push_or_pop([10, 20, 30]) => [10, 20, 30]
# push_or_pop([10, 20, 2, 30]) => [10, 30]


'''push_or_pop_items = [12,33,44,55,66,3,44,777,8,887]
#old_push_or_pop = [10, 20, 2, 30]
def push_or_pop(numbers):
    empty_push_or_pop = []
    for num in numbers:
        if num>5:
            empty_push_or_pop.append(num)
        else:
            empty_push_or_pop.pop(num)
    return empty_push_or_pop
print(push_or_pop(push_or_pop_items))'''

'''old_push_or_pop = [10, 20, 2, 30]
def push_or_pop(numbers):
    empty_push_or_pop = []
    for num in numbers:
        if num>5:
            empty_push_or_pop.append(num)
        #else:

            #empty_push_or_pop.pop(num)
    return empty_push_or_pop
print(push_or_pop(old_push_or_pop))'''

#reverse method
'''players = ["a","b","c","d","e"]
players.reverse()
print(f"{players}".upper())'''

'''counting = [34,55,44,33,22,11,278,999,435]
counting.sort()
print("Here is the assending list of items \n",counting)
counting.reverse()
print("This is decenfing list of items \n",counting)'''

''''string_list = ["ali","rehman","haseeb","babar","jahanzaib"]
capitale_mixed_string = ["Haseeb","rehman","Ali","murtaza","baby"]
string_list.reverse()
print(string_list)
print()
string_list.sort()
print(string_list)
print()
print(sorted(string_list))


capitale_mixed_string.reverse()
print(capitale_mixed_string)
print()
capitale_mixed_string.sort()
print(capitale_mixed_string)
print()
print(sorted(capitale_mixed_string))'''


#count method
'''count_number = [1,2,3,3,44,54,3,2]
print(count_number.count(2))

count_string = ["haseeb","haseeb","rehman"]
print(count_string.count("haseeb"))
print(count_string.index("haseeb",1))
print(count_number.index(2,3))'''

#Copy method
'''orginal_list = ["haseeb","rehman","haider","murtaza"]
#print(orginal_list)
copy_list = orginal_list.copy()
print()
print(copy_list)
orginal_list.remove("haseeb")
print("this is after removing first ",orginal_list)
copy_list = orginal_list[:]
print(copy_list)
orginal_list.append("ali")
print(orginal_list)'''

#split method

'''o_string = "haseeb, rehman, ali, awais, hamza"
print(o_string)
print(o_string.split(", "))
print(o_string.split(", ", 2))
s_test = "i am learnig french"
words = s_test.split(" ")
print(words)'''

#join method

'''address = ["Street and home", "city", "21000", "country"]
print(", ".join(address))
subject_marks = ["23","122","908","444","873"]
print("-".join(subject_marks))
print("-".join(["92","303","9729771"]))'''

# Define a word_lengths function that accepts a string.
# It should return a list with the lengths of each word.
#
# word_lengths("Mary Poppins was a nanny") => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut") => [8, 5, 2, 5]
########################################################################################################
# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"]) => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"]) => "cat er pillar"
# cleanup(["", "", " "]) => ""
'''breakfasts = ["egg", "choclate"]
lunchs = ["rice", "biryani"]
dinners = ["daal", "channy"]
print(zip(breakfasts,lunchs,dinners))
print(zip(breakfasts,lunchs,dinners))

for breakfast,lunch,dinner in zip(breakfasts,lunchs,dinners):
    print(f"my meal today {breakfast} and {lunch} and lastly in dinner {dinner}")'''

'''breakfasts = ["egg", "choclate"]
lunchs = ["rice", "biryani"]
dinners = ["daal", "channy"]
print(zip(breakfasts,lunchs,dinners))
print(type(zip(breakfasts,lunchs,dinners)))
print(list(zip(breakfasts,lunchs,dinners)))'''

#nested list
'''multi_list = [
    ["fsd","lhr","isb","okr"],
    ["ali","haseeb","rehman","azhar"],
    ["paris","dijon","lyon","besoncon"]
    ]
#print(multi_list)
#print()
#print(multi_list[0],len(multi_list[0]))
#print()
#print(multi_list[1][2])
#print()
empty_list = []
for cities in multi_list:
    for city in cities:
        empty_list.append(city)
print(empty_list)'''


# nested_sum([[1, 2, 3], [4, 5]]) => # 15

##############################################################33
#PRINT THE SQUARE FOR A LIST
'''square_list = [4,5,6,7]
empty_list = []
#for numbers in square_list:
 #   empty_list.append(numbers**2)
#print(empty_list, end=" ")
empty_list = [numbers**2 for numbers in square_list] # same thing in one line 
print(empty_list)'''

#find length of string

'''cities = ["faisalabad", "lahore", "multan", "isb"]

empty_list = []
for words in cities:
    words_length = len(words)
    empty_list.append(words_length)
print("THIS IS THE LENGTH OF EACH WORD \n", cities,"\n", empty_list, end=" ")
print([uppercase_city.upper() for uppercase_city in cities ])'''

'''decimals = [23.3, 55.7, 65.1, 98.8]
for deci in decimals:
    print(int(deci), end=" ") '''

#filtering the result

'''for number in range(20):
    print(number/2, end=" ")'''

#counting the index number of word in string

#print(["aquicklittlebrownfoxjumpsoverthelazydog".index(char) for char in "abc"])

#finding string
'''find_string = ["haseeb rehman", "ali rehman", "hamza", "huzaifa", "azhar", "ashraf"]
empty = []
for name in find_string:
if "rehman" in name:
        empty.append(name)
        print(len(name))
print(empty)
for name in find_string:
if "rehman" in name:
        print(name.split(" ")[0], ",", end=" ")'''
###########################################################################################
# Uncomment the commented lines of code bellow and complete the list comprehension logic

# The floats variable should store the floating point values for each string in the values list.
#values = ["3.14", "9.99", "567.324", "5.678"]
# floats = []

# The letters variable should store a list of 5 strings.
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
#name = "Boris"
# letters = []

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
#elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
# lengths = []
#######################################################################
# Declare a function destroy_elements that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# destroy_elements([1, 2, 3], [1, 2]) => [3]
# destroy_elements([1, 2, 3], [1, 2, 3]) => []
# destroy_elements([1, 2, 3], [4, 5]) => [1, 2, 3]


############################## build in functions

#help(print)
#help(list)
#help("hejj".replace)
#help("lkj".swapcase)
#help([1].extend)
#help(map)

'''numbers = [2, 4, 5, 1, 7, 3, 6]
animals = ["cat", "dog", "bufflow", "cow"]
def cubes(number):
    return number**3
print(list(map(cubes, numbers)))
print(list(map(len, animals)))'''

#filter function
'''animals = ["cat", "dog", "bufflow", "cow"]
def filter_animal(animal):
    return len(animal) > 3
print(list(filter(filter_animal, animals)))
help(filter)'''

'''animals = ["cat", "dog", "bufflow", "cow"]
print(list(filter(lambda animal: len(animal) > 3 , animals)))
print(list(map(lambda animal: len(animal) > 3 , animals)))'''

# ALL AND ANY FUNCTION

'''print(all([True]))
print(all([True, False]))
print(all([""]))
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all(["haseeb", "rehman", "asd"]))
print()

print(any([True, False]))
print(any([0, 1]))
print(any([]))
print(any(["", " "]))'''

#  MAX AND MIN FUNCTION
'''print(max([3,4,5,6,7]))
print(min([1,2,3,4,5]))

print(max(122,33,443,2243,444))
print(min(11,22,33,44,0))'''

# SUM FUNCTION
# dunder methods # dir
'''print(dir([]))
print("haseeb rehman ".__len__())
print(len("haseeb rehman"))
print("sts" in "pastsa")
print("pasta".__contains__("stww"))'''

#FORMAT METHOD
'''number = .123456789
print(format(number, "f"))
print(format(number, ".2f"))
print(format(.3, "%"))
print(format(.5, ".2%"))
print(format(1234567, ","))'''

#TUPLE

'''names = "ahseeb", "rehmna", "ali"
print(type(names))
name = ("hamza", "huzaif", "asghar")
print(type(name))

print(tuple(["france", "germany", "italy"]))
print(tuple("haseeb"))
birthday = (2, 4, 1996)
print(type(birthday))
print(birthday[0])
print(birthday[1])
print(birthday[2])'''

#unpacking the TUPLE
'''details = ("Haseeb", "Rehman", "Sadiq", 24)
f_name, l_name, Father_name, age = details
print(f_name, l_name, Father_name, age)'''


#swapping values
'''a = 10
b = 40
a, b = b, a
print("Here is the new value of A", a)
print("Here is the new value of B", b)'''

'''employee = ("Haseeb", "Rehman", "Sadiq", 24)
f_name, l_name, *other = employee
print(f_name)
print(l_name)
print(other)
*name, age = employee
print(name)'''



