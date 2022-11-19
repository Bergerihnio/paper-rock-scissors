import sys
print('\nHello in rock paper scissors (first player!)')
choose = ''
moves = ['paper', 'scissors', 'rock']

while not (choose in moves):
    choose = input('    Choose paper rock or scissors: ')
    if choose == moves[0]:
        print('     You choose a paper! 🧻 ')
    elif choose == moves[1]:
        print("     You choose scissors! ✂ ")
    elif choose == moves[2]:
        print('     You choose rock! 🪨 ')
    else:
        print('\nTry choose good option from the game like for example "rock" !!!')


import random
randomer = random.choice(moves)


if randomer == moves[0]:
    print('\n       Computer play paper! 🧻 ')
elif randomer == moves[1]:
    print('\n       Computer play scissors! ✂ ')
elif randomer == moves[2]:
    print('\n       Computer play rock! 🪨 ')

print("\n           Let's Fight 👊 ")


if choose == moves[0] and randomer == moves[0]:
    print('                 paper 🧻 vs paper 🧻 ')
    print('                     Draw!')
elif choose == moves[0] and randomer == moves[1]:
    print('             paper 🧻 vs scissors ✂')
    print('                 You loose 😥')
elif choose == moves[0] and randomer == moves[2]:
    print('             You Win 🎉')
elif choose == moves[1] and randomer == moves[0]:
    print('             scissors ✂ vs paper 🧻')
    print('                 You Win 🎉')
elif choose == moves[1] and randomer == moves[1]:
    print('             scissors ✂ vs scissors ✂')
    print('                     Draw!')
elif choose == moves[1] and randomer == moves[2]:
    print('             scissors ✂ vs rock 🪨')
    print('                 You loose 😥')
elif choose == moves[2] and randomer == moves[0]:
    print('             rock 🪨 vs paper 🧻')
    print('                 You loose 😥')
elif choose == moves[2] and randomer == moves[1]:
    print('             rock 🪨 vs scissors ✂')
    print('                 You Win 🎉')
elif choose == moves[2] and randomer == moves[2]:
    print('             rock 🪨 vs rock 🪨')
    print('                     Draw!')






