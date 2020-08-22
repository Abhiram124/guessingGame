import random 
  
print("Number guessing game") 
answer = random.randint(1, 9) 
chances = 0
  
print("Guess a number (between 1 and 9):")  
  
while chances < 5: 
    guess = int(input()) 
      
    if guess == answer:  
        print("Congratulation YOU WIN!!:)") 
        break    
    
    elif guess < answer: 
        print("Your guess was too low: Try again next time", guess) 
            
    else: 
        print("Your guess was too high: Try again next time", guess) 
          
    chances += 1
          
if not chances < 5: 
    print("YOU LOSE!! :( The number is", answer) 

