import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#rocka le gana a las tijeras
#tijeras le gana al papel
#papel le gana a la rocka
print('''
･*･.⠀⠀(\/)⠀⠀∧__∧ ･*･
'.　 (｡^ω^)(`ω´｡)　.'
⠀'･|　つ♡と　|.･'
⠀⠀⠀⠀*ﾟ'･｡｡･ﾟ'*
''')
print('♡ Welcome to the Game, Rock, Papper and the Scissors!!! ♡ \n')
images = [rock, paper, scissors]

usuario_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(images[usuario_option])

pc_choice = random.randint(0, 2)
print(f"Pc Chose {images[pc_choice]}")


if usuario_option >= 3 or usuario_option < 0:
  print('Invalid Number, try again')

elif usuario_option == 0 and pc_choice == 2:
  print('You Win!! (づ｡◕‿‿◕｡)づ')

elif pc_choice == 0 and usuario_option ==2:
  print('You Loose! o(╥﹏╥)o')

elif pc_choice > usuario_option:
  print('You Loose! o(╥﹏╥)o')

elif usuario_option > pc_choice:
  print('You Win!!! (づ｡◕‿‿◕｡)づ')\

elif usuario_option == pc_choice:
  print('Draw! v( ‘.’ )v')

else:
  pass