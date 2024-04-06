import random

PLAYER = 0
COMPUTER = 0

options = {
  1: 'rock',
  2: 'paper',
  3: 'scissors'
}

def game():
  player = input('Choose rock, paper or scissors: ')
  player = player.lower()
  if player not in options.values():
    print('Invalid option')
    return game()
  computer = random.choice(list(options.values()))
  print(f'Computer chose {computer}')
  if player == computer:
    print('It\'s a tie!')
  elif player == 'rock' and computer == 'scissors' or player == 'paper' and computer == 'rock' or player == 'scissors' and computer == 'paper':
    print('You win!')
    return 1
  else:
    print('You lose!')
    return -1
  
def main():
  while True:
    global PLAYER
    global COMPUTER
    result = game()
    if result == 1:
      PLAYER += 1
    elif result == -1:
      COMPUTER += 1
    print(f'Player: {PLAYER} Computer: {COMPUTER}')
    play_again = input('Do you want to play again? (y/n): ')
    if play_again.lower() != 'y':
      break

main()