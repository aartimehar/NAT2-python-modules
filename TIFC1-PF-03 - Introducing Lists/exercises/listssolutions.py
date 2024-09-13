##Solutions 

# 1. Store the names of a few of your favorite music artists in a list called names.
# Print each name by accessing each element in the list, one at a time. 

names = ["Adele" , "Bob Marley" , "Avicii" , "Taylor Swift" , "Artic Monkeys"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 2. Start with the “names” list you used in the first exercise, but instead of 
# just printing each name, print a message to them. The text of each message should 
# be the same, but each message should be personalized with the music artist’s name. 

if "Adele" in names: 
    print(names[0] + "is my favorite Artist")

if "Bob Marley" in names: 
    print(names[1] + " is my favorite Artist")

if "Avicii" in names: 
      print(names[2] + " is my favorite Artist")

if "Taylor Swift" in names: 
    print(names[3] + " is my favorite Artist")

if "Artic Monkeys" in names: 
    print(names[4] + " is my favorite Artist")

# 3. Think of your favorite book or movie. Then:- Make a list that stores several examples. 
# Use your list to print a statement about your favorite book or movie. 
# For example, “My favorite book is Pride and Prejudice”.
# - Add an author or director name! Try printing a message to the author or director 
# on what you liked about their book or movie!

Authors = ["David Deutsch","Ann Druyan","George Gilder"]
print(Authors[0] + "is a British physicist at the University of Oxford. He is a visiting professor in the Department of Atomic and Laser Physics at the Centre for Quantum Computation (CQC) in the Clarendon Laboratory of the University of Oxford.")
print(Authors[1] + "is an American writer and producer specializing in the communication of science. She co-wrote the 1980 PBS documentary series Cosmos, hosted by Carl Sagan, whom she married in 1981.")
print(Authors[2] + "is an American investor, writer, economist, techno-utopian advocate, and co-founder of the Discovery Institute.")


# The Dinner Problem

# 4.If you could invite anyone, living or deceased, to dinner, who would you invite? Follow each bullet point to build your program:
   
# - Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

invitepeople = ["Illona", "Ian" ,"Romano"]

for guest in invitepeople: 
   print("Dear " + guest + "Please come along to my place with your family to dinner")

# - You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
print(f"Unfortunately{invitepeople[2]} can't make it to dinner")

#Replace the guest who cant make it 
cancelled_guests = invitepeople.pop(2)
print(cancelled_guests)

# Sending new set of invitations

for guest in invitepeople:
    print(f"Dear {guest} , Please come along with your family to have dinner at my place.")

# - Add a print statement at the end of your program stating the name of the guest who can’t make it.

print(f"Unfortunately, {cancelled_guests} cannot make it to dinner party")

# - Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. 
invitepeople.append("Alex")

# - Print a second set of invitation messages, one for each person who is still in your list.
for guest in invitepeople:
    print(f"Dear {guest} , You are invited to my dinner party ")

# - You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.  
# Start with your program from question 4 or question 5. Add a print statement to the end of your program informing people that you found a bigger dinner table.
for guest in invitepeople:
 print(f"Dear {guest} , We now have additional 3 spaces available for additional guests")

# - Use insert() to add one new guest to the beginning of your list. 

invitepeople.insert(0, "Amma")
print(invitepeople)

# - Use insert() to add one new guest to the middle of your list.

invitepeople.insert(3,"Sylar")
print(invitepeople)
# - Use append() to add one new guest to the end of your list. 

invitepeople.append("Hitu")
print(invitepeople)

# - Print a new set of invitation messages, one for each person in your list.

for guest in invitepeople: 
    print(f" Dear {guest} , you are welcome to my dinner party ")

# - You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests. 
#  Add a new line that prints a message saying that you can invite only two people for dinner.

for guest in invitepeople: 
    print(f"Dear {guest} , Unfortunately, our table has not arrived so we can only invite two guests at the moment")

# - Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner. 

guest_six = invitepeople.pop()
print(f"Unfortunately {guest_six} , we have to terminate your request for dinner party becuase we don't have the dinner table")

guest_five = invitepeople.pop()
print(f"Unfortunately {guest_five} , we have to terminate your request for dinner party becuase we don't have the dinner table")

guest_four = invitepeople.pop()
print(f"Unfortunately {guest_four} , we have to terminate your request for dinner party becuase we don't have the dinner table")

guest_three = invitepeople.pop()
print(f"Unfortunately {guest_three} , we have to terminate your request for dinner party becuase we don't have the dinner table")


# - Print a message to each of the two people still on your list, letting them know they’re still invited. 
print(f"Dear {invitepeople[0]} You are invited ")
print(f"Dear {invitepeople[1]} You are invited ")

# - Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program. 
# - Use len() to print a message indicating the number of people you are inviting to dinner

practice_len = len(invitepeople)
print(practice_len)



