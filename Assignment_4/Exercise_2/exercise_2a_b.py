player1_input 	= "Player 1: Please choose rock, paper, scissors, lizard or spock: "
player2_input 	= "Player 2: Please choose rock, paper, scissors, lizard or spock: "

paper_rock 		= "Paper covers Rock"
paper_spock		= "Paper disproves Spock"
rock_scissors	= "Rock crushes Scissors"
rock_lizard		= "Rock crushes Lizard"
scissors_lizard = "Scissors decapitates Lizard"
scissors_paper	= "Scissors cuts Paper"
lizard_paper	= "Lizard eats Paper"
lizard_spock	= "Lizard poisons Spock"
spock_rock		= "Spock vaporizes Rock"
spock_scissors	= "Spock smashes Scissors"

player1_response = ""
player2_response = ""

while (
		player1_response.lower() != "rock" and
		player1_response.lower() != "paper" and
		player1_response.lower() != "scissors" and
		player1_response.lower() != "lizard" and
		player1_response.lower() != "spock"
		):
	player1_response = raw_input(player1_input).lower()


while (
		player2_response.lower() != "rock" and
		player2_response.lower() != "paper" and
		player2_response.lower() != "scissors" and
		player2_response.lower() != "lizard" and
		player2_response.lower() != "spock"
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
	elif player2_response == "lizard":
		winner = "1"
		print rock_lizard
	elif player2_response == "spock":
		winner = "2"
		print spock_rock

if player1_response == "paper":
	if player2_response == "rock":
		winner = "1"
		print paper_rock
	elif player2_response == "paper":
		winner = "both"
	elif player2_response == "scissors":
		winner = "2"
		print scissors_paper
	elif player2_response == "lizard":
		winner = "2"
		print lizard_paper
	elif player2_response == "spock":
		winner = "1"
		print paper_spock

if player1_response == "scissors":
	if player2_response == "rock":
		winner = "2"
		print rock_scissors
	elif player2_response == "paper":
		winner = "1"
		print scissors_paper
	elif player2_response == "scissors":
		winner = "both"
	elif player2_response == "lizard":
		winner = "1"
		print scissors_lizard
	elif player2_response == "spock":
		winner = "2"
		print spock_scissors

if player1_response == "lizard":
	if player2_response == "rock":
		winner = "2"
		print rock_lizard
	elif player2_response == "paper":
		winner = "1"
		print lizard_paper
	elif player2_response == "scissors":
		winner = "2"
		print scissors_lizard
	elif player2_response == "lizard":
		winner = "both"
	elif player2_response == "spock":
		winner = "1"
		print lizard_spock

if player1_response == "spock":
	if player2_response == "rock":
		winner = "1"
		print spock_rock
	elif player2_response == "paper":
		winner = "2"
		print paper_spock
	elif player2_response == "scissors":
		winner = "1"
		print spock_scissors
	elif player2_response == "lizard":
		winner = "2"
		print lizard_spock
	elif player2_response == "spock":
		winner = "both"


	

if winner == "1":
	print "The winner is player 1."
elif winner == "2":
	print "The winner is player 2."
elif winner == "both":
	print "It's a tie."
else:
	print "Something went wrong, there is no outcome!"