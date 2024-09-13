# Excercise Soluions 

# 1.  Store a message in a variable, then print that message. 

x = "aarti"
y = 7
print(x)
print(y)

# 2. Store a message in a variable, and print that message. 
#    Then change the value of your variable to a new message, 
#    and print the new message.

x ="my_variable"
print(x)
x = "changed my variable"
print(x)


# 3. Store a person’s name in a variable, and print a message to that person. 

name = "bob"
print(f"hello {name}" )

# 4. Store a person’s name in a variable, and then print that 
# person’s name in lowercase, uppercase, and titlecase.

variable_name = "Charlie is his name" 
p = variable_name.upper()
print(p) 


variable_name = "Charlie is his name" 
k = variable_name.lower()
print(k) 

variable_name = "Charlie is his name" 
s = variable_name.title()
print(s) 

#5. Write addition, subtraction, multiplication, and division operations 
# that each result in the number 8. Be sure to enclose your operations in 
# print statements to see the results.

x =5
y= 3
print (x+y)

x = 10
y= 2
print (x-y)

x = 2
y = 4
print(x*y)

x= 16
y = 2
print(x/y) 

# 6. Store your favorite number in a variable. Then, using that variable, 
# create a message that reveals your favorite number. Print that message.

favnumber = 19 
print("Guess my fav number?")
print(f"my fav number is {favnumber}")


## Stretch and Challenge 

# 1. Use an f-string to print out a message with a variable. 
x = "this is my f-string statement"
print(f"Please see my fine line. {x}" )

# 2. Use multiple variables in one string to print a message.
x = "my first line" 
y ="my second line"
z= "my third line" 

print("x" + "y" + "z")

# 3. Set three variables, one that says, “Good”, another that 
# says, “Day”, and another that says your name. “Add” them together, 
# with a space between each word, and store it into another variable. 
# Then, print out that variable.

first_v = "good "
second_v = "day "
third_v = "charlie "

fourth_v = first_v + second_v + third_v 

print(fourth_v)