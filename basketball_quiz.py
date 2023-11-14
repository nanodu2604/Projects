print('Hello! This is my NBA basketball quiz!')

playing=input('Would you like to test your NBA knowledge and play? ')

if playing.lower() !="yes":
	print('Aw man, ok. Maybe next time :( ')
	quit()

print('Cool! Lets play :)')
score=0




answer=input("Ok, first question. Who is the NBA all-time leader in points? ").lower()
if answer=="lebron james" or answer.lower()=="lebron":
	print("Correct!")
	score +=1
else:
	print("Sorry, but that is not correct.")




answer=input("Here we go, second question. In the 2015-2016 season, what team won the NBA Finals? ").lower()
if answer.lower=="the cleveland cavaliers" or answer=="cleveland" or answer=="cavaliers" or answer=="cleveland cavaliers" or answer=="cavs":
	print("Correct!")
	score +=1
else:
	print("Sorry, but that is not correct.")




answer=input("Okay,third question. What is the name of the player that won the NBA Finals MVP in 2005? ").lower()
if answer=="tim duncan":
	print("Correct!")
	score +=1
else:
	print("Sorry, but that is not correct.")




answer=input("Fourth question, you got this! What year did Kevin Garnett win MVP? ").lower()
if answer=="2004" or answer=="2003-2004":
	print("Correct!")
	score +=1
else:
	print("Sorry, but that is not correct.")




answer=input("Here is question number five! What is the name of the player that has the most NBA MVP's in NBA history? ").lower()
if answer=="kareem" or answer=="kareem abdul jabbar":
	print("Correct!")
	score +=1
else:
	print("Sorry, but that is not correct.")




answer=input("For question number six, I will ask you a question about the 2016 NBA draft. In the 2016 NBA draft, who was drafted 2nd overall? ").lower()
if answer=="brandon ingram" or answer=="ingram" or answer=="bi":
	print("Correct!")
	score +=1
else:
	print("Sorry, but that is not correct.")




answer=input("Question number seven, only two more left! In 2013, what player won the NBA Most Improved Player award? ").lower()
if answer=="paul george" or answer=="pg13":
	print("Correct!")
	score +=1
else:
	print("Sorry, but that is not correct.")




answer=input("Last question,question number eight! What team drafted Kobe Bryant in the 1996 NBA draft? ").lower()
if answer=="charlotte hornets" or answer=="hornets" or answer=="charlotte":
	print("Correct!")
	score +=1
else:
	print("Sorry,but that is not correct.")




final_score=input("Those were all of the questions. Would you like to know how many questions you got correct? ")
if final_score.lower()!="yes":
	print("Okay,thank you for playing!")
	quit()
print("You got " + str(score) + " questions correct! ")
print("You got " + str((score / 8)*100)+ "%" " of the questions correct!")
print("Thank you for playing!")