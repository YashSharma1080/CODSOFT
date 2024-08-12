while True :
   print('\033[94;1m' + 'Welcome to the Rock-Paper-Scissors Game' '\033[0m')
   c1 = ("A knockout")
   c2 = ("A 5 points game")
   c3 = input("What would you like to play 'A knockout' or 'A 5 points game'(type c1 for a knockout and c2 for a points game):")
   if c3 == "c1" :
      print("Starting a knockout game against computer")
      c4 = input('\033[91;1m'  +  "Make a choice between Rock-Paper-Scissors"  '\033[0m')
      if c4 == "Rock" :
         print("Computer is choosing.......")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[93;1m' + "It's a tie!  :|"  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
               print("Starting a knockout game against computer")
            if yn == "no":
               print("Thanks for playing!")
               break 
         if computer_choice == "Paper":
            print('\033[95;1m' + "Computer wins!  :( "  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
               print("Starting a knockout game against computer")
            if yn == "no":
               print("Thanks for playing")
               break
         if computer_choice == "Scissors":
            print('\033[92;1m' + "You win!  :)"  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
               print("Starting a knockout game against computer")
            if yn == "no":
               print("Thanks for playing!")
               break
      if c4 == "Paper" :
         print("Computer is choosing.......")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[92;1m' + "You win!  :)"  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
                print("Starting a knockout game against computer")
            if yn == "no":
                print("Thanks for playing!")
                break
         if computer_choice == "Paper":
            print('\033[93;1m' + "It's a tie!   :|"  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
                print("Starting a knockout game against computer")
            if yn == "no":
                print("Thanks for playing!")
                break
         if computer_choice == "Scissors":
            print('\033[95;1m' + "Computer wins!   :("  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
                print("Starting a knockout game against computer")
            if yn == "no":
                print("Thanks for playing!")
                break
      if c4 == "Scissors" :                       
        print("Computer is choosing.......")
        import random
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)
        if computer_choice == "Rock":
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
             print("Starting a knockout game against computer")
            if yn == "no":
             print("Thanks for playing!")
             break
        if computer_choice == "Paper":
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
             print("Starting a knockout game against computer")
            if yn == "no":
             print("Thanks for playing!")
             break
        if computer_choice == "Scissors":
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
            yn = input("Want to play again?(yes|no):")
            if yn == "yes" :
             print("Starting a knockout game against computer")
            if yn == "no":
             print("Thanks for playing!")
             break
   if c3 == "c2" :
      print("Starting a 5 points game against computer")
      print('\033[36;1m'  +  "ROUND 1"  '\033[0m')
      YourScore = 0
      ComputerScore = 0
      c5 = input('\033[91;1m'  +  "Make a choice between Rock-Paper-Scissors"  '\033[0m')
      if c5 == "Rock" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Paper" :
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore, "Computer:" , ComputerScore ) 
         if computer_choice == "Scissors" :
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore, "Compputer:" , ComputerScore )       
      if c5 == "Paper" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore, "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore, "Computer:" , ComputerScore )
      if c5 == "Scissors" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore, "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore, "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')      
      print('\033[36;1m'  +  "ROUND 2"  '\033[0m')
      c5 = input('\033[91;1m'  +  "Make a choice between Rock-Paper-Scissors"  '\033[0m')
      if c5 == "Rock" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Paper" :
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore, "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )      
      if c5 == "Paper" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore, "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
      if c5 == "Scissors" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')  
      print('\033[36;1m'  +  "ROUND 3"  '\033[0m')
      c5 = input('\033[91;1m'  +  "Make a choice between Rock-Paper-Scissors"  '\033[0m')
      if c5 == "Rock" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
      if c5 == "Paper" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" ,  ComputerScore )
         if computer_choice == "Paper" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" ,  ComputerScore )
      if c5 == "Scissors" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore ,"Computer:" ,  ComputerScore )
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')  
      print('\033[36;1m'  +  "ROUND 4"  '\033[0m')
      c5 = input('\033[91;1m'  +  "Make a choice between Rock-Paper-Scissors"  '\033[0m')
      if c5 == "Rock" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" ,  ComputerScore )      
      if c5 == "Paper" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
      if c5 == "Scissors" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
      print('\033[36;1m'  +  "ROUND 5(final round)"  '\033[0m')
      c5 = input('\033[91;1m'  +  "Make a choice between Rock-Paper-Scissors"  '\033[0m')
      if c5 == "Rock" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )      
      if c5 == "Paper" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')
         if computer_choice == "Scissors" :
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
      if c5 == "Scissors" :
         print("Computer is choosing.....")
         import random
         choices = ["Rock", "Paper", "Scissors"]
         computer_choice = random.choice(choices)
         print("Computer chose:", computer_choice)
         if computer_choice == "Rock":
            print('\033[95;1m'  +  "Computer wins!  :("  '\033[0m')
            ComputerScore = ComputerScore + 1
            print("You:", YourScore , "Computer:" , ComputerScore )
         if computer_choice == "Paper" :
            print('\033[92;1m'  +  "You win!  :)"  '\033[0m')
            YourScore = YourScore + 1
            print("You:", YourScore , "Computer:", ComputerScore )
         if computer_choice == "Scissors" :
            print('\033[93;1m'  +  "It's a tie!  :|"  '\033[0m')     
      TotalScore = ('You:',YourScore  , 'Computer:',ComputerScore)
      print()
      print('TotalScore:', TotalScore)
      if YourScore > ComputerScore :
         print()
         print('\033[92;1;4m'  +  "Congratulations! You won the game!"  '\033[0m')
      if ComputerScore > YourScore :
         print()
         print('\033[95;1;4m'  +  "Sorry, you lost the game!"  '\033[0m')
      if YourScore == ComputerScore :
         print()
         print('\033[93;1;4m'  +  "It's a tie!"  '\033[0m')
         print()      
      yn = input("Wnat to play again(yes/no):")
      if yn == "yes" :
         continue
      if yn == "no" :
         print("Thank you for playing :-)")
         break          



                                               
                    
