import random
game_list=['Rock', 'Paper','Scissors']
computer = c= 0
comand = p = 0
print("score :  Computer" + str(c) + "Comand" + str(p))
#The loop
run = True
while run:
	computer_choice = random.choice(game_list)
	comand = input('Rock, Paper, Scissors, or Quit : ')
	if comand == computer_choice:
		print("Tie")
	elif comand == "Rock":
		if computer_choice =="Scissors":
			print("Player won!")
			p+=1
		else :
			print("Computer won!")
			c+=1
	elif comand =="Paper":
		if comand =="Rock":
			print("Player won!")
			p+=1
		else:
			print('Computer won!')
			c +=1
	elif comand == "Scissors":
		if computer_choice =="Paper":
			print("Player won!")
			p+=1
		else:
			print('Computer won!')
			c +=1
	elif comand == 'Quit':
		break
	else:
		 print('Wrong comand!')
	print("Player:  "+ comand)
	print("Computer:  "+ computer_choice)
	print(' ')
	print("Score :  Computer" + str(c) + "Player" + str(p))