player1_input = "Player 1: Please choose rock, paper or scissors: "
player2_input = "Player 2: Please choose rock, paper or scissors: "

paper_rock 		= "Paper covers Rock"
rock_scissors  	= "Rock crushes Scissors"
scissors_paper	= "Scissors cuts Paper"
tie				= "It's a tie."

player1_response = raw_input(player1_input).lower()

while (
		player1_response.lower() != "rock" and
		player1_response.lower() != "paper" and
		player1_response.lower() != "scissors"
		):
	player1_response = raw_input(player1_input).lower()

player2_response = raw_input(player2_input).lower()

while (
		player2_response.lower() != "rock" and
		player2_response.lower() != "paper" and
		player2_response.lower() != "scissors"
		):
	player2_response = raw_input(player2_input).lower()

winner = "none";

if player1_response == "rock":
	if player2_response == "rock":
		winner = "both"
	elif player2_response == "paper":
		winner = "2"
		print paper_rock
	elif player2_response == "scissors":
		winner = "1"
		print rock_scissors

if player1_response == "paper":
	if player2_response == "rock":
		winner = "1"
		print paper_rock
	elif player2_response == "paper":
		winner = "both"
	elif player2_response == "scissors":
		winner = "2"
		print scissors_paper

if player1_response == "scissors":
	if player2_response == "rock":
		print rock_scissors
		winner = "2"
	elif player2_response == "paper":
		winner = "1"
		print scissors_paper
	elif player2_response == "scissors":
		winner = "both"

if winner == "1":
	print "The winner is player 1."
elif winner == "2":
	print "The winner is player 2."
elif winner == "both":
	print "It's a tie."