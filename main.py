import random, time, os


main_choices = ["rock","paper","scissors"]
green = "\033[0;32m"

def valid_answer(answer):
	if answer == main_choices[0] or answer == main_choices[1] or answer == main_choices[2]:
		return True
	else:
		return False

def wining_answers(answer1, answer2):
	if answer1 == "rock" and answer2 == "scissors":
		return True
	elif answer1 == "paper" and answer2 == "rock":
		return True
	elif answer1 == "scissors" and answer2 == "paper":
		return True
	else:
		return False

def draw(answer1, answer2):
	if answer1 == answer2:
		return True

def main():
	running = True
	while running:
		print(" type your choice: ")
		player_answer = input()


		#validating the answer
		switch = True
		while switch:
			if not valid_answer(player_answer):
				print("not a valid option, expecting: ", main_choices[0], main_choices[1], "or", main_choices[2])
				player_answer = input()
			else:
				switch = False

		#player and computer's choice
		print("you choose: ", player_answer)
		time.sleep(0.5)
		print("computer is thinking...")
		time.sleep(1)
		pc_answer = random.choice(main_choices)
		print("computer choose: ", pc_answer)
		print('\n')

		#if both answers are the same, it's a tie
		if draw(player_answer, pc_answer):
			print("IT'S A TIE!!!")
			#running = False

	  	#player wins
		if wining_answers(player_answer, pc_answer) == True:
			print(player_answer, " beats " ,pc_answer)
			print("YOU WIN!!!")
			#running = False

		#computer wins
		elif not wining_answers(player_answer, pc_answer) and not draw(player_answer, pc_answer):
			print(pc_answer, " beats ", player_answer)
			print("YOU LOOSE!, ")
			running = False

os.system("clear")
print(green)
print("### rock paper scissors game ###")
main()
print("have a good day")
