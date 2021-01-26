a = 200
b = 33

if (b > a): 
  print("b is greater than a")
else:
  print("b is not greater than a")

#Write a conditiona statement that evaluates if the user input is positive or negative

num = int(input("Give me a number: "))
if (num > 0):
 print("Your number is positive")
elif(num == 0):
  print("You entered 0, a neutral number. Please ask again")
else:
  print("Your number is negative")                 

#Ask the user for their age
#If they are younger than 13, tell them they can only watch PG/G movies
#If they are 13 and older but younger than 17, the can only watch PG-13/PG/G movies
#If they are 17 and older, they can watch all movies

age = int(input("How old are you? "))
if (age < 13):
  print("You can only watch PG/G movies")
elif (age == 13, 14, 15, 16, 17):
  print("You may watch PG-13 and PG/G movies")
else:
  print("You can watch any movie you would like. Congrats!")

#hungry?

isHungry = False
isSleepy = False
if(isHungry == True):
  print("You should go eat")
elif(isSleepy == True):
  print("GOOD NIGHT!!")
elif(isSleepy == False):
  print("Wow,great sleep schedule")
else:
  print("I ADMIRE YOUR STRESS EATING")