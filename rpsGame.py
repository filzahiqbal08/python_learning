import sys, random
print('Rock, Paper, Scissors')

wins = 0
losses = 0
ties = 0

while True: #main game loop
    print(wins, 'Wins', losses, 'Losses', ties, 'Ties')
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_move = input('>')
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or 'p' or 's':
            break
        print('Type one: r,s,p, or q')
    
    if player_move == 'r':
        print('Rock versus...')
    elif player_move == 'p':
        print('Paper versus...')
    elif player_move == 's':
        print('Scissors versus...')

    computer_num = random.randint(1,3)
    if computer_num == 1:
        computer_move = 'r'
        print('ROCK')
    elif computer_num == 2:
        computer_move = 'p'
        print('PAPER')
    elif computer_num == 3:
        computer_move = 's'
        print('SCISSORS')

    if player_move == computer_move:
        print('Tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lost')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lost')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose')
        losses = losses + 1
