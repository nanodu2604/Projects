import random

user_wins=0
cpu_wins=0

options = ["rock", "paper", "scissors"]

while True:
	user_input=input("Type Rock,Paper,or Scissors. If you wish to quit type Q: ").lower()
	if user_input == "q":
		break

	if user_input not in options:
		continue

	random_number = random.randint(0,2)
	#rock: 0, paper: 1, scissors: 2
	cpu_pick=options[random_number]
	print("The computer picked", cpu_pick + ".")


	if user_input=="rock" and cpu_pick=="scissors":
		print("You won!")
		user_wins+=1
		

	elif user_input=="paper" and cpu_pick=="rock":
		print("You won!")
		user_wins+=1
		

	elif user_input=="scissors" and cpu_pick=="paper":
		print("You won!")
		user_wins+=1
	
	else:
		print("You lost!")
		cpu_wins+=1




print("You won", user_wins, "times.")

print("The computer won", cpu_wins, "times")

print("Goodbye!")


