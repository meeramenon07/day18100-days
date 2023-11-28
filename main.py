
import emoji
print("Welcome to the Guess the Number guessing game! Enter any number between 0 and 1,000,000")
print()
correct_number = 70000
guess_attempts = 1
while True:
  your_guess = int(input("Enter your guess number between 1 and 1,000,000 : " ))
  if your_guess < 0:
    print("Sorry, you are disqualified!")
    exit()
  if your_guess < correct_number:
    print("Too Low! You didn't guess right! Try again!")
    guess_attempts += 1
  elif your_guess > correct_number:
    print("Too High! You didn't guess right! Try again!")
    guess_attempts += 1
    continue
  elif your_guess == correct_number:
    print("right!",emoji.emojize(":winking_face_with_tongue:"))
    
    
 
    break
  else:
    print("I dont recognize this!")
  
print("You guessed the correct number in", guess_attempts, "attempts!")
  
  
    
  
  
    
    
  
  
    
    

