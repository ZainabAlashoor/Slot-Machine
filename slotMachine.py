import random

symbol = ['🍒',' 🍇', '🍉', '7️⃣']

def play():
  
  result = random.choices(symbol, k=3)

  print(f'{result[0]} | {result[1]} | {result[2]}')

  if result[0]=='7️⃣' and result[1]=='7️⃣' and result[2]=='7️⃣':
    print('Jackpot! 💰')
  else:
    print('Try Again!')


choice = input('Do you want to play? (Y/N) ')

while choice.upper() == 'Y':
  play()
  choice = input('Do you want to play again? (Y/N) ')
  choice.upper()