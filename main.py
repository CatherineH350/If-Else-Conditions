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
elif (18 > age > 13):
  print("You may watch PG-13 and PG/G movies")
else:
  print("You can watch any movie you would like. Congrats!")

#hungry?

isHungry = True
isSleepy = False
isBored = True
if(isHungry == True):
  print("You should go eat")
elif(isSleepy == True):
  print("GOOD NIGHT!!")
elif(isSleepy == False):
  print("Wow, great sleep schedule")
else:
  print("I ADMIRE YOUR STRESS EATING :D")


if(isHungry == isBored or isSleepy == isHungry):
  print("You should do your homework")
else: 
  print("You can play outside")

if(isSleepy == isHungry and isHungry == isBored):
  print("It's nap time")
else: 
  print("It's time for bed!")

#Ask the user for a number
#Tell the user if their number is even or odd.

userNum = int(input("Give me another number: "))
if (userNum % 2 != 0): 
  print("You have given an odd number")
else:
  print("You have given an even number")

# Math Quadrants
# Ask the user for an x and y value
# Using a nested conditional, output which quadrant they are in. 


quad = int(input("Enter a number for x: "))
quadY = int(input("Enter a number for y: "))
if(quad > 0):
  if(quadY > 0):
    print("Your coordinates would be in Quad 1")
  else:
    print("Your coordinates would be in Quad 4")
elif(quadY > 0):
  print("Your coordinates are in Quad 2")
elif(quadY == 0):
  if(quad == 0):
    print("Your coodinates are on the origin")
else:
  print("Your coordinates are in Quad 3")

if(quad < 0 and quadY > 0):
 print("Your coordinates are in Quad 2")
elif(quad < 0 and quadY < 0):
  print("Your coordinates are in Quad 3")

# let the user know when they are on the x-axis or the y-axis
#if we have +y or -y but x == 0 
#"You are on the "y-axis"
#if we have -x and +x but y == 0 
#You are on the x-axis

if(quad == 0):
   if(quadY > 0):
     print("Your coordinates are on the y axis, above the origin.")
   elif(quad == 0 and quadY < 0):
     print("Your coordinates are on the y axis, below the origin")
   else: 
     print("Your coordinates are on the origin")
elif(quadY == 0):
  if(quad > 0):
    print("Your coordinates are on the x axis, to the right of the origin")
  elif(quad < 0):
    print("Your coordinates are on the x axis, to the left of the origin")
  else:
    print("Your coordinates are on the origin")


#create ab if statement using "and" or "or" for the third and second qudrant. 

#If x and y are 0, output the origin 
#and, or
#and takes precendence over or
#"and" both conditions have to be true 
#"or" only one has to be correct 

x = 5
y = 6
z = 7
if(x == 5 and y == 5 or z == 5):
  print("Yay")
else:
  print("Nay ")

if(x == 5 or y ==5 and z == 5):
  print("IM DA BEST")
else:
  print("IM STILL DA BEST")