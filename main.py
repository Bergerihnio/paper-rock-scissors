import sys
print('\nHello in rock paper scissors (first player!)')
choose = ''
moves = ['paper', 'scissors', 'rock']

while not (choose in moves):
    choose = input('    Choose paper rock or scissors: ')
    if choose == moves[0]:
        print('     You choose a paper! ๐งป ')
    elif choose == moves[1]:
        print("     You choose scissors! โ ")
    elif choose == moves[2]:
        print('     You choose rock! ๐ชจ ')
    else:
        print('\nTry choose good option from the game like for example "rock" !!!')


import random
randomer = random.choice(moves)


if randomer == moves[0]:
    print('\n       Computer play paper! ๐งป ')
elif randomer == moves[1]:
    print('\n       Computer play scissors! โ ')
elif randomer == moves[2]:
    print('\n       Computer play rock! ๐ชจ ')

print("\n           Let's Fight ๐ ")


if choose == moves[0] and randomer == moves[0]:
    print('                 paper ๐งป vs paper ๐งป ')
    print('                     Draw!')
elif choose == moves[0] and randomer == moves[1]:
    print('             paper ๐งป vs scissors โ')
    print('                 You loose ๐ฅ')
elif choose == moves[0] and randomer == moves[2]:
    print('             You Win ๐')
elif choose == moves[1] and randomer == moves[0]:
    print('             scissors โ vs paper ๐งป')
    print('                 You Win ๐')
elif choose == moves[1] and randomer == moves[1]:
    print('             scissors โ vs scissors โ')
    print('                     Draw!')
elif choose == moves[1] and randomer == moves[2]:
    print('             scissors โ vs rock ๐ชจ')
    print('                 You loose ๐ฅ')
elif choose == moves[2] and randomer == moves[0]:
    print('             rock ๐ชจ vs paper ๐งป')
    print('                 You loose ๐ฅ')
elif choose == moves[2] and randomer == moves[1]:
    print('             rock ๐ชจ vs scissors โ')
    print('                 You Win ๐')
elif choose == moves[2] and randomer == moves[2]:
    print('             rock ๐ชจ vs rock ๐ชจ')
    print('                     Draw!')






