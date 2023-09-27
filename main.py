import random
choices = ['камень', 'ножницы', 'бумага']
player_choice = input('привет, для игры выбери камень, ножницы или бумагу:')
computer_choice = random.choice(choices)
print('ты выбрал:' + player_choice)
print('компьютер выбрал:' + computer_choice)

if player_choice == computer_choice:
    print('победила дружба!')
elif (player_choice == 'камень' and computer_choice == 'ножницы') or \
    (player_choice == 'ножницы' and computer_choice == 'бумага') or \
    (player_choice == 'бумага' and computer_choice == 'камень'):
    print('ты победил! поздравляем!')
else:
    print('победил компьютер')
