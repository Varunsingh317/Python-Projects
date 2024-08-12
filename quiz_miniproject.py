print("Welcome to Computer Quiz" )

player = input("What is your name? ")

print('Hello ' + player)

age = int(input('write your age: '))

if age >= 18:
   print("You are eligible for the quiz cmopetition ")

   print("Lets begin the quiz ")

   score = 0

# QUE 1

   print('Question 1')

   print('What is the full form of RAM?')

   answer1 = input('')

   if answer1.lower() == "random access memory":
      print('Correct')

      score += 1
      print('Your current score is : ', score)

   else: 
      print("Incorrect")
      print("Correct answer is random access memory ")


   #que 2

   print('Question 2')

   print('What is the full form of CPU?')

   answer2 = input('')

   if answer2.lower() == "central processing unit":
      print('Correct!')

      score += 1 
      print('Your current score is : ', score)

   else: 
      print("Incorrect!")
      print("Correct answer is central processing unit")


   # que 3


   print('Question 3')

   print('What is the full form of OS?')

   answer1 = input('')

   if answer1.lower() == "operating system":
      print('Correct')

      score += 1
      print('Your current score is : ', score)

   else: 
      print("Incorrect")
      print("Correct answer is operating system")


   #que 4

   print('Question 4')

   print('Who discovered python rogramming language? ')

   answer1 = input('')

   if answer1.lower() == "Guido van Rossum":
      print('Correct')

      score += 1 
      print('Your current score is : ', score)

   else: 
      print("Incorrect")
      print("Correct answer is guido van rossum ")


   #que 5


   print('Question 5')

   print('17*45-10 is equals to _______')

   answer1 = input('')

   if answer1.lower() == "755":
      print('Correct')

      score += 1 
      print('Your current score is : ', score)

   else: 
      print("Incorrect")
      print("Correct answer is 755 ")


   #que 6

   print('Question 6')

   print('Keyboard and mouse are hardware, true or false?')

   answer1 = input('')

   if answer1.lower() == "true":
      print('Correct')

      score += 1
      print('Your current score is : ', score)

   else: print("Incorrect")


   # que 7
   
  
   print('Question 7')

   print('What is the full form of GPU?')

   answer1 = input('')

   if answer1.lower() == "graphic processing unit":
      print('Correct')

      score += 1
      print('Your current score is : ', score)

   else: 
      print("Incorrect")
      print("Correct answer is graphic processing unit ")


   # que 8


   print('Question 8')

   print('The capital of Italy is _______ ')

   answer1 = input('')

   if answer1.lower() == "rome":
      print('Correct')

      score += 1
      print('Your current score is : ', score)

   else: 
      print("Incorrect")
      print("Correct answer is rome ")



   # que 9 


   print('Question 9')

   print('What is the full form of RGB?')

   answer1 = input('')

   if answer1.lower() == "red green blue":
      print('Correct')

      score += 1
      print('Your current score is : ', score)

   else: 
      print("Incorrect")
      print("Correct answer is Red Green Blue ")



   # que 10 


   print('Question 10')

   print('Which one is the largest planet in our solar system?')

   answer1 = input('')

   if answer1.lower() == "jupiter":
      print('Correct')

      score += 1
     

   else: 
      print("Incorrect")
      print("Correct answer is Jupiter ")



   print('GAME OVER, YOUR FINAL SCORE IS ', score )

   print("You got " + str((score / 10) * 100) + "%.")



elif age < 0:
   print("Write valid age please. ")

else:
   print("Sorry you are not eligible for the quiz. ")

   print("Game over ")

